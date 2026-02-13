# 🎵 YouTube Mashup Generator (CLI + Web Service)

---

## 📌 Project Overview

This project implements a **YouTube Audio Mashup Generator** in two parts:

1. **Program 1** – Command Line Python Application  
2. **Program 2** – Web-Based Mashup Service using Flask  

The system downloads songs from YouTube, trims them to a specified duration, merges them into a single mashup file, and optionally sends the result via email.

---

# 🔹 Program 1 – Command Line Mashup

## 📁 File
102303831.py

---

## ▶️ Description

This program:

- Accepts command-line arguments
- Downloads top N songs of a given singer from YouTube
- Converts them into MP3 format
- Trims first Y seconds (Y > 20)
- Merges all trimmed audios
- Generates final mashup file

---

## ▶️ Command Format

python 102303831.py "<SingerName>" <NumberOfVideos> <AudioDuration> <OutputFileName>

---

## ▶️ Example Execution

python 102303831.py "Sharry Mann" 3 30 final.mp3

---

## ✅ Features Implemented

- ✔ Validates correct number of parameters
- ✔ Ensures duration > 20 seconds
- ✔ Handles invalid inputs
- ✔ Exception handling implemented
- ✔ Uses PyPI libraries (yt-dlp, pydub)
- ✔ Merges multiple audio files into one output file

---

## 🖥 Command Prompt Output

(Screenshot added below showing successful execution)
<img width="1465" height="500" alt="image" src="https://github.com/user-attachments/assets/ec98e5bb-a44f-4d99-af04-8b50bdcab60e" />


---

# 🔹 Program 2 – Web Mashup Service

## 📁 File
app.py

---

## 🌐 Description

This is a Flask-based web application that:

- Accepts:
  - Singer Name
  - Number of Videos
  - Duration (seconds)
  - Email ID
- Internally calls Program 1
- Generates mashup file
- Creates ZIP archive
- Sends ZIP file to provided email

---

## ▶️ How To Run Locally

Install dependencies:
pip install -r requirements.txt
Run application:
python app.py
Open in browser:
http://127.0.0.1:5000
<img width="1098" height="657" alt="image" src="https://github.com/user-attachments/assets/d5e8507c-f6f4-42d2-85fe-9bb8f6b1a8de" />

---

## 📧 Email Feature

- Uses Gmail SMTP
- Requires Google App Password
- Sends mashup in ZIP format to user

---



# ⚙ Technologies Used

- Python
- Flask
- yt-dlp
- pydub
- ffmpeg
- smtplib
- zipfile

---



# ⚠ Important Notes

- FFmpeg must be installed and added to system PATH.
- Duration must be greater than 20 seconds.
- Gmail App Password is required for email functionality.
- Works for any valid singer name available on YouTube.

---

# 👩‍💻 Author

Roll Number: 102303831  
Course: Computer Engineering  
Assignment: Mashup Generator (Program 1 & Program 2)

---
