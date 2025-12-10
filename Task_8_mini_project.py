# Tech Stack Counter

# Predefined categories
programming_languages = ["python", "java", "c", "c++", "javascript", "ruby", "go"]
databases = ["mysql", "mongodb", "oracle", "postgresql", "sqlite"]
frameworks = ["django", "flask", "react", "angular", "spring", "nodejs"]

# Input from user
stack_input = input("Enter tools/technologies (comma separated): ").lower()

# Convert to list
stack_items = [item.strip() for item in stack_input.split(",")]

# Counters
pl_count = 0
db_count = 0
fw_count = 0

# Classification
for item in stack_items:
    if item in programming_languages:
        pl_count += 1
    elif item in databases:
        db_count += 1
    elif item in frameworks:
        fw_count += 1

# Output summary
print("\n--- Tech Stack Summary ---")
print("Programming Languages:", pl_count)
print("Databases:", db_count)
print("Frameworks:", fw_count)
