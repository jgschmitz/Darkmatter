# Basic tensorflow demo -> in mongod -> Origami 

import tensorflow as tf
from tensorflow.keras import layers
import sklearn as SK

# Define the CNN model

model = tf.keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(image_width, image_height, num_channels)),
    layers.MaxPooling2D(2),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train and evaluate the model
model.fit(train_images, train_labels, epochs=10, batch_size=32)
test_loss, test_acc = model.evaluate(test_images, test_labels)

print(f'Test accuracy: {test_acc:.4f}')
