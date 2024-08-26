Image Classification Project using MobileNetV2

This project is an image classification system that uses the MobileNetV2 model to classify images into different categories. 

The system is designed to be user-friendly, allowing users to input the path of an image and receive the classification result.

Key Features

Image Classification: The system uses the MobileNetV2 model to classify images into different categories.

User Input: Users can input the path of an image to be classified.

Real-time Results: The system provides real-time classification results, including the label and confidence level.

Load the Model: The system loads the MobileNetV2 model with the top classification layer.

Load the Image: The system loads the image to be classified and preprocesses it.

Classify the Image: The system uses the MobileNetV2 model to classify the image and get the result.

Display Results: The system displays the classification result, including the label and confidence level.

Code Structure
The code is structured into two main functions:

classify_image: This function takes an image path as input, loads the image, preprocesses it, and classifies it using the MobileNetV2 model.

main: This function is the entry point of the program. It prompts the user to input the path of an image, calls the classify_image function, and displays the results.

Technical Details

Libraries: The project uses the following libraries:
TensorFlow

Keras

NumPy

Model: The project uses the MobileNetV2 model with the top classification layer.

Image Preprocessing: The project uses the preprocess_input function from Keras to preprocess the image.
