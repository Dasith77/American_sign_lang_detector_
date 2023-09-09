import os
import mediapipe as mp
import cv2
import pickle

import matplotlib.pyplot as plt
from mediapipe.python.solutions import hands

mp_hands = mp.solutions.hands  #provide functionality to hand tracking
mp_drawing = mp.solutions.drawing_utils  #provide utility functions for drawing landmarks in image
mp_drawing_styles = mp.solutions.drawing_styles  #provide predefined solutions for drawnig landmarks

hands = mp_hands.Hands(static_image_mode=False, min_detection_confidence=0.4)  #0.4 is the threshold

DATA_DIR = './data'

for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_))[:1]:
        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #plt.imshow(img_rgb) #show images without landmarks

        results = hands.process(img_rgb)   #
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:  # Corrected typo here
                mp_drawing.draw_landmarks(
                    img_rgb,
                    hand_landmarks,   #by this,is a data structure that contains detected landmarks on hand
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

        plt.figure()
        plt.imshow(img_rgb)

plt.show()
