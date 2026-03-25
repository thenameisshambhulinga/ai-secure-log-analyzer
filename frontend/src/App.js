import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    if (!file) return alert("Upload file first");

    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post("http://127.0.0.1:8000/analyze", formData);
    setResult(res.data);
  };

  const getColor = (risk) => {
    if (risk === "critical") return "red";
    if (risk === "high") return "orange";
    if (risk === "medium") return "gold";
    return "green";
  };

  return (
    <div
      style={{
        fontFamily: "Arial",
        background: "#111",
        color: "#fff",
        minHeight: "100vh",
        padding: "20px",
      }}
    >
      <h1>🔐 AI Secure Data Intelligence Platform</h1>
      <p style={{ color: "gray" }}>
        AI-powered real-time log security intelligence
      </p>

      {/* Upload */}
      <div style={{ marginTop: "20px" }}>
        <input type="file" onChange={(e) => setFile(e.target.files[0])} />
        <button onClick={handleUpload} style={{ marginLeft: "10px" }}>
          Analyze
        </button>
      </div>

      {result && (
        <div style={{ marginTop: "30px" }}>
          {/* Summary */}
          <h2>📊 Summary</h2>
          <p>{result.summary}</p>

          {/* Security Status */}
          <h2>🛡 Security Status</h2>
          <p style={{ color: getColor(result.risk_level), fontWeight: "bold" }}>
            {result.risk_level === "high" || result.risk_level === "critical"
              ? "⚠ System is Vulnerable"
              : "✅ System is Safe"}
          </p>

          {/* Risk */}
          <h2>⚠ Risk Level</h2>
          <h3 style={{ color: getColor(result.risk_level) }}>
            {result.risk_level.toUpperCase()} (Score: {result.risk_score})
          </h3>

          {/* Findings */}
          <h2>🔍 Findings</h2>
          <table border="1" cellPadding="10">
            <thead>
              <tr>
                <th>Type</th>
                <th>Line</th>
                <th>Content</th>
                <th>Risk</th>
              </tr>
            </thead>
            <tbody>
              {result.findings.map((f, i) => (
                <tr key={i}>
                  <td>{f.type}</td>
                  <td>{f.line}</td>
                  <td>{f.content}</td>
                  <td style={{ color: getColor(f.risk), fontWeight: "bold" }}>
                    {f.risk}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>

          {/* Insights */}
          <h2>💡 AI Insights</h2>
          <ul>
            {result.insights.map((i, idx) => (
              <li key={idx}>{i}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
