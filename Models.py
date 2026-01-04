
import math
import random
import datetime
import os
import sys
import json
import re
import statistics
import time

# -------------------- 1 --------------------
# Square root using math.sqrt()
num = 16
print("1.", math.sqrt(num))

# -------------------- 2 --------------------
# Floor and Ceil
value = 5.67
print("2.", math.floor(value), math.ceil(value))

# -------------------- 3 --------------------
# Random number between 1 and 100
print("3.", random.randint(1, 100))

# -------------------- 4 --------------------
# 5 random integers between 10 and 20
print("4.", [random.randint(10, 20) for _ in range(5)])

# -------------------- 5 --------------------
# Today's date
today = datetime.date.today()
print("5.", today)

# -------------------- 6 --------------------
# Current year, month, day
print("6.", today.year, today.month, today.day)

# -------------------- 7 --------------------
# Current working directory
print("7.", os.getcwd())

# -------------------- 8 --------------------
# List all files in current directory
print("8.", os.listdir())

# -------------------- 9 --------------------
# Python version
print("9.", sys.version)

# -------------------- 10 --------------------
# JSON string to dictionary
json_str = '{"name": "Nikunj", "branch": "ICE", "year": 4}'
data = json.loads(json_str)
print("10.", data)

# -------------------- 11 --------------------
# Math functions
print("11.",
      "cos(0) =", math.cos(0),
      "sin(90°) =", math.sin(math.radians(90)),
      "log(10) =", math.log(10))

# -------------------- 12 --------------------
# Dice roll simulation (10 times)
dice_rolls = [random.randint(1, 6) for _ in range(10)]
print("12.", dice_rolls)

# -------------------- 13 --------------------
# Days left for next birthday (example: 15 August)
birthday = datetime.date(today.year, 8, 15)
if birthday < today:
    birthday = datetime.date(today.year + 1, 8, 15)
days_left = (birthday - today).days
print("13.", days_left, "days left for next birthday")

# -------------------- 14 --------------------
# Add 30 days to given date
date_obj = datetime.datetime.strptime("2022-05-15", "%Y-%m-%d")
new_date = date_obj + datetime.timedelta(days=30)
print("14.", new_date)

# -------------------- 15 --------------------
# Create folder named 'backup'
folder_name = "backup"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
print("15. Folder 'backup' created (if not already present)")

# -------------------- 16 --------------------
# Dictionary to JSON
dict_data = {"course": "Python", "level": "Beginner"}
json_output = json.dumps(dict_data)
print("16.", json_output)

# -------------------- 17 --------------------
# Extract digits using regex
text = "Order123Number456"
digits = re.findall(r'\d', text)
print("17.", digits)

# -------------------- 18 --------------------
# Check if string starts with 'Hello'
string = "Hello Python World"
match = re.match(r'^Hello', string)
print("18.", bool(match))

# -------------------- 19 --------------------
# Mean, Median, Mode
nums = [10, 20, 20, 30, 40]
print("19.",
      "Mean =", statistics.mean(nums),
      "Median =", statistics.median(nums),
      "Mode =", statistics.mode(nums))

# -------------------- 20 --------------------
# Measure execution time
start = time.time()
for i in range(1, 1_000_001):
    pass
end = time.time()
print("20. Execution time:", end - start, "seconds")
