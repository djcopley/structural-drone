import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
import cv2
from tensorflow import keras

print(tf.__version__)

##############################################################################
# Basic linear equation recognition
# Equation: y = 3x + 1
#
# model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
#
# model.compile(optimizer='sgd', loss='mean_squared_error')
#
# xs = np.array([-2.0, -1.0, 0, 1.0, 2.0, 3.0, 4.0], dtype=float)
# ys = np.array([-5.0, -2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)
#
# model.fit(xs, ys, epochs=500)
#
# print(model.predict([20]))

#################################################################################
# Basic Computer Vision


# If I would like the training to stop at a certain threshold
# class MyCallback(tf.keras.callbacks.Callback):
#     def on_epoch_end(self, epoch, logs={}):
#         if logs.get('accuracy') > 0.9:
#             print("\nReached 90% accuracy so cancelling training!")
#             self.model.stop_training = True
#
#
# callbacks = MyCallback()
# mnist = keras.datasets.fashion_mnist
# (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
#
# plt.imshow(train_images[0])
# plt.gray()
# plt.show()
# print(train_labels[0])
# print(train_images[0])
#
# train_images = train_images / 255.0
# test_images = test_images / 255.0
#
# model = tf.keras.models.Sequential([
#     keras.layers.Flatten(input_shape=(28, 28)),
#     keras.layers.Dense(128, activation=tf.nn.relu),
#     keras.layers.Dense(10, activation=tf.nn.softmax)])
#
# model.compile(optimizer=tf.keras.optimizers.Adam(),
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])
#
# model.fit(train_images, train_labels, epochs=10)
#
# print("\nTest Evaluation Results:")
# model.evaluate(test_images, test_labels)
#
# # model.fit(train_images, train_labels, epochs=5)
# # model.evaluate(test_images, test_labels)
# # model.fit(train_images, train_labels, epochs=5)
# # model.evaluate(test_images, test_labels)
#
# classifications = model.predict(test_images)
# test_index = 0
#
# print(classifications[test_index])
# print(test_labels[test_index])

#################################################################################
# Convolutional Neural Network

# # Start off with basic convolution functions on image
# ascent = misc.ascent()
# print(ascent.shape)
# # noinspection PyArgumentList
# print(ascent.max())
#
# # plt.gray()
# # plt.grid(False)
# # plt.axis('off')
# # plt.imshow(ascent)
# # plt.show()
#
# ascent_transformed = np.copy(ascent)
# size_x = ascent_transformed.shape[0]
# size_y = ascent_transformed.shape[1]
#
# # This filter detects edges nicely
# # It creates a convolution that only passes through sharp edges and straight
# # lines.
#
# # Experiment with different values for fun effects.
# # filter = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]  # Sharper Edges?
#
# # A couple more filters to try for fun!
# filter = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]  # Vertical Lines
# # filter = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]  # Horizontal Lines
#
# # If all the digits in the filter don't add up to 0 or 1, you
# # should probably do a weight to get it to do so
# # so, for example, if your weights are 1,1,1 1,2,1 1,1,1
# # They add up to 10, so you would set a weight of .1 if you want to normalize them
# weight = 1
#
# # for x in range(1, size_x - 1):
# #     for y in range(1, size_y - 1):
# #         convolution = 0.0
# #         convolution = convolution + (ascent[x - 1, y - 1] * filter[0][0])
# #         convolution = convolution + (ascent[x, y - 1] * filter[0][1])
# #         convolution = convolution + (ascent[x + 1, y - 1] * filter[0][2])
# #         convolution = convolution + (ascent[x - 1, y] * filter[1][0])
# #         convolution = convolution + (ascent[x, y] * filter[1][1])
# #         convolution = convolution + (ascent[x + 1, y] * filter[1][2])
# #         convolution = convolution + (ascent[x - 1, y + 1] * filter[2][0])
# #         convolution = convolution + (ascent[x, y + 1] * filter[2][1])
# #         convolution = convolution + (ascent[x + 1, y + 1] * filter[2][2])
# #         convolution = convolution * weight
# #         if convolution < 0:
# #             convolution = 0
# #         if convolution > 255:
# #             convolution = 255
# #         ascent_transformed[x, y] = convolution
#
# # Plot the image. Note the size of the axes -- they are 512 by 512
# # plt.gray()
# # plt.grid(False)
# # plt.imshow(ascent_transformed)
# # # plt.axis('off')
# # plt.show()
#
# # Picture Compression
# new_x = int(size_x / 2)
# new_y = int(size_y / 2)
# newImage = np.zeros((new_x, new_y))
# for x in range(0, size_x, 2):
#     for y in range(0, size_y, 2):
#         pixels = []
#         pixels.append(ascent_transformed[x, y])
#         pixels.append(ascent_transformed[x + 1, y])
#         pixels.append(ascent_transformed[x, y + 1])
#         pixels.append(ascent_transformed[x + 1, y + 1])
#         pixels.sort(reverse=True)
#         newImage[int(x / 2), int(y / 2)] = pixels[0]
#
# # Plot the image. Note the size of the axes -- now 256 pixels instead of 512
# plt.gray()
# plt.grid(False)
# plt.imshow(newImage)
# # plt.axis('off')
# plt.show()

#################################################################################
# Build into combining convolution with DNN

# mnist = tf.keras.datasets.fashion_mnist
# (training_images, training_labels), (test_images, test_labels) = mnist.load_data()
# training_images = training_images.reshape(60000, 28, 28, 1)  # Reshape for conv - 4d array
# training_images = training_images / 255.0
# test_images = test_images.reshape(10000, 28, 28, 1)  # Reshape for conv - 4d array
# test_images = test_images / 255.0
# model = tf.keras.models.Sequential([
#     tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),  # Conv Improvement
#     tf.keras.layers.MaxPooling2D(2, 2),  # Conv Improvement
#     tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),  # Conv Improvement
#     tf.keras.layers.MaxPooling2D(2, 2),  # Conv Improvement
#
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(64, activation='relu'),
#     tf.keras.layers.Dense(10, activation='softmax')
# ])
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# model.summary()
# model.fit(training_images, training_labels, epochs=1)
# test_loss, test_accuracy = model.evaluate(test_images, test_labels)
# print('Test loss: {}, Test accuracy: {}'.format(test_loss, test_accuracy * 100))
#
# # For showing the pooling results:
# f, axarr = plt.subplots(3, 4)
# FIRST_IMAGE = 0
# SECOND_IMAGE = 23
# THIRD_IMAGE = 28
# CONVOLUTION_NUMBER = 6
#
# layer_outputs = [layer.output for layer in model.layers]
# activation_model = tf.keras.models.Model(inputs=model.input, outputs=layer_outputs)
# for x in range(0, 4):
#     f1 = activation_model.predict(test_images[FIRST_IMAGE].reshape(1, 28, 28, 1))[x]
#     axarr[0, x].imshow(f1[0, :, :, CONVOLUTION_NUMBER], cmap='inferno')
#     axarr[0, x].grid(False)
#     f2 = activation_model.predict(test_images[SECOND_IMAGE].reshape(1, 28, 28, 1))[x]
#     axarr[1, x].imshow(f2[0, :, :, CONVOLUTION_NUMBER], cmap='inferno')
#     axarr[1, x].grid(False)
#     f3 = activation_model.predict(test_images[THIRD_IMAGE].reshape(1, 28, 28, 1))[x]
#     axarr[2, x].imshow(f3[0, :, :, CONVOLUTION_NUMBER], cmap='inferno')
#     axarr[2, x].grid(False)
# plt.show()
