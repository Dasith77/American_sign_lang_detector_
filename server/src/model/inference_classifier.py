import mediapipe as mp
import pickle
import cv2
import numpy as np
import time

model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
labels_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
previous_char = "initial"
threshold = 3.0
count = True
time_before = time.time()
predicted_text = ""  # Initialize the predicted text as an empty string

while True:
    data_aux = []
    ret, frame = cap.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    predicted_character = "initial"  # when no hand is recognized, it shows 'initial'

    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x)
                data_aux.append(y)

        prediction = model.predict([np.asarray(data_aux)])
        predicted_character = labels_dict[int(prediction[0])]

    if predicted_character == "initial":
        previous_char = "initial"

    if previous_char == "initial":
        if predicted_character != "initial":
            
            time_now = time.time()
            time_idle = time_now - time_before
            if time_idle > threshold:
                print("  ", end='') # Add a space to the predicted text
            print(predicted_character, end='')  # Add the character to the predicted text
            time_before = time.time()
        previous_char = predicted_character
        count = False

    cv2.imshow('frame', frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

#print("Predicted Text:", predicted_text)  # Print the final predicted text
cap.release()
cv2.destroyAllWindows()
