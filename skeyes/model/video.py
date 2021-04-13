import cv2
import logging
import socket
import time
import threading

from goprocam import GoProCamera

logger = logging.getLogger(__name__)


class CameraBufferCleanerThread(threading.Thread):
    """
    Flush the image buffer continuously. https://stackoverflow.com/a/65191619/6876488
    """
    def __init__(self, camera, name='camera-buffer-cleaner-thread'):
        self.camera = camera
        self.running = True
        self.last_frame = None
        self.ret = None
        super(CameraBufferCleanerThread, self).__init__(name=name)
        self.start()

    def run(self):
        while self.running:
            self.ret, self.last_frame = self.camera.read()

    def stop(self):
        self.running = False

    def read(self):
        return self.ret, self.last_frame


class Video:
    def __init__(self, host="127.0.0.1", port="5600"):
        # Configure GoPro camera
        self._go_pro = GoProCamera.GoPro()

        self._go_pro.livestream("start")
        self._capture_uri = "udp://10.5.5.9:8554"

        self._host = host
        self._port = port

        self._capture_device = cv2.VideoCapture(self._capture_uri)
        self._video_buffer = CameraBufferCleanerThread(self._capture_device)

        self._go_pro_keep_alive = 2.5  # keep alive time in seconds
        self._go_pro_last_checkin = time.time()
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Configure GStreamer
        self._stream_device = None
        self._configure_stream()

    def set_host(self, host):
        self._host = host
        self._configure_stream()

    def set_port(self, port):
        self._port = port
        self._configure_stream()

    def _configure_stream(self):
        if self._stream_device:
            # Release stream device handle first
            self._stream_device.release()

        codec = 0
        fps = 20
        img_dimension = (432, 240)  # Video dimensions from the gopro stream
        # img_dimension = (1280, 960)
        is_color = True

        self._stream_device = cv2.VideoWriter(
            "appsrc ! videoconvert ! x264enc tune=zerolatency speed-preset=superfast ! rtph264pay ! "
            "udpsink host={} port={}".format(self._host, self._port),
            cv2.CAP_GSTREAMER, codec, fps, img_dimension, is_color)

    def keep_alive(self):
        if time.time() - self._go_pro_last_checkin >= self._go_pro_keep_alive:
            # print("Checkin")
            self._sock.sendto("_GPHD_:0:0:2:0.000000\n".encode(), ("10.5.5.9", 8554))
            self._go_pro_last_checkin = time.time()

    def get_frame(self):
        """
        Method returns a frame from the specified video input device.
        """
        # Make sure keep alive sends request to gopro
        self.keep_alive()

        ret, frame = self._video_buffer.read()
        if not ret:
            # Logger, print couldn't get frame for current device
            logger.error("Couldn't access capture device number: {}".format(self._capture_uri))
        # NOTE: Potential bug. If downstream streamer expects frame, this method might return None if invalid
        # video capture device
        return frame  # BUG

    def stream_frame(self, frame):
        self._stream_device.write(frame)

    def release(self):
        self._capture_device.release()
        self._stream_device.release()
        self._go_pro.livestream("stop")


if __name__ == '__main__':
    video = Video()

    while True:
        frame = video.get_frame()
        cv2.imshow("test", frame)

        video.stream_frame(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(1)

    video.release()
    cv2.destroyAllWindows()
