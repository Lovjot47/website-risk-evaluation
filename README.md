📌 Website Risk Evaluation System

🔹 Overview

This project implements a rule-based website risk evaluation engine that analyzes merchant websites by extracting on-site signals and correlating them with external intelligence.

⚙️ Features

Website crawling and content extraction
Rule-based risk detection (domain, identity, compliance, behavior)
External correlation using public search data
Structured risk reporting with severity and rationale
Risk scoring system

🧠 Pipeline

Input URL → Crawl → Extract → Rules → External Correlation → Score → Report
📊 Sample Results
🟢 manifestwaresoftware.com
Low Risk
Minimal risk indicators
🟠 zylotechindia.online
Medium Risk
High-risk TLD (.online)
Limited external signals

🚀 How to Run

pip install -r requirement.txt
python app.py

Then open:
http://127.0.0.1:5000/

## 📸 Demo
<img width="1871" height="596" alt="Screenshot 2026-04-16 033637" src="https://github.com/user-attachments/assets/084623a2-6486-4ae1-b13c-7f15018adb79" />
<img width="1466" height="580" alt="Screenshot 2026-04-16 033210" src="https://github.com/user-attachments/assets/81fe7675-ddbf-4c53-966a-5f149af6da24" />

⚠️ Limitations

Uses static HTML parsing
Dynamic (JS-heavy) websites may have incomplete extraction

🔮 Future Improvements

Headless browser (Selenium/Playwright)
WHOIS integration
ML-based risk scoring
