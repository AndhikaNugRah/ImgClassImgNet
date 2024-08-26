# Import necessary libraries
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np

def classify_image(img_path):
    # Load the MobileNetV2 model with the top classification layer
    model = MobileNetV2(weights='imagenet', include_top=True, input_shape=(224, 224, 3))

    # Load the image to classify
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocess the image
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # Classify the image and get the result
    preds = model.predict(x)
    results = decode_predictions(preds, top=1)

    # Filter electronic devices only
    if results:
        for result in results[0]:
            label=result[1]
            confidence=result[2]
            print(f"{label} with {confidence * 100:.2f}% confidence")

def main():
    while True:
        img_path = input("Please input the path of the image: (without quotes) ")
        classify_image(img_path)

        response = input("Do you want to continue classifying? (yes/no): ")
        if response.lower() == "no":
            print("Thanks for using our service! -Dhika")
            break
        elif response.lower() == "yes":
            print("Please input the new path of the image:")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()