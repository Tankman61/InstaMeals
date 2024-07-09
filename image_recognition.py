import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import json

# Load model architecture and weights
with open('model.json') as json_file:
    model_json = json_file.read()

model = tf.keras.models.model_from_json(model_json)
model.load_weights('weights.bin')

# Load the labels
with open('metadata.json') as metadata_file:
    metadata = json.load(metadata_file)
labels = metadata['labels']

# Function to preprocess the image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

# Predict function
def predict_top_categories(img_path, top_n=10):
    img_array = preprocess_image(img_path)
    predictions = model.predict(img_array)[0]
    top_indices = predictions.argsort()[-top_n:][::-1]
    top_categories = [(labels[i], predictions[i]) for i in top_indices]
    return top_categories

# Example usage
img_path = 'path_to_your_image.jpg'
top_categories = predict_top_categories(img_path)
print("Top categories:")
for category, score in top_categories:
    print(f"{category}: {score*100:.2f}%")
