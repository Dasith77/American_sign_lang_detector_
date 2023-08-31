# American_sign_lang_detector_
![ACTUAL DESIGN - This is what we publish!](https://github.com/Dasith77/American_sign_lang_detector_/assets/65776391/6097b390-bb16-459e-a791-184a10cea026)


# Overall Project description

This is semester 5 embedded system engineering project based on machine learning and computer vision to detedct hand sign languages and convert it  to a audible sounds.

The American Sign Language Interpreter is a powerful application designed to bridge communication gaps between hearing-impaired individuals and the broader community. Leveraging the capabilities of the MediaPipe framework, this interpreter utilizes landmark detection technology to accurately recognize and translate American Sign Language gestures into textual or auditory output. Unlike traditional pixel recognition methods, which often struggle with varying lighting conditions and complex hand movements, the MediaPipe-based approach excels in robustly identifying key landmarks on hands, making it more reliable and adaptable. This enables the interpreter to provide more accurate and real-time translations, enhancing accessibility and fostering effective communication between the deaf and hearing communities. Whether in educational settings, public spaces, or everyday interactions, the American Sign Language Interpreter powered by MediaPipe serves as an essential tool for promoting inclusivity and understanding.

# I implement this project as 2 stages.

    1. Impelemt machine learning part to recognizes hand signs and build a sentence using those characters.
    2. Further implementation into a web based application.
    


# 1 . First stage

## 1.1 Collecting dataset from webcam

This code is part of a GitHub repository for collecting data from a webcam to create a training dataset for a machine learning model. The script uses the OpenCV library to interact with the webcam and capture frames. It sets up a directory structure in the repository's "./data" directory to store the collected images. The script is designed to work with 10 classes, capturing 200 images for each class. It uses the webcam feed to guide users to press the 'Q' key to start capturing frames for each class. Subsequently, the code captures frames, displays them in a window, and saves them as sequentially numbered image files in their respective class folders. Once the dataset size is reached for each class, the script releases the webcam capture and closes any open windows. This code snippet is an essential part of the repository's data collection process for training machine learning models that require image data.

![image](https://github.com/Dasith77/American_sign_lang_detector_/assets/65776391/66841f39-5b9f-465a-8625-260a7dc5c80e)

references: https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html


## About mediapipe library
MediaPipe is an open-source framework developed by Google that focuses on providing pre-built solutions for various computer vision and machine learning tasks. It simplifies the development process by offering a collection of ready-to-use models and tools, allowing developers to build applications that involve real-time perception and understanding of the world through cameras, images, and videos.The relationship between MediaPipe and TensorFlow is that MediaPipe is built on top of TensorFlow. It utilizes TensorFlow's underlying capabilities for training and inference of models. MediaPipe takes advantage of TensorFlow's deep learning capabilities while providing a higher-level interface for specific computer vision tasks.


