import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
from processImg import process_image 

(train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()
train_images = train_images / 255.0
test_images = test_images / 255.0

# Build the model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=6)
model.evaluate(test_images, test_labels)

# Test the model
test_img = test_images[0]
test_img = np.expand_dims(test_img, axis=1)
plt.imshow(test_img[0], cmap='gray')
plt.show()

predictions = model.predict(test_img)
print("Predictions: ", predictions)
print("Predicted digit: ", np.argmax(predictions[0]))

#model.save("meu_modelo.h5")