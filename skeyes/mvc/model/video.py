import cv2
import logging

logger = logging.getLogger(__name__)


class Video:
    def __init__(self, device: int):
        # Default camera device should be device 0, however, if user has multiple webcams, it may be something
        # different.
        self.capture_device = device

    @property
    def capture_device(self):
        # Return the OpenCV device handle number
        return self._devnum

    @capture_device.setter
    def capture_device(self, device: int):
        """
        Method updates the current video capture device
        """
        self._devnum = device
        self._device = cv2.VideoCapture(device)

    def get_frame(self):
        """
        Method returns a frame from the specified video input device.
        """
        ret, frame = self._device.read()
        if not ret:
            # Logger, print couldn't get frame for current device
            logger.error("Couldn't access capture device number: {}".format(self._devnum))
        # NOTE: Potential bug. If downstream streamer expects frame, this method might return None if invalid
        # video capture device
        # BUG
        return frame


if __name__ == '__main__':
    video = Video(0)
    cv2.imshow("test", video.get_frame())
    cv2.waitKey(0)
