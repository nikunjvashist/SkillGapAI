def map_skill_to_group(skill):
    s = skill.lower()

    # Core technical skills
    if "machine learning" in s or s.strip() == "ml":
        return "ML"

    if "python" in s:
        return "Python"

    if "sql" in s and "nosql" not in s:
        return "SQL"

    if "visual" in s or "tableau" in s or "matplotlib" in s:
        return "Data Visualization"

    # Statistics differentiation
    if "advanced statistic" in s:
        return "Adv. Stats"

    if "basic statistic" in s or "statistical method" in s:
        return "Stats (Basic)"

    # Databases & Cloud
    if "nosql" in s or "mongodb" in s:
        return "NoSQL"

    if "aws" in s or "cloud" in s:
        return "Cloud"

    # Soft skills
    if "communicat" in s:
        return "Communication"

    if "leader" in s:
        return "Team Leadership"

    return None
