# 1. Extract 'Programming' using slicing only
text = 'PythonProgramming'
print("1.", text[6:])

# 2. Count how many times 'Hello' appears
s = 'Hello, Python, Hello, World'
print("2.", s.count('Hello'))

# 3. Reverse the string without using reverse()
word = 'Development'
print("3.", word[::-1])

# 4. Replace 'awesome' with 'powerful' only if 'Python' exists
sentence = 'Python is awesome'
if 'Python' in sentence:
    sentence = sentence.replace('awesome', 'powerful')
print("4.", sentence)

# 5. Count overlapping occurrences of 'aaa'
text = 'aaabbbcccaaa'
count = 0
for i in range(len(text) - 2):
    if text[i:i+3] == 'aaa':
        count += 1
print("5.", count)

# 6. Extract username and domain from email
email = 'username@example.com'
username, domain = email.split('@')
print("6.", "Username:", username, ", Domain:", domain)

# 7. Extract numeric value from the string
line = 'The price is 1500 rupees'
number = ''
for ch in line:
    if ch.isdigit():
        number += ch
print("7.", number)

# 8. Split by '-' and rejoin with spaces
words = 'python-is-simple-and-powerful'
print("8.", ' '.join(words.split('-')))

# 9. Remove numbers and keep only letters
text = 'Hello123World45Python'
letters_only = ''
for ch in text:
    if ch.isalpha():
        letters_only += ch
print("9.", letters_only)

# 10. Find first character that appears more than once
text = 'Mississippi'
found = None
for ch in text:
    if text.count(ch) > 1:
        found = ch
        break
print("10.", found)
