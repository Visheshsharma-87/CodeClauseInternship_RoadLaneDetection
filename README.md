🚗 Road Lane Detection by Processing Video
🔬 Internship Project (Golden Level)
🧠 Domain: Artificial Intelligence | 🏢 Company: CodeClause

📌 Project Overview
This intelligent system automatically detects and highlights road lanes in a video stream using Python, OpenCV, and Computer Vision techniques. It is designed to assist in autonomous vehicle navigation or driver safety systems by identifying lane boundaries in real time.

🎯 Objectives
📹 Process road videos frame-by-frame.

🧠 Detect actual road lane markings.

📏 Filter false lines (barriers, poles).

🖥️ Display real-time GUI-based detection.

📁 Save output video with overlays.

📊 Log detections to optional SQLite database.

⚙️ Features
✅ Real-time video processing with OpenCV
✅ Advanced lane detection using Hough Transform & slope filtering
✅ Noise reduction via Gaussian blur and ROI masking
✅ GUI interface for easy video selection & control
✅ Optional SQLite database logging (lane_logs.db)
✅ FPS counter and overlay status display
✅ Audio alerts when no lanes are detected
✅ All detections rendered and saved as result_output.avi
✅ Thumbnail and clean folder structure for GitHub/LinkedIn demo

🖥️ Technologies Used
Python 3.x

OpenCV

NumPy

Tkinter (GUI)

SQLite3 (Optional DB logging)

📂 Folder Structure
RoadLaneDetection/
├── main.py                       # GUI + Integration
├── lane_detector.py             # Lane detection logic
├── video_processor.py           # Frame handling, overlay, audio
├── db_logger.py                 # Optional: SQLite logging
├── requirements.txt             # Dependencies
├── README.md                    # Project overview
├── input/
│   └── road_sample.mp4          # Sample road video
├── output/
│   └── result_output.avi        # Final processed video
├── database/
│   └── lane_logs.db             # SQLite DB (auto-created)
├── assets/
│   └── thumbnail.png            # For LinkedIn/GitHub
└── utils/
    └── fps_counter.py           # Real-time FPS tracking
🚀 How to Run
1. 🔃 Clone the repo:
git clone https://github.com/Visheshsharma-87/CodeClauseInternship_RoadLaneDetection.git
2. 📦 Install dependencies:
pip install -r requirements.txt
3. ▶️ Launch GUI:
python main.py
🎥 Select a road video → Click on Start Lane Detection.

4. 📽️ Output Demo
Detected lanes will be drawn in green lines.

Status: ✅ Lanes Detected / ❌ No Lane Found

Audio alert plays when no lanes are found.

Output video saved in /output/result_output.avi.
🏅 Internship Criteria Check ✅
 Golden Level Project

 Real-time Working GUI

 Not Console-based

 Dynamic Functionality

 SQLite logging + FPS Counter

 Original & High Quality

👨‍💻 Developed by
Vishesh Sharma
B.Tech CSE (Data Science), Galgotias University
