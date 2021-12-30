import cv2
import numpy as np
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

global text
text = str("")

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
        min_detection_confidence=0.8,
        min_tracking_confidence=0.8) as hands:
    while True:
        _, frame = cap.read()

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)
        image.flags.writeable = False
        imageHeight, imageWidth, _ = image.shape
        results = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS, mp_drawing.DrawingSpec(
                        color=(0, 0, 255)),
                    mp_drawing.DrawingSpec(color=(255, 255, 255)))

            # angka 1
            # atas
            normalizedLandmark = hand_landmarks.landmark[8]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(
                normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight,
            )
            index_finger_tip_y = pixelCoordinatesLandmark[1]
            # bawah
            normalizedLandmark = hand_landmarks.landmark[6]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(
                normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
            index_finger_pip_y = pixelCoordinatesLandmark[1]

            # angka 2
            # atas
            normalizedLandmark = hand_landmarks.landmark[12]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(
                normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
            middle_finger_tip_y = pixelCoordinatesLandmark[1]
            # bawah
            normalizedLandmark = hand_landmarks.landmark[10]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(
                normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
            middle_finger_pip_y = pixelCoordinatesLandmark[1]

            # angka 3
            normalizedLandmark = hand_landmarks.landmark[16]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(
                normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
            ring_finger_tip_y = pixelCoordinatesLandmark[1]
            # bawah
            normalizedLandmark = hand_landmarks.landmark[14]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(
                normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
            ring_finger_pip_y = pixelCoordinatesLandmark[1]

            # angka 4
            normalizedLandmark = hand_landmarks.landmark[20]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(
                normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
            pinky_finger_tip_y = pixelCoordinatesLandmark[1]
            # bawah
            normalizedLandmark = hand_landmarks.landmark[18]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(
                normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
            pinky_finger_pip_y = pixelCoordinatesLandmark[1]
            # tambahan
            normalizedLandmark = hand_landmarks.landmark[17]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(
                normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
            pinky_mcp_y = pixelCoordinatesLandmark[1]

            # angka 5
            normalizedLandmark = hand_landmarks.landmark[4]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(
                normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
            thumb_tip_y = pixelCoordinatesLandmark[1]
            # bawah
            normalizedLandmark = hand_landmarks.landmark[3]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(
                normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
            thumb_pip_y = pixelCoordinatesLandmark[1]

            # untuk angka 1
            if index_finger_pip_y < middle_finger_tip_y and index_finger_pip_y < ring_finger_tip_y and index_finger_pip_y < pinky_finger_tip_y:
                if index_finger_tip_y < middle_finger_pip_y and index_finger_tip_y < ring_finger_pip_y and index_finger_tip_y < pinky_finger_tip_y:
                    number = int(1)
                    print(number)
                    text = str("satu")

            # untuk angka 2
            if middle_finger_tip_y < ring_finger_pip_y and middle_finger_tip_y < ring_finger_pip_y:
                if middle_finger_pip_y < ring_finger_tip_y and middle_finger_pip_y < pinky_finger_tip_y:
                    if index_finger_tip_y < middle_finger_pip_y and middle_finger_tip_y < index_finger_pip_y:
                        number = int(2)
                        print(number)
                        text = str("dua")

            # untuk angka 3
            if ring_finger_pip_y < pinky_finger_tip_y and ring_finger_tip_y < pinky_finger_pip_y:
                if  index_finger_tip_y < ring_finger_pip_y and middle_finger_tip_y < ring_finger_pip_y:
                    if ring_finger_tip_y < index_finger_pip_y and ring_finger_tip_y < middle_finger_pip_y:
                        number = int(3)
                        print(number)
                        text = str("tiga")

            # untuk angka 4
            if index_finger_tip_y < pinky_finger_pip_y and middle_finger_tip_y < pinky_finger_pip_y and ring_finger_tip_y < pinky_finger_pip_y:
                if pinky_finger_tip_y < index_finger_pip_y and pinky_finger_tip_y < middle_finger_pip_y and pinky_finger_tip_y < ring_finger_pip_y:
                    if  pinky_mcp_y < thumb_tip_y:
                        number = int(4)
                        print(number)
                        text = str("empat")

            # untuk angka 5
            if index_finger_tip_y < middle_finger_pip_y and index_finger_tip_y < ring_finger_pip_y and index_finger_tip_y < pinky_finger_pip_y and index_finger_tip_y < thumb_pip_y:
                if thumb_tip_y  < pinky_mcp_y:
                    number = int(5)
                    print(number)
                    text = str("lima")

        cv2.putText(image, text, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (255, 0, 0), 2, cv2.LINE_AA)
        
        cv2.imshow('Hand Tracking', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
