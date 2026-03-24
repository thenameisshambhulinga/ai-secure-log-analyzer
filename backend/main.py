from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import re

app = FastAPI()

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Patterns
patterns = {
    "email": r"[\w\.-]+@[\w\.-]+",
    "api_key": r"sk-[a-zA-Z0-9]+",
    "password": r"password\s*=\s*\w+",
    "error": r"error|exception|trace",
}

# Risk levels
risk_map = {
    "email": "low",
    "api_key": "high",
    "password": "critical",
    "error": "medium"
}

score_map = {
    "low": 1,
    "medium": 3,
    "high": 5,
    "critical": 10
}

# 🔐 Mask sensitive data
def mask_sensitive(line):
    line = re.sub(r"password=\w+", "password=****", line)
    line = re.sub(r"sk-[a-zA-Z0-9]+", "sk-****", line)
    return line

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    content = (await file.read()).decode(errors="ignore")
    lines = content.split("\n")

    findings = []
    score = 0

    for i, line in enumerate(lines):
        for key, pattern in patterns.items():
            if re.search(pattern, line, re.IGNORECASE):
                risk = risk_map[key]

                masked_line = mask_sensitive(line)

                findings.append({
                    "type": key,
                    "line": i + 1,
                    "content": masked_line,
                    "risk": risk
                })

                score += score_map[risk]

    # Risk engine
    if score >= 20:
        level = "critical"
    elif score >= 10:
        level = "high"
    elif score >= 5:
        level = "medium"
    else:
        level = "low"

    # 🤖 AI insights
    insights = []

    if any(f["type"] == "password" for f in findings):
        insights.append("Sensitive passwords exposed in logs")

    if any(f["type"] == "api_key" for f in findings):
        insights.append("API keys detected - potential security risk")

    if any(f["type"] == "error" for f in findings):
        insights.append("System errors detected - possible vulnerability")

    if score > 15:
        insights.append("High security risk detected. Immediate action recommended.")

    summary = f"AI Analysis Report: {len(findings)} issues detected with risk level {level.upper()}."

    return {
        "summary": summary,
        "findings": findings,
        "risk_score": score,
        "risk_level": level,
        "insights": insights
    }