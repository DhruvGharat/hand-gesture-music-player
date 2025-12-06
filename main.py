import cv2
import mediapipe as mp
from gesture_controller import GestureController
from music_player import MusicPlayer

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
gc = GestureController()
player = MusicPlayer()

player.play()   # start playing music automatically

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            lm = handLms.landmark

            # ==== FINGER COUNT ====
            finger_count = gc.count_fingers(lm)

            # ==== SWIPE DETECTION ====
            wrist_x = lm[0].x
            swipe = gc.detect_swipe(wrist_x)

            # ==== GESTURE → MUSIC MAPPING ====

            # Play music → open palm (4 fingers)
            if finger_count == 4:
                player.unpause()
                cv2.putText(frame, "Play", (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            # Pause music → fist (0 fingers)
            elif finger_count == 0:
                player.pause()
                cv2.putText(frame, "Pause", (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

            # Next/Prev song by swipe
            if swipe == "RIGHT":
                player.next()
                cv2.putText(frame, "Next Song", (20, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

            elif swipe == "LEFT":
                player.prev()
                cv2.putText(frame, "Prev Song", (20, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

            # Display finger count
            cv2.putText(frame, f"Fingers: {finger_count}", (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            # Display swipe
            if swipe:
                cv2.putText(frame, f"Swipe: {swipe}", (20, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    cv2.imshow("Gesture Music Controller", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
