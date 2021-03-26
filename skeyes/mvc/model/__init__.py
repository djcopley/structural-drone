import os

YOLO_DIR = os.path.join(os.path.dirname(__file__), "yolo")

YOLO_MODEL_CFG = os.path.join(YOLO_DIR, "yolov4-obj.cfg")
YOLO_MODEL_WEIGHTS = os.path.join(YOLO_DIR, "yolov4-obj_best.weights")

TF_CLASSIFIER_DIR = os.path.join(os.path.dirname(__file__), "tf_classifier")
TF_CLASSIFIER_WEIGHTS = os.path.join(TF_CLASSIFIER_DIR, "")
