import os
import mediapipe as mp
import cv2
import pickle  # use to save datasets models and info

import matplotlib.pyplot as plt
from mediapipe.python.solutions import hands

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

DATA_DIR = './data'

data = []
class_lables = []

for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        data_aux = []
        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))   #It takes the file path as an argument and returns a NumPy array representing the image.
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    # in here print all coordinate of landmarks of an image
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x)
                    data_aux.append(y)

            data.append(data_aux)  # this big array represents our image
            class_lables.append(dir_)

# create file to save all this data
with open('data.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': class_lables}, f)
