# American_sign_lang_detector_
![ACTUAL DESIGN - This is what we publish!](https://github.com/Dasith77/American_sign_lang_detector_/assets/65776391/6097b390-bb16-459e-a791-184a10cea026)


# Overall Project description

This is semester 5 embedded system engineering project based on machine learning and computer vision to detedct hand sign languages and convert it  to a audible sounds.

The American Sign Language Interpreter is a powerful application designed to bridge communication gaps between hearing-impaired individuals and the broader community. Leveraging the capabilities of the MediaPipe framework, this interpreter utilizes landmark detection technology to accurately recognize and translate American Sign Language gestures into textual or auditory output. Unlike traditional pixel recognition methods, which often struggle with varying lighting conditions and complex hand movements, the MediaPipe-based approach excels in robustly identifying key landmarks on hands, making it more reliable and adaptable. This enables the interpreter to provide more accurate and real-time translations, enhancing accessibility and fostering effective communication between the deaf and hearing communities. Whether in educational settings, public spaces, or everyday interactions, the American Sign Language Interpreter powered by MediaPipe serves as an essential tool for promoting inclusivity and understanding.

# I implement this project as 2 stages.

    1. Impelemt machine learning part to recognizes and build a sentence using those characters.
    2. Further implementation into a web based application.
    


**1 . First stage(convert finger spelling into the readable english language text)**

**description**

Fingerspelling is a way of encoding written language using handshapes and movements of the fingers. It can be used to spell out names, words, and phrases that do not have a sign equivalent.

To convert fingerspelling into readable English text, we can use computer vision  models.Using computer vision libraries like openCV get frames from live video and crop the image of the hand . These models can identify the handshapes and movements of the fingers, and then generate a sequence of characters that represent the fingerspelled word. This sequence of characters can then be converted into readable English text.

This process is challenging, but it is becoming increasingly feasible with the development of new computer vision models.


**--In this 1st stage I  use this flow--**

    How to load the data
    
    Convert the data to tfrecords to make it faster to re-train the model
    
    Train a transformer models on the data
    
    Convert the model to TFLite


**--Prerequisites for this first stage--**

    Python 3.8+
    
    TensorFlow 2.8+
    
    NumPy
    
    Pandas

    OpenCV
    
    Matplotlib



# Using land mark detection

This project will done by using landmark detection method.

# 1 STEP - Collecting data set for training

In here I used my own example dataset for prototype. I create as each alphabet letter as a class and in each class include 100 images(frames).








Converting the data to tfrecords

Training the model

Converting the model to TFLite

