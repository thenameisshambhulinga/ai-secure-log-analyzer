from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import re
import io
from PyPDF2 import PdfReader

app = FastAPI()

# CORS (to connect frontend)
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

# Risk mapping
risk_map = {
    "email": "low",
    "api_key": "high",
    "password": "critical",
    "error": "medium"
}

# Score mapping
score_map = {
    "low": 1,
    "medium": 3,
    "high": 5,
    "critical": 10
}

# Mask sensitive data
def mask_sensitive(line):
    line = re.sub(r"password=\w+", "password=****", line)
    line = re.sub(r"sk-[a-zA-Z0-9]+", "sk-****", line)
    return line


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    filename = file.filename

    # 🔥 FILE TYPE HANDLING
    if filename.endswith(".txt") or filename.endswith(".log") or filename.endswith(".sql"):
        content = (await file.read()).decode(errors="ignore")

    elif filename.endswith(".pdf"):
        pdf_bytes = await file.read()
        reader = PdfReader(io.BytesIO(pdf_bytes))

        content = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                content += text + "\n"

    elif filename.endswith(".doc") or filename.endswith(".docx"):
        content = "DOC processing supported (extendable)"

    else:
        content = (await file.read()).decode(errors="ignore")

    lines = content.split("\n")

    findings = []
    score = 0

    # 🔍 Detection Engine
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

    # ⚠ Risk Engine
    if score >= 20:
        level = "critical"
    elif score >= 10:
        level = "high"
    elif score >= 5:
        level = "medium"
    else:
        level = "low"

    # 🤖 AI INSIGHTS
    insights = []
    types = [f["type"] for f in findings]

    if "password" in types:
        insights.append("Critical risk: Plaintext passwords detected, which may lead to account compromise.")

    if "api_key" in types:
        insights.append("High risk: API keys exposed, allowing possible unauthorized access.")

    if "email" in types:
        insights.append("Low risk: Email addresses detected, may expose user identity.")

    if "error" in types:
        insights.append("Medium risk: System errors detected, revealing internal system behavior.")

    if score > 15:
        insights.append("Overall system risk is high. Immediate remediation recommended.")

    if len(findings) >= 4:
        insights.append("Multiple sensitive data points detected, indicating logging misconfiguration.")

    if len(findings) == 0:
        insights.append("No major security risks detected. System appears safe.")

    # 📊 Summary
    summary = f"AI-driven analysis detected {len(findings)} issues with overall risk level {level.upper()}."

    return {
        "summary": summary,
        "findings": findings,
        "risk_score": score,
        "risk_level": level,
        "insights": insights
    }