import cv2
import mediapipe as mp
from ultralytics import YOLO

def count_fingers(hand_landmarks):
    fingers = [0, 0, 0, 0, 0]  # Thumb, Index, Middle, Ring, Little
    
    # Thumb (Special case, since it moves differently)
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers[0] = 1  # Thumb (M)
    
    # Other four fingers
    for i, tip in enumerate([8, 12, 16, 20]):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers[i + 1] = 1
    
    return fingers

def detect_hand_gesture(fingers, hand_landmarks):
    # Check if index finger touches thumb
    thumb_tip = hand_landmarks.landmark[4]
    index_tip = hand_landmarks.landmark[8]
    if abs(thumb_tip.x - index_tip.x) < 0.03 and abs(thumb_tip.y - index_tip.y) < 0.03:
        return "sehat selalu"
    
    if fingers == [1, 1, 1, 1, 1]:
        return "Haloo"
    elif fingers == [1, 1, 0, 0, 0]:
        return "HAIII"
    elif fingers == [0, 1, 0, 0, 0]:
        return "Nama aku adalah Gamma"
    elif fingers == [0, 1, 1, 0, 0]:
        return ""
    elif fingers == [0, 0, 0, 1, 0]:
        return "Nama kamu siapa?"
    elif fingers == [0, 0, 0, 0, 1]:
        return "salam kenal"
    elif fingers == [0, 0, 0, 0, 0]:
        return ""
    return ""

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

# Load YOLOv8 model
yolo_model = YOLO("yolov8n.pt")

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Detect objects using YOLOv8
        results = yolo_model(frame)
        
        # Process YOLO results
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                label = result.names[int(box.cls[0])]
                
                # Draw YOLO bounding box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        
        # Detect hand landmarks
        results_hands = hands.process(rgb_frame)
        if results_hands.multi_hand_landmarks:
            for hand_landmarks in results_hands.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                fingers = count_fingers(hand_landmarks)
                gesture_text = detect_hand_gesture(fingers, hand_landmarks)
                
                cv2.putText(frame, gesture_text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imshow('Hand Gesture Recognition', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

