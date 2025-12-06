# ✋🎵 Hand Gesture Controlled Music Player  
A fun beginner-friendly Machine Learning + Computer Vision project built using **Python, OpenCV, and MediaPipe**.  
This project allows you to **play, pause, and change music tracks using just hand gestures** — no buttons, no UI, just gestures in front of your webcam.

---

## 🚀 Why I Built This
I recently started exploring **Machine Learning**, and while experimenting with real-time computer vision tools like **OpenCV** and **MediaPipe**, I wanted to build something hands-on and interactive.

This project is simple, but building it while learning concepts like landmark detection, gesture logic, and real-time processing was genuinely fun and insightful.

---

## ✨ Features

### 🎵 Music Control with Hand Gestures  
- **Open Palm (4 fingers open)** → Play / Resume music  
- **Fist (0 fingers open)** → Pause music  
- **Swipe Right** → Next song  
- **Swipe Left** → Previous song  

### 🔧 Real-time Hand Tracking
- Powered by **MediaPipe Hands ML model**  
- Tracks **21 hand landmarks** with high accuracy  
- Detects finger states & movement direction

### 🖥 Real-time Overlay  
- Displays finger count  
- Displays detected gesture  
- Shows swipe direction  

---

## 🛠 Tech Stack

| Component | Usage |
|----------|-------|
| **Python 3.10** | Core programming |
| **OpenCV** | Webcam access, frame processing, display |
| **MediaPipe** | ML model for hand landmark detection |
| **Pygame** | Music playback control |
| **Numpy** | Used internally by OpenCV |

---

## 🧠 How It Works

### 1️⃣ MediaPipe Hand Detection  
MediaPipe provides 21 landmark points for each hand.  
Example:  
- `landmark[8]` → Index fingertip  
- `landmark[0]` → Wrist  

### 2️⃣ Finger Counting  
A finger is considered “open” if its **tip landmark is above its lower joint landmark**.

Example logic:  
```python
if lm[8].y < lm[6].y:
    finger_open = True
