# Experience Extractor

sentence = input("Enter experience statement:\n")

experience_years = None

for char in sentence:
    if char.isdigit():   # detect any number
        experience_years = char
        break

if experience_years:
    print(f"Experience Detected: {experience_years} Years")
else:
    print("No experience value detected.")
