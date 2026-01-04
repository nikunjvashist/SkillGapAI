# Basic Skill Matcher

# Take resume skills input
resume_input = input("Enter resume skills (comma separated): ")
resume_skills = [skill.strip().lower() for skill in resume_input.split(",")]

# Take job skills input
job_input = input("Enter job required skills (comma separated): ")
job_skills = [skill.strip().lower() for skill in job_input.split(",")]

# Compare
matched = [skill for skill in job_skills if skill in resume_skills]
missing = [skill for skill in job_skills if skill not in resume_skills]

# Output
print("\nMatched Skills:", matched)
print("Missing Skills:", missing)
