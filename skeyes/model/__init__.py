import os

YOLO_DIR = os.path.join(os.path.dirname(__file__), "yolo")

YOLO_MODEL_CFG = os.path.join(YOLO_DIR, "yolov4-obj.cfg")
YOLO_MODEL_WEIGHTS = os.path.join(YOLO_DIR, "yolov4-obj_best.weights")
YOLO_CLASS_NAMES = os.path.join(YOLO_DIR, "obj.names")

TF_CLASSIFIER_DIR = os.path.join(os.path.dirname(__file__), "tf_classifiers")
TF_CLASSIFIER_MODEL_WINDOW = os.path.join(TF_CLASSIFIER_DIR, "window.h5")
TF_CLASSIFIER_MODEL_GUTTER = os.path.join(TF_CLASSIFIER_DIR, "gutter.h5")
