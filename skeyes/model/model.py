import logging

from skeyes.model import *
from skeyes.model.utils import *
from skeyes.model.action import Action
from skeyes.model.classifier import Classifier
from skeyes.model.video import Video
from skeyes.model.yolo import YoloV4, Detection

logger = logging.getLogger(__name__)


class Model:
    def __init__(self):
        self.running = True

        self.action = Action()
        # self.classifier = Classifier()
        self.video = Video()
        self.yolo = YoloV4(YOLO_MODEL_CFG, YOLO_MODEL_WEIGHTS, extract_class_names(YOLO_CLASS_NAMES))
        # self.test = cv2.VideoCapture(0)

    def start(self):
        while self.running:
            # Get video frame
            frame = self.video.get_frame()
            if frame is not None:
                # Run detections
                detections = self.yolo.run_inference(frame)
                for detection in detections:
                    # Get the detection bounds
                    min_x, min_y, max_x, max_y = detection.box
                    # Crop the image to the detection bounds
                    cropped_img = image_crop(frame, min_x, min_y, max_x, max_y)
                    # Classify defective or nominal
                    defective = False  # self.classifier.predict(cropped_img, detection.name)  # True if damaged
                    # Get the frame
                    frame = image_annotate(frame, min_x, min_y, max_x, max_y,
                                           f"{'Defective' if defective else 'Nominal'} {detection.name}", defective)
                    # Generate action if defective
                    # if defective:
                    #     self.action.generate_action(detection.name)
                # Stream video frame out to UDP port
                self.video.stream_frame(frame)

    def stop(self):
        self.running = False
        self.video.release()

    def set_qgc_ip(self, ip):
        self.video.set_host(ip)

    def set_qgc_port(self, port):
        self.video.set_port(port)

    def set_logging_file_path(self, fp):
        pass

    def get_actions(self):
        return

    def set_action(self, img_class, action):
        self.action.set_action(img_class, action)


if __name__ == '__main__':
    model = Model()
    model.start()
