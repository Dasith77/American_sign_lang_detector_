# American_sign_lang_detector_
![ACTUAL DESIGN - This is what we publish!](https://github.com/Dasith77/American_sign_lang_detector_/assets/65776391/6097b390-bb16-459e-a791-184a10cea026)


# Overall Project description

This is semester 5 embedded system engineering project based on machine learning and computer vision to detedct hand sign languages and convert it  to a audible sounds.

In this project I mainly go through two stages. As the first stage, I hope to convert finger spelling into the readable english language text.As the second stage, I hope to develop this system to convert text output as an audio output and create a web interface.

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

