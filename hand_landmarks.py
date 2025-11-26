import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
alpha = 0.6
smoothed_color = np.array([0.0,0.0,0.0])


while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    color = np.array([0,0,0], dtype=np.float32)


    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]
        lm = hand_landmarks.landmark
        def px(i):
            return int(lm[i].x * w), int(lm[i].y * h)
        
        t4 = px(4)
        t8 = px(8)
        t12 = px(12)
        t16 = px(16)
        def dist(a, b):
            return np.hypot(a[0] - b[0], a[1] - b[1])
        d_r = dist(t4, t8)
        d_g = dist(t8, t12)
        d_b = dist(t12, t16)

        diag = np.hypot(w, h)
        color[0] = np.clip((d_r / diag) * 3 * 255, 0, 255)
        color[1] = np.clip((d_g / diag) * 3 * 255, 0, 255)
        color[2] = np.clip((d_b / diag) * 3 * 255, 0, 255)
        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        cv2.circle(frame, t4, 6, (0, 0, 255), -1)
        cv2.circle(frame, t8, 6, (0, 255, 0), -1)
        cv2.circle(frame, t12, 6, (255, 0, 0), -1)
        cv2.circle(frame, t16, 6, (255, 255, 0), -1)
        
    smoothed_color = alpha * smoothed_color + (1 - alpha) * color
    swatch = smoothed_color.astype(np.uint8).tolist()
    swatch_bgr = (swatch[2], swatch[1], swatch[0])
    cv2.rectangle(frame, (10, 10), (140, 110), swatch_bgr, -1)
    text = f"R:{int(smoothed_color[0])} G:{int(smoothed_color[1])} B:{int(smoothed_color[2])}"
    cv2.putText(frame, text, (10, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.imshow("Hand Color Mixer", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()