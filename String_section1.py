# 1. Extract the first 3 characters
text = 'Python'
print("1.", text[:3])

# 2. Convert to lowercase
name = 'hello WORLD'
print("2.", name.lower())

# 3. Remove extra spaces
msg = ' Welcome to Python '
print("3.", msg.strip())

# 4. Find the length of the word
word = 'Programming'
print("4.", len(word))

# 5. Split based on comma
text = 'apple,banana,grape'
print("5.", text.split(','))

# 6. Replace 'Java' with 'Python'
text = 'I love Java'
print("6.", text.replace('Java', 'Python'))

# 7. Extract 'Science'
line = 'Data Science'
print("7.", line.split()[1])

# 8. Get the last character
text = 'Python'
print("8.", text[-1])

# 9. Check if 'Python' is present
sentence = 'Learning Python is fun'
print("9.", 'Python' in sentence)

# 10. Join list into a sentence
words = ['Python', 'is', 'easy']
print("10.", ' '.join(words))
