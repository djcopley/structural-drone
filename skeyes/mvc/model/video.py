import cv2
import logging

from goprocam import GoProCamera
# from goprocam import constants

logger = logging.getLogger(__name__)


class Video:
    def __init__(self, host="127.0.0.1", port="5600"):
        # Configure GoPro camera
        self._go_pro = GoProCamera.GoPro()

        # If we decide to go the no ffmpeg route
        # self._go_pro.livestream("start")
        # self._capture_uri = "udp://10.5.5.9:8554"

        self._capture_uri = "udp://127.0.0.1:10000"
        self._capture_device = cv2.VideoCapture(self._capture_uri)

        # Configure GStreamer
        self._stream_device = None
        self.configure_stream(host, port)

    def configure_stream(self, host, port):
        try:
            # Release stream device handle first
            self._stream_device.release()
        except AttributeError:
            pass

        codec = 0
        fps = 20
        img_dimension = (432, 240)
        is_color = True

        self._stream_device = cv2.VideoWriter(
            "appsrc ! videoconvert ! x264enc tune=zerolatency speed-preset=superfast ! rtph264pay ! "
            "udpsink host={} port={}".format(host, port),
            cv2.CAP_GSTREAMER, codec, fps, img_dimension, is_color)

    def get_frame(self):
        """
        Method returns a frame from the specified video input device.
        """
        ret, frame = self._capture_device.read()
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


if __name__ == '__main__':
    video = Video()

    while True:
        frame = video.get_frame()
        cv2.imshow("test", video.get_frame())

        video.stream_frame(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    video.release()
