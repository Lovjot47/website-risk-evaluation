def apply_rules(data, domain):
    risks = []
    text = data["text"]
    links = data["links"]

    # 🔴 1. Domain Risk
    high_risk_tlds = ["online", "xyz", "top", "site", "club"]

    for tld in high_risk_tlds:
        if domain.endswith(tld):
            risks.append({
                "element": "Domain",
                "rule": f"High-risk TLD detected: .{tld}",
                "severity": "High",
                "rationale": "Disposable or low-trust domain pattern"
            })

    # 🔴 2. Scam Keywords
    suspicious_keywords = [
        "guaranteed profit", "100% return", "instant income"
    ]

    for word in suspicious_keywords:
        if word in text:
            risks.append({
                "element": "Content",
                "rule": f"Suspicious keyword: {word}",
                "severity": "High",
                "rationale": "Fraud pattern"
            })

    # 🔴 3. Compliance (FIXED)
    if not any(k in text for k in ["privacy", "terms", "policy"]) and len(text) < 5000:
        risks.append({
            "element": "Compliance",
            "rule": "Missing legal/compliance pages",
            "severity": "High",
            "rationale": "Non-compliant with standard business requirements"
        })

    # 🟠 4. Identity (FIXED)
    if not data["emails"] and not data["phones"] and "contact" not in text:
        risks.append({
            "element": "Identity",
            "rule": "No contact info",
            "severity": "Medium",
            "rationale": "Low transparency"
        })

    if "about" not in text and len(text) < 5000:
        risks.append({
            "element": "Identity",
            "rule": "Missing About Us",
            "severity": "Medium",
            "rationale": "Weak business identity"
        })

    # 🟠 5. Content Quality
    if len(text) < 800:
        risks.append({
            "element": "Content",
            "rule": "Low content volume",
            "severity": "Medium",
            "rationale": "Low credibility / incomplete site"
        })

    # 🟠 6. Link Behavior
    external_links = [l for l in links if l and l.startswith("http")]

    if len(external_links) > 50:
        risks.append({
            "element": "Links",
            "rule": "High number of external links",
            "severity": "Medium",
            "rationale": "Spam/redirect behavior"
        })

    return risks