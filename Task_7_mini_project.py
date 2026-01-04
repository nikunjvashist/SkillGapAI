# Simple Email Extractor (No Regex)

text = input("Enter text block:\n")

# Split into words
words = text.split()

email = None

# Check which word contains "@"
for word in words:
    if "@" in word:
        email = word.strip(",.")  # remove punctuation if attached
        break

# Output result
if email:
    print("Email found:", email)
else:
    print("No email detected.")
