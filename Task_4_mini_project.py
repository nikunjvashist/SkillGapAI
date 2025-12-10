# Job Title Normalizer

import string

# Input job title
job_title = input("Enter job title: ")

# Remove special characters
clean_title = job_title.translate(str.maketrans("", "", string.punctuation))

# Convert to title case
normalized_title = clean_title.title()

# Output
print("Normalized Job Title:", normalized_title)
