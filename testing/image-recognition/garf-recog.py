import tensorflow as tf
import numpy as np

from keras_preprocessing import image
from keras_preprocessing.image import ImageDataGenerator

garf_training_path = "../../datasets/experimental/training"
garf_testing_path = "../../datasets/experimental/testing"

training_datagen = ImageDataGenerator(
    rescale=1 / 255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest"
)

testing_datagen = ImageDataGenerator(
    rescale=1 / 255
)

training_generator = training_datagen.flow_from_directory(
    garf_training_path,
    target_size=(200, 200),
    class_mode="categorical",
    batch_size=5
)

testing_generator = testing_datagen.flow_from_directory(
    garf_testing_path,
    target_size=(200, 200),
    class_mode="categorical",
    batch_size=1
)

model = tf.keras.models.Sequential(
    [
        # Note the input shape is the desired size of the image 150x150 with 3 bytes color
        # This is the first convolution
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(200, 200, 3)),
        tf.keras.layers.MaxPooling2D(2, 2),
        # The second convolution
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        # The third convolution
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        # The fourth convolution
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        # Flatten the results to feed into a DNN
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dropout(0.5),
        # 512 neuron hidden layer
        tf.keras.layers.Dense(1024, activation='relu'),
        tf.keras.layers.Dense(2, activation='softmax')
    ]
)

model.summary()
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

# history = model.fit(training_generator, epochs=100, steps_per_epoch=5, validation_data=testing_generator, verbose=1,
#                     validation_steps=5)
#
# model.save("garf.h5")
#
# acc = history.history['accuracy']
# val_acc = history.history['val_accuracy']
# loss = history.history['loss']
# val_loss = history.history['val_loss']

model.load_weights("garf.h5")
print(training_generator.class_indices)

predict_img = image.load_img("../../datasets/experimental/testing/not garfield/images (21).jpeg",
                             target_size=(200, 200))
x = image.img_to_array(predict_img) / 255
x = np.expand_dims(x, axis=0)
images = np.vstack([x])
print(model.predict(images, batch_size=1))
