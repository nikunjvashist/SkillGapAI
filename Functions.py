# 1. Function that prints a welcome message
def welcome():
    print("Welcome to Python!")

welcome()


# 2. Function that greets a person
def greet(name):
    print("Hello", name)

greet("Nikunj")


# 3. Function that returns square of a number
def square(n):
    return n * n

print("Square:", square(5))


# 4. Function that returns sum, difference, and product
def calculator(a, b):
    return a + b, a - b, a * b

result = calculator(10, 5)
print("Sum, Difference, Product:", result)


# 5. Function with default argument
def country(name="India"):
    print("I am from", name)

country()
country("Canada")


# 6. Function with variable-length arguments
def total(*nums):
    return sum(nums)

print("Total:", total(10, 20, 30, 40))


# 7. Function with keyword arguments
def student_info(**data):
    for key, value in data.items():
        print(key, ":", value)

student_info(name="Nikunj", branch="ICE", year=4)


# 8. Function to count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

print("Vowel count:", count_vowels("Python Programming"))


# 9. Lambda function to find cube of a number
cube = lambda x: x ** 3
print("Cube:", cube(4))


# 10. Function to return unique letters in order
def unique_letters(text):
    result = ""
    for ch in text:
        if ch not in result:
            result += ch
    return result

print("Unique letters:", unique_letters("programming"))
