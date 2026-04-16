from googlesearch import search

def external_check(domain):
    try:
        queries = [
            f"{domain}",
            f"{domain} review",
            f"{domain} scam"
        ]

        results = []

        for query in queries:
            try:
                res = list(search(query, num_results=2))
                results.extend(res)
            except:
                continue

        results = list(set(results))

        # 🔧 FIX: Only mark low footprint if truly empty
        if not results:
            return [f"Low digital footprint for {domain}"]

        return results[:3]

    except:
        return ["External lookup failed"]