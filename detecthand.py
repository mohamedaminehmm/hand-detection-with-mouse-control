import cv2 as cv
import mediapipe as mp
import math as m
import pyautogui

mp_drawing = mp.solutions.drawing_utils
mp_hands   = mp.solutions.hands
screen_width, screen_height = pyautogui.size()
cap = cv.VideoCapture(0)

with mp_hands.Hands(
    static_image_mode=False,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.5
) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("This frame couldn't be read, skipping…")
            continue

        img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        img.flags.writeable = False
        x, y, z = img.shape
        text = "Hello"
        font = cv.FONT_HERSHEY_SIMPLEX
        font_scale = 1.5
        thickness = 3

# --- compute text width and height
        (text_width, text_height), _ = cv.getTextSize(text, font, font_scale, thickness)

# --- calculate centered x position
        center_x = (img.shape[1] - text_width) // 2
        y = 40   # distance from top (you can change it)
        def hi():
            cv.putText(img, text, (center_x, y), font, font_scale, (0, 255, 0), thickness)

        res = hands.process(img)

        img.flags.writeable = True
        img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

        if res.multi_hand_landmarks:
            for num, hand in enumerate(res.multi_hand_landmarks):
                mp_drawing.draw_landmarks(
                    img,
                    hand,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(250, 0, 0), thickness=2, circle_radius=4),
                    mp_drawing.DrawingSpec(color=(0, 0, 250), thickness=2, circle_radius=2)
                )
            
            for hand_landmarks in res.multi_hand_landmarks:
                index_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
                index_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                thumb_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
                thumb_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
                mid_x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x
                mid_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                # --- Compute hand size as reference ---
                wrist_x = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
                wrist_y = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
                middle_mcp_x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x
                middle_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y

                hand_size = ((middle_mcp_x - wrist_x) ** 2 + (middle_mcp_y - wrist_y) ** 2) ** 0.5

                # --- Compute normalized distance ---
                xx = (index_x - thumb_x) ** 2
                yy = (index_y - thumb_y) ** 2
                distance = (xx + yy) ** 0.5
                #print("hhhhhhhhhhhhhhhhhhhhhhhhh")
                xx1 = (mid_x - thumb_x) ** 2
                yy1 = (mid_y - thumb_y) ** 2
                distance1 = (xx1 + yy1) ** 0.5
                #print(xx,yy)
                normalized_distance = distance / hand_size  # normalized
                normalized_distance1 = distance1 / hand_size
                # --- Pinch detection using normalized distance ---
                radius = 0.19 # adjust this threshold as needed
                if normalized_distance <= radius:
                    #print("Pinch detected")
                    screen_x = int(index_x * screen_width)
                    screen_y = int(index_y * screen_height)
                    screen_y = screen_height - screen_y
                    #print(screen_x,screen_y)
                    #print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
                    pyautogui.moveTo(screen_x, screen_y)

                #else:
                    #print("no pinch")
                # to make midxthymb as right click 
                #if normalized_distance1 <= radius:
                 #   screen_x1 = int(mid_x * screen_width)
                  #  screen_y1 = int(mid_y * screen_height)
                   # screen_y1 = screen_height - screen_y1
                    #pyautogui.click(button='right')
                

                

        
      
        cv.imshow("Web Window", img )

        if cv.waitKey(1) == ord('q'):
            break

cap.release()
cv.destroyAllWindows()
