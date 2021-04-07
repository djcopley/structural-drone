import cv2
import numpy as np
import logging

from skeyes.model import *

logger = logging.getLogger(__name__)


class Detection:
    def __init__(self, name, class_id, confidence, box):
        self.name = name
        self.class_id = class_id
        self.confidence = confidence

        # np.array
        self.box = box  # Box format: [min_x, min_y, max_x, max_y]

        # Convert box from [x y w h] to [min_x, min_y, max_x, max_y]
        self.box[2] = self.box[0] + self.box[2]
        self.box[3] = self.box[1] + self.box[3]

    def __str__(self):
        return "Detection: {} at {}, {:.2%} confident".format(self.name, self.box, self.confidence)

    def __repr__(self):
        return str(self)


class YoloV4:
    def __init__(self, cfg: str, weights: str, names: list, input_size: int = 416, conf_threshold: float = 0.5,
                 nms_threshold: float = 0.4):
        self.dnn = cv2.dnn_DetectionModel(cfg, weights)

        # Always prefer GPU acceleration
        self.dnn.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        self.dnn.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

        self.names = names

        assert input_size % 32 == 0, "input_size must be a multiple of 32"

        self.dnn.setInputSize(input_size, input_size)
        self.dnn.setInputScale(1.0 / 255)
        self.dnn.setInputSwapRB(True)

        assert 0 < conf_threshold < 1.0, "conf_threshold must be normalized"
        assert 0 < nms_threshold < 1.0, "nms_threshold must be normalized"
        self.conf_threshold = conf_threshold
        self.nms_threshold = nms_threshold

    def run_inference(self, image: np.array):
        classes, confidences, boxes = self.dnn.detect(image, confThreshold=self.conf_threshold,
                                                      nmsThreshold=self.nms_threshold)
        detections = []
        try:
            for class_id, confidence, box in zip(classes.flatten(), confidences.flatten(), boxes):
                detections.append(Detection(self.names[class_id], class_id, confidence, box))
        except AttributeError:
            pass

        return detections


if __name__ == '__main__':
    from skeyes.model.utils import image_annotate

    yolo = YoloV4(YOLO_MODEL_CFG, YOLO_MODEL_WEIGHTS, ["Window", "Gutter"])

    frame = cv2.imread("yolo/test/img4.png")

    for detection in yolo.run_inference(frame):
        min_x, min_y, max_x, max_y = detection.box
        frame = image_annotate(frame, min_x, min_y, max_x, max_y,
                               text="{}: {:.2%}".format(detection.name, detection.confidence))

    cv2.imshow('frame', frame)
    print(yolo.run_inference(frame))
    cv2.waitKey(0)
