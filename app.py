from flask import Flask, render_template, request
from crawler import fetch_website
from extractor import extract_elements
from rules import apply_rules
from external import external_check
from scorer import calculate_risk_score
from report import generate_report
import tldextract

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    report = None
    url = ""

    if request.method == "POST":
        url = request.form["url"]

        # 🌐 Fetch website
        html = fetch_website(url)

        if html:
            # 🔍 Extract data
            data = extract_elements(html)

            # 🌍 Extract domain properly
            ext = tldextract.extract(url)
            full_domain = f"{ext.domain}.{ext.suffix}"

            # 🧠 Apply rules
            risks = apply_rules(data, full_domain)

            # 🌍 External correlation
            external_data = external_check(full_domain)

            # 📊 Risk scoring
            overall, score = calculate_risk_score(risks)

            # 🛡️ Trusted domain handling (FIXED)
            trusted_domains = ["amazon", "flipkart", "bigbasket", "google"]
            if any(td in full_domain for td in trusted_domains):
                overall = "Low Risk"
                score = min(score, 3)   # ✅ keeps consistency

            # 📄 Generate report
            report = generate_report(risks, external_data, overall, full_domain)

            # ➕ Add score to report
            report["Score"] = score

        else:
            report = {
                "Overall Risk": "Error",
                "Summary": "Failed to fetch website.",
                "Decision": "Unable to evaluate the website due to fetch failure.",
                "Findings": [],
                "Score": 0
            }

    return render_template("index.html", report=report, url=url)


if __name__ == "__main__":
    app.run(debug=True)