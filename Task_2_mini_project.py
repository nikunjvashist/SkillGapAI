# Resume Word Counter

# Input your paragraph
text = input("Enter a paragraph of resume text:\n")

# Normalize the text: convert to lowercase and remove punctuation
import string
clean_text = text.lower().translate(str.maketrans("", "", string.punctuation))

# Split into words
words = clean_text.split()

# Count the total words 
total_words = len(words)

# Count the unique words
unique_words = set(words)
unique_count = len(unique_words)

# Most repeated word
word_frequency = {}
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

most_repeated = max(word_frequency, key=word_frequency.get)

# Output
print("\n--- Resume Word Analysis ---")
print("Total words:", total_words)
print("Unique words:", unique_count)
print("Most repeated word:", most_repeated)
