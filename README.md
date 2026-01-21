# 🖐️ Hand Gesture Mouse Controller

A computer vision project that uses **MediaPipe** and **OpenCV** to track hand movements in real-time and control the mouse cursor using **hand gestures**.

---

## 🚀 Overview

This project allows you to control your computer cursor **without touching the mouse** — just by moving your hand in front of the camera.  
It uses the **MediaPipe Hands** model to detect hand landmarks and **PyAutoGUI** to move the system mouse pointer based on the position of your fingers.

---

## 🎯 Features

- ✅ Real-time **hand tracking** using a webcam  
- 🖱️ **Mouse control** with index finger movement  
- ✋ **Pinch gesture detection** to move the cursor  
- ⚙️ Easily extendable to add more gestures (clicks, scrolling, etc.)  
- 💻 Runs locally with Python and webcam  

---

## 🧰 Technologies Used

- **Python**
- **OpenCV**
- **MediaPipe**
- **PyAutoGUI**
- **Math library**

---

## ⚙️ How It Works

1. The webcam captures your hand in real-time.  
2. **MediaPipe** detects 21 key points (landmarks) on the hand.  
3. The script calculates distances between fingertips (thumb–index, thumb–middle).  
4. When a **pinch gesture** is detected (thumb touching index finger), the mouse cursor moves to the same relative position on the screen.  

You can easily modify thresholds to detect other gestures such as:
- Right click (thumb–middle finger pinch)
- Scroll (vertical hand movement)
- Zoom (distance between fingers)

---

## 🧪 Installation

### 1️⃣ Clone the repository
```bash
-----
Install dependencies :
pip install opencv-python mediapipe pyautogui
Run the program
python detecthand-py
press q t exit

git clone https://github.com/mohamedaminehmm/hand-detection-with-mouse-control.git
cd hand-gesture-mouse
