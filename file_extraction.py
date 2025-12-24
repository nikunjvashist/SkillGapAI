

import csv
from collections import Counter

# -------------------------------
# 1. Create a Python list containing five technical skills and print the list.
# -------------------------------
technical_skills = ["Python", "SQL", "MATLAB", "Control Systems", "PLC"]
print("1. Technical Skills List:", technical_skills)

# -------------------------------
# 2. Create a Python list containing five soft skills and print the list.
# -------------------------------
soft_skills = ["Communication", "Teamwork", "Problem Solving", "Leadership", "Time Management"]
print("2. Soft Skills List:", soft_skills)

# -------------------------------
# 3. Convert the resume text to lowercase
# -------------------------------
resume_text = "Experienced in Python and SQL"
resume_text_lower = resume_text.lower()
print("3. Lowercase Resume Text:", resume_text_lower)

# -------------------------------
# 4. Check whether the word 'python' exists in resume text
# -------------------------------
print("4. Does 'python' exist in resume text?:", "python" in resume_text_lower)

# -------------------------------
# 5. Print technical and soft skills using loops
# -------------------------------
print("5. Technical Skills (Loop):")
for skill in technical_skills:
    print("-", skill)

print("Soft Skills (Loop):")
for skill in soft_skills:
    print("-", skill)

# -------------------------------
# Sample resume & job description text
# -------------------------------
resume_full_text = """
Experienced in Python, SQL, MATLAB and Control Systems.
Strong problem solving and teamwork skills.
"""

job_description_text = """
Looking for candidates with Python, PLC, leadership,
communication and time management skills.
"""

# -------------------------------
# 6. Extract technical skills from resume text
# -------------------------------
extracted_tech_skills = []
for skill in technical_skills:
    if skill.lower() in resume_full_text.lower():
        extracted_tech_skills.append(skill)

print("6. Extracted Technical Skills from Resume:", extracted_tech_skills)

# -------------------------------
# 7. Extract soft skills from job description
# -------------------------------
extracted_soft_skills = []
for skill in soft_skills:
    if skill.lower() in job_description_text.lower():
        extracted_soft_skills.append(skill)

print("7. Extracted Soft Skills from Job Description:", extracted_soft_skills)

# -------------------------------
# 8. Read skills from CSV file and print only technical skills
# (Assume skills.csv contains: skill,category)
# -------------------------------
csv_technical_skills = []

try:
    with open("skills.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["category"].lower() == "technical":
                csv_technical_skills.append(row["skill"])
    print("8. Technical Skills from CSV:", csv_technical_skills)
except FileNotFoundError:
    print("8. skills.csv not found (skip if not available)")

# -------------------------------
# 9. Find common skills between resume and job description
# -------------------------------
resume_words = set(resume_full_text.lower().split())
job_words = set(job_description_text.lower().split())
common_skills = resume_words.intersection(job_words)
print("9. Common Skills:", common_skills)

# -------------------------------
# 10. Store extracted skills without duplicates
# -------------------------------
unique_skills = list(set(extracted_tech_skills + extracted_soft_skills))
print("10. Unique Extracted Skills:", unique_skills)

# -------------------------------
# 11. Store extracted skills in dictionary
# -------------------------------
skills_dict = {
    "Technical Skills": extracted_tech_skills,
    "Soft Skills": extracted_soft_skills
}
print("11. Skills Dictionary:", skills_dict)

# -------------------------------
# 12. Identify missing skills (JD - Resume)
# -------------------------------
resume_all_skills = set(extracted_tech_skills + extracted_soft_skills)
jd_all_skills = set(skill for skill in technical_skills + soft_skills
                    if skill.lower() in job_description_text.lower())

missing_skills = jd_all_skills - resume_all_skills
print("12. Missing Skills:", missing_skills)

# -------------------------------
# 13. Count frequency of each skill in resume
# -------------------------------
resume_tokens = resume_full_text.lower().split()
skill_frequency = {}

for skill in technical_skills + soft_skills:
    count = resume_tokens.count(skill.lower())
    if count > 0:
        skill_frequency[skill] = count

print("13. Skill Frequency in Resume:", skill_frequency)

# -------------------------------
# 14. Case-insensitive skill matching from CSV
# -------------------------------
matched_skills_csv = []

try:
    with open("skills.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["skill"].lower() in resume_full_text.lower():
                matched_skills_csv.append(row["skill"])
    print("14. Case-insensitive CSV Skill Match:", matched_skills_csv)
except FileNotFoundError:
    print("14. skills.csv not found (skip if not available)")

# -------------------------------
# 15. Save extracted skills to a new CSV file
# -------------------------------
with open("extracted_skills.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Skill", "Category"])
    for skill in extracted_tech_skills:
        writer.writerow([skill, "Technical"])
    for skill in extracted_soft_skills:
        writer.writerow([skill, "Soft"])

print("15. Extracted skills saved to extracted_skills.csv")

