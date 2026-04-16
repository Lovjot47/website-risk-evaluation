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

⚠️ Limitations

Uses static HTML parsing
Dynamic (JS-heavy) websites may have incomplete extraction

🔮 Future Improvements

Headless browser (Selenium/Playwright)
WHOIS integration
ML-based risk scoring
