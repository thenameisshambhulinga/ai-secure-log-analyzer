# 🔐 AI Secure Data Intelligence Platform

## 🚀 Overview
This project is an AI-powered security platform that analyzes log files to detect sensitive data leaks and potential vulnerabilities.

## 🎯 Problem Statement
Log files often contain sensitive information like passwords, API keys, and system errors which can lead to security breaches if exposed.

## 💡 Solution
This platform performs:
- Log parsing and analysis
- Sensitive data detection (passwords, API keys, emails)
- Risk classification
- AI-based insights generation
- Masking of confidential data

## 🧠 Key Features
- 🔍 Log file upload and analysis
- 🔐 Sensitive data masking
- ⚠ Risk scoring and classification
- 💡 AI-generated insights
- 🛡 Security status detection

## 🏗 Architecture
Input → Detection Engine → Log Analyzer → Risk Engine → Insights → Output

## 🛠 Tech Stack
- Frontend: React.js
- Backend: FastAPI (Python)
- Detection: Regex + AI logic

## ⚙ Setup Instructions

### Backend
cd backend  
python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  
python3 -m uvicorn main:app --reload  

### Frontend
cd frontend  
npm install  
npm start  

## 🧪 Sample Input
Use `sample.log` file to test.

## 🎥 Demo
(Attach your video link here)

## 📊 Output
- Findings (email, password, API key, errors)
- Risk score and level
- AI insights

## 🏆 Highlights
- Real-time log security analysis
- AI-driven insights
- Secure data masking

## 👨‍💻 Author
Your Name