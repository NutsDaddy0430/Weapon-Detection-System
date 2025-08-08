# 🔫 Weapon Detection System (Real-Time)

This project uses OpenCV and a Haar Cascade classifier to detect weapons (e.g., guns) from a webcam feed in real time. Detected events are logged into a CSV file with timestamps for recordkeeping.

---

## 📸 Features

- Real-time video capture from webcam
- Gun detection using a Haar Cascade XML file
- Visual bounding boxes around detected objects
- Automatic logging of detections with timestamps to `log.csv`
- Simple and lightweight (no deep learning required)

---

## 📁 Project Structure

weapon-detection-system/
├── main.py # Main detection script
├── cascade.xml # Haar Cascade classifier for weapons
├── log.csv # Output log file with timestamps
├── requirements.txt # Python dependencies
└── README.md # Project info


---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/weapon-detection-system.git
cd weapon-detection-system
```
### 2. Install Dependencies

Use a virtual environment (recommended) and install:
```bash
pip install -r requirements.txt
```
### 3. Run the Script
```bash
python main.py
```
Press q to quit the camera feed.
