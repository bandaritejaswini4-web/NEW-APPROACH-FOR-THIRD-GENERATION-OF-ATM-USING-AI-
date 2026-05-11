# AI-Based ATM Security System using Facial Recognition

## 📌 Project Overview
This project is a Flask-based AI ATM Security System that uses Facial Recognition for secure authentication. Instead of relying only on ATM cards and PINs, the system verifies users using their facial features, reducing risks such as card theft, PIN hacking, skimming attacks, and unauthorized access.

The system captures live video through a webcam, detects faces in real time, and compares them with registered users stored in the database.

---

## 🚀 Features

- Real-time face detection and recognition
- User registration with image database
- Secure authentication using AI
- Access granted/denied display
- Live webcam streaming using Flask
- Easy-to-use web interface
- Cardless ATM authentication concept

---

## 🛠️ Technologies Used

- Python
- Flask
- OpenCV
- face_recognition
- HTML/CSS
- Machine Learning
- Computer Vision

---

## 📂 Project Structure

```bash
project/
│
├── app.py
├── database/
│   ├── user1.png
│   ├── user2.png
│
├── templates/
│   ├── home.html
│   ├── about.html
│   ├── process.html
│   ├── create_database.html
│   ├── detection.html
│
└── static/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-atm-security-system.git
cd ai-atm-security-system
```

### 2. Install Dependencies

```bash
pip install flask opencv-python face_recognition numpy
```

### 3. Run the Application

```bash
python app.py
```

### 4. Open Browser

```bash
http://127.0.0.1:5000
```

---

## 📸 How It Works

### Step 1: Register User
- Upload user image
- Store facial data in database

### Step 2: Start Detection
- Webcam starts capturing live video
- Face is detected and encoded

### Step 3: Authentication
- Face is compared with stored encodings
- If matched → Access Granted
- Else → Access Denied

---

## 🧠 Working Process

1. Load registered user images
2. Extract facial encodings
3. Capture live webcam feed
4. Detect faces in real time
5. Compare detected face with database
6. Display authentication result

---

## 🔐 Security Advantages

- Eliminates dependency on ATM cards
- Reduces fraud and unauthorized access
- Enhances banking security
- Faster and user-friendly authentication

---

## 📈 Future Enhancements

- OTP verification
- Fingerprint authentication
- Cloud database integration
- Real-time alert system
- Deep learning optimization
- Multi-user tracking

---

## 📖 Reference

This project is inspired by the concept of “New Approach for Third Generation of ATM Using Artificial Intelligence” which focuses on improving ATM security using facial recognition and image processing techniques.

---

## 👨‍💻 Author

Developed as a Machine Learning & Computer Vision project using Flask and Facial Recognition.
