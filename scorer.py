def calculate_risk_score(risks):
    score = 0

    for r in risks:
        if r["severity"] == "High":
            score += 4
        elif r["severity"] == "Medium":
            score += 2
        else:
            score += 1

    # 🔧 Adjusted thresholds
    if score >= 12:
        overall_risk = "High Risk"
    elif score >= 6:
        overall_risk = "Medium Risk"
    else:
        overall_risk = "Low Risk"

    return overall_risk, score