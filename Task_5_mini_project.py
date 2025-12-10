# Simple Resume Category Classifier

# Input skills
skills_input = input("Enter skills (comma separated): ").lower()

# Convert to list
skills = [skill.strip() for skill in skills_input.split(",")]

# Classification logic
if "machine learning" in skills or "data science" in skills or "python" in skills or "statistics" in skills:
    category = "Data / ML"
elif "html" in skills or "css" in skills or "javascript" in skills or "react" in skills:
    category = "Web Development"
elif "java" in skills or "c++" in skills or "software engineering" in skills:
    category = "Software Development"
else:
    category = "Other"

# Output result
print("Predicted Category:", category)
