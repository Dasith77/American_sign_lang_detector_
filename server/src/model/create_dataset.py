import os # Provides functions for interacting with the operating system, used for navigating directories.
import mediapipe as mp
import cv2
import pickle  # serializing and deserializing Python objects.

import matplotlib.pyplot as plt
from mediapipe.python.solutions import hands

mp_hands = mp.solutions.hands  # provide functionality to hand tracking
mp_drawing = mp.solutions.drawing_utils  # provide utility functions for drawing landmarks in image
mp_drawing_styles = mp.solutions.drawing_styles  # provide predefined solutions for drawnig landmarks

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.6)

DATA_DIR = './data'

data = []  #An empty list to store the landmark data for each image.
class_lables = [] #An empty list to store the class labels (i.e., directory names) 

for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        data_aux = []  # contains the x and y coordinate values of the landmarks detected on one particular hand in a
        # single image.
        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))  # It takes the file path as an argument and
        # returns a NumPy array representing the image.
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

#print(len(data_aux))
#print(len(data))
#max_landmarks = max(len(entry) for entry in data)

# Pad the data with zeros to match the maximum shape
#for entry in data:
    #while len(entry) < max_landmarks:
        #entry.extend([0.0, 0.0])  # Assuming landmarks are represented as (x, y) pairs

# Now, you can safely convert data into a NumPy array
# create file to save all this data
with open('data.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': class_lables}, f)  # serializes this dictionary and writes it to the
    # 'data.pickle' file in binary format. This file will now contain the data and labels in a serialized form.
