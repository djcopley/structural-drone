import cv2
import numpy as np
import tensorflow as tf

from skeyes.model import *


class Classifier:
    def __init__(self, ):
        # Model initialization
        self.img_size = 128
        self.input_shape = (self.img_size, self.img_size, 1)  # 1 for grayscale

        self.window_nodes = 32
        self.gutter_nodes = 128

        self.window = tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(self.window_nodes, (3, 3), activation='relu', input_shape=self.input_shape),
            tf.keras.layers.MaxPooling2D(2, 2),
            tf.keras.layers.Conv2D(self.window_nodes, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D(2, 2),
            tf.keras.layers.Conv2D(self.window_nodes, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D(2, 2),

            tf.keras.layers.Flatten(),

            tf.keras.layers.Dense(self.window_nodes, activation='relu'),
            tf.keras.layers.Dense(self.window_nodes, activation='relu'),

            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        self.gutter = tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(self.gutter_nodes, (3, 3), activation='relu', input_shape=self.input_shape),
            tf.keras.layers.MaxPooling2D(2, 2),
            tf.keras.layers.Conv2D(self.gutter_nodes, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D(2, 2),
            tf.keras.layers.Conv2D(self.gutter_nodes, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D(2, 2),

            tf.keras.layers.Flatten(),

            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        self.window.compile(loss="binary_crossentropy",
                            optimizer="adam",
                            metrics=['accuracy'])
        self.window.load_weights(TF_CLASSIFIER_MODEL_WINDOW)

        self.gutter.compile(loss="binary_crossentropy",
                            optimizer="adam",
                            metrics=['accuracy'])
        self.gutter.load_weights(TF_CLASSIFIER_MODEL_GUTTER)

    def format_image(self, image):
        resized_img = np.array(image).reshape(-1, self.img_size, self.img_size, 1)  # expected warning
        sobel_kernel_x = np.array(([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]), np.float32) / 9
        sobel_kernel_y = np.array(([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]), np.float32) / 9

        sobel_x = cv2.filter2D(src=resized_img, kernel=sobel_kernel_x, ddepth=-1)
        sobel_y = cv2.filter2D(src=resized_img, kernel=sobel_kernel_y, ddepth=-1)

        new_img = np.sqrt(np.square(sobel_x) + np.square(sobel_y))
        new_img *= 255.0 / new_img.max()

        return new_img

    def predict(self, image, cls):
        if cls == 'window':
            image = self.format_image(image)
            prediction = self.window.predict(image, batch_size=1)
            dmg_class = np.argmax(prediction, axis=1)
        elif cls == 'gutter':
            image = self.format_image(image)
            prediction = self.window.predict(image, batch_size=1)
            dmg_class = np.argmax(prediction, axis=1)
        else:
            return None

        return not dmg_class[0]


if __name__ == '__main__':
    classifier = Classifier()
