import os
import cv2
import numpy as np

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# class_labels = ['A', 'B', 'C']  # Names for classes

number_of_classes = 5
dataset_size = 100

cap = cv2.VideoCapture(0)
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Please put your hand in box and press "s"', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 3,
                    cv2.LINE_AA)
        # Calculate the center of the frame
        frame_height, frame_width = frame.shape[:2]
        center_x = frame_width // 2
        center_y = frame_height // 2

        # Calculate the box dimensions
        box_size = 350  # Adjust this size as needed
        box_half_size = box_size // 2
        box_left = center_x - box_half_size
        box_top = center_y - box_half_size
        box_right = center_x + box_half_size
        box_bottom = center_y + box_half_size

        # Draw the box on the frame
        cv2.rectangle(frame, (box_left, box_top), (box_right, box_bottom), (0, 255, 0), 2)

        # Display the frame
        cv2.imshow('frame', frame)

        if cv2.waitKey(25) == ord('s'):
            break
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()   #function cap.read() returns two values "ret"(a boolean indicating if the frame was read successfully), frame(captured frame itself)
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()
