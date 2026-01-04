def calculate_metrics(matched, partial, missing):
    total = len(matched) + len(partial) + len(missing)

    overall_match = int((len(matched) / total) * 100) if total > 0 else 0

    return {
        "overall_match": overall_match,
        "matched": len(matched),
        "partial": len(partial),
        "missing": len(missing)
    }
