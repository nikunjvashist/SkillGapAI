# Skill Frequency Checker

# Input resume paragraph
text = input("Enter resume text:\n").lower()

# Input skill to search
skill = input("Enter skill to check frequency: ").lower()

# Split text into words
words = text.split()

# Count frequency
count = words.count(skill)

# Output result
print(f"Skill appears {count} times.")
