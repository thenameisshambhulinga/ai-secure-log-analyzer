# 🔐 AI Secure Data Intelligence Platform

## 🚀 Overview

This project is an AI-powered security tool that analyzes log and document files to identify sensitive data exposure and potential risks. It helps developers and organizations quickly understand whether their system logs contain information that could lead to security issues.

---

## 🎯 Problem

In real-world applications, log files often contain sensitive data such as passwords, API keys, emails, and system errors. If these logs are exposed or not properly handled, they can lead to serious security breaches.

---

## 💡 Solution

This platform takes a file as input (log, text, PDF, etc.), scans it for sensitive information using pattern detection, and then provides a clear report with risk levels and insights. It also masks sensitive data to prevent further exposure.

---

## ⚙️ Features

* Detects sensitive data (emails, passwords, API keys, errors)
* Assigns risk levels (Low, Medium, High, Critical)
* Generates simple AI-based insights
* Masks sensitive values in output
* Supports multiple file types:

  * `.log`, `.txt`, `.sql`
  * `.pdf` (text-based parsing)
  * `.doc/.docx` (extendable)
* Clean and easy-to-use web interface

---

## 🛠️ Tech Stack

**Frontend:** React.js, Axios
**Backend:** FastAPI (Python), Uvicorn
**Libraries:** PyPDF2, Regex

---

## 📂 Project Structure

```
hackathon_sisa/
├── backend/
├── frontend/
└── README.md
```

---

## 🚀 How to Run

### Backend

```
cd backend
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn python-multipart PyPDF2
python3 -m uvicorn main:app --reload
```

### Frontend

```
cd frontend
npm install
npm start
```

---

## 🧪 How It Works

1. Upload a file
2. The backend reads and analyzes its content
3. Sensitive patterns are detected
4. A risk score is calculated
5. Results are shown in a dashboard with insights

---

## 🎥 Demo

Here is a short demo of the project:
https://drive.google.com/file/d/1GH8R05hnxgkx7V_59u10dW--8WPULRyI/view?usp=drivesdk

---

## 🔮 Future Improvements

* Better support for DOC/DOCX files
* OCR support for scanned PDFs
* Real-time log monitoring
* Integration with security tools

---

## 👨‍💻 Author

Shambhulingappa S S

---

## 📌 Final Note

This project focuses on solving a real-world problem in a simple and practical way. It shows how basic AI concepts and pattern detection can be used to improve system security.
