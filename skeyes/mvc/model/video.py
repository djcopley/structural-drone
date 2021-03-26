import cv2
import logging

logger = logging.getLogger(__name__)


class Video:
    def __init__(self, capture_device: int, host="127.0.0.1", port="5600"):
        # Default camera device should be device 0, however, if user has multiple webcams, it may be something
        # different.
        self._capture_devnum = None
        self._capture_device = None
        self._stream_device = None

        self.set_capture_device(capture_device)
        self.set_stream_device(host, port)

    def set_capture_device(self, capture_device):
        try:
            # Release the capture device handle first
            self._capture_device.release()
        except AttributeError:
            pass
        # Update to new device
        self._capture_devnum = capture_device
        self._capture_device = cv2.VideoCapture(capture_device)

    def set_stream_device(self, host, port):
        try:
            # Release stream device handle first
            self._stream_device.release()
        except AttributeError:
            pass

        codec = 0
        fps = 20
        img_dimension = (640 * 2, 480 * 2)
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
            logger.error("Couldn't access capture device number: {}".format(self._capture_devnum))
        # NOTE: Potential bug. If downstream streamer expects frame, this method might return None if invalid
        # video capture device
        return frame  # BUG

    def stream_frame(self, frame):
        self._stream_device.write(frame)

    def release(self):
        self._capture_device.release()
        self._stream_device.release()


if __name__ == '__main__':
    video = Video(0)

    while True:
        frame = video.get_frame()
        cv2.imshow("test", video.get_frame())

        video.stream_frame(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    video.release()
