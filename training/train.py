from training import *

import numpy as np
import os
import cv2
import random
import tensorflow as tf

nn_class = "gutter"
data_dir = os.path.join(DATASET_DIR, nn_class)
categories = os.listdir(data_dir)

print(data_dir)
print(categories)

img_size = 128
window_nodes = 32
gutter_nodes = 128

training_data = []


def create_training_data():
    for category in categories:
        path = os.path.join(data_dir, category)
        class_num = categories.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (img_size, img_size))
                training_data.append([new_array, class_num])
            except:
                pass


create_training_data()

random.shuffle(training_data)

X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1, img_size, img_size, 1)
y = np.array(y)

window = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(window_nodes, (3, 3), activation='relu', input_shape=X.shape[1:]),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(window_nodes, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(window_nodes, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(window_nodes, activation='relu'),
    tf.keras.layers.Dense(window_nodes, activation='relu'),

    tf.keras.layers.Dense(1, activation='sigmoid')
])

gutter = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(gutter_nodes, (3, 3), activation='relu', input_shape=X.shape[1:]),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(gutter_nodes, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(gutter_nodes, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(1, activation='sigmoid')
])

if nn_class == "window":
    window.compile(loss="binary_crossentropy",
                  optimizer="adam",
                  metrics=['accuracy'])
    window.fit(X, y, batch_size=8, epochs=15, validation_split=0.2)
    window.save('window.h5')

elif nn_class == "gutter":
    gutter.compile(loss="binary_crossentropy",
                  optimizer="adam",
                  metrics=['accuracy'])
    gutter.fit(X, y, batch_size=32, epochs=20, validation_split=0.2)
    gutter.save('gutter.h5')

else:
    pass
