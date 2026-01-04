# 1. Print numbers from 1 to 10
print("1. Numbers from 1 to 10")
for i in range(1, 11):
    print(i)
print()

# 2. Print all even numbers from 1 to 20
print("2. Even numbers from 1 to 20")
for i in range(2, 21, 2):
    print(i)
print()

# 3. Print each character of 'Python'
print("3. Characters in 'Python'")
for ch in "Python":
    print(ch)
print()

# 4. While loop: 5 down to 1
print("4. Numbers from 5 down to 1")
i = 5
while i >= 1:
    print(i)
    i -= 1
print()

# 5. Sum of numbers from 1 to 50
print("5. Sum of numbers from 1 to 50")
total = 0
for i in range(1, 51):
    total += i
print(total)
print()

# 6. Multiplication table of 5
print("6. Multiplication table of 5")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
print()

# 7. Count vowels in 'Programming'
print("7. Vowels in 'Programming'")
s = "Programming"
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print(count)
print()

# 8. Reverse 'PythonLoops'
print("8. Reverse of 'PythonLoops'")
text = "PythonLoops"
rev = ""
for ch in text:
    rev = ch + rev
print(rev)
print()

# 9. Print numbers 1–10, skip 5
print("9. Numbers 1–10 skipping 5")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
print()

# 10. Print numbers 1–20, stop at 13
print("10. Numbers from 1–20 stopping at 13")
for i in range(1, 21):
    if i == 13:
        break
    print(i)
print()

# 11. Check if a number is prime
print("11. Prime number check")
num = 29   # change number as needed
is_prime = True

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False

print("Prime" if is_prime else "Not Prime")
print()

# 12. Count character occurrences in 'mississippi'
print("12. Character count in 'mississippi'")
s = "mississippi"
count_dict = {}
for ch in s:
    count_dict[ch] = count_dict.get(ch, 0) + 1
print(count_dict)
print()

# 13. Pattern: *, **, ***, ****, *****
print("13. Pattern (1 to 5 stars)")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
print()

# 14. Largest digit in 5847361
print("14. Largest digit in 5847361")
num = "5847361"
largest = 0
for d in num:
    if int(d) > largest:
        largest = int(d)
print(largest)
print()

# 15. Pattern: *****, ****, ***, **, *
print("15. Reverse star pattern")
for i in range(5, 0, -1):
    print("*" * i)
