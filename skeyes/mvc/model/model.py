import cv2
import logging

from skeyes.mvc.model import *
from skeyes.mvc.model.utils import *
from skeyes.mvc.model.yolo import YoloV4, Detection
from skeyes.mvc.model.video import Video


class Model:
    def __init__(self, video_device_handle, gst_ip_address, gst_port):
        self.running = True

        # TODO make getters and setters for the following parameters that way the controller can update objects easily
        # Configuration options
        # ----------------------
        # Webcam opencv device handle - ie: 0, 1, 2, 3
        self.video_device_handle = video_device_handle
        # Gstreamer udp stream ip (this is the destination ip)
        self.gst_ip_address = gst_ip_address
        # Gstreamer port
        self.gst_port = gst_port

        self.video = Video(self.video_device_handle)

    def start(self):
        while self.running:
            # Get video frame
            frame = self.video.get_frame()
            # Run detection
            # Crop
            # Run Classification
            # Annotate
            # Action Generation
            # Stream to user
            pass


if __name__ == '__main__':
    # cap = cv2.VideoCapture(os.path.join(YOLO_DIR, "video1.mov"))
    # cap = cv2.VideoCapture(
    #     os.path.join(YOLO_DIR, "/home/djcopley/Documents/School/Capstone/drone-footage/GPS_TEST_FLIGHT.mp4"))
    cap = Video(0)
    yolo = YoloV4(YOLO_MODEL_CFG, YOLO_MODEL_WEIGHTS, extract_class_names(YOLO_CLASS_NAMES))

    while True:
        frame = cap.get_frame()
        for detection in yolo.run_inference(frame):
            min_x, min_y, max_x, max_y = detection.box
            frame = image_annotate(frame, min_x, min_y, max_x, max_y,
                                   text="{}: {:.2%}".format(detection.name, detection.confidence))
        cv2.imshow('frame', frame)
        cap.stream_frame(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
