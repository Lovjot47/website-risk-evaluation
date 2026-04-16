def get_risk_category(element):
    mapping = {
        "Domain": "Domain Trust Risk",
        "Content": "Content Risk",
        "Compliance": "Regulatory Risk",
        "Identity": "Identity Risk",
        "Links": "Behavioral Risk"
    }
    return mapping.get(element, "General Risk")


def generate_report(risks, external_data, overall_risk, domain):

    findings = []

    # 🌍 External Evidence (FIXED - safer wording)
    if external_data and not any("Low digital footprint" in str(e) for e in external_data):
        evidence = external_data[:2]
    else:
        evidence = ["Limited external signals detected (may require deeper verification)"]

    # 📊 Build Findings
    for r in risks:
        findings.append({
            "Detected Element": r["element"],
            "Matched External Evidence": evidence,
            "Rule Triggered": r["rule"],
            "Risk Category": get_risk_category(r["element"]),
            "Severity": r["severity"],
            "Rationale": r["rationale"]
        })

    # 📈 Summary Logic
    high = sum(1 for r in risks if r["severity"] == "High")
    medium = sum(1 for r in risks if r["severity"] == "Medium")

    if high > 0 or medium > 0:
        summary = f"{high} high-risk and {medium} medium-risk indicators detected."
    else:
        summary = "Minimal risk indicators detected."

    # 🧠 Final Decision Layer
    if overall_risk == "High Risk":
        decision = (
            "The merchant exhibits multiple high-risk indicators across domain trust, "
            "compliance, and identity dimensions, suggesting elevated fraud or credibility risk."
        )
    elif overall_risk == "Medium Risk":
        decision = (
            "The merchant shows moderate risk signals; further verification and due diligence "
            "are recommended before onboarding."
        )
    else:
        decision = (
            "The merchant shows minimal risk indicators and appears relatively trustworthy "
            "based on available signals."
        )

    return {
        "Findings": findings,
        "Overall Risk": overall_risk,
        "Summary": summary,
        "Decision": decision
    }