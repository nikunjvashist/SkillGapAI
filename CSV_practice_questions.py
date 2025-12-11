import csv
import os

# -----------------------------------------------------------
# 1. Create students.csv with 3 records
# -----------------------------------------------------------
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "grade"])
    writer.writerow(["Riya", 20, "A"])
    writer.writerow(["Aman", 19, "B"])
    writer.writerow(["Neha", 21, "A"])

print("1. students.csv created")


# -----------------------------------------------------------
# 2. Read and print rows from employees.csv
# -----------------------------------------------------------
print("\n2. employees.csv rows:")
try:
    with open("employees.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("employees.csv not found")


# -----------------------------------------------------------
# 3. Print first column from products.csv
# -----------------------------------------------------------
print("\n3. First column from products.csv (product names):")
try:
    with open("products.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0])
except FileNotFoundError:
    print("products.csv not found")


# -----------------------------------------------------------
# 4. Read CSV using DictReader and print key-value pairs
# -----------------------------------------------------------
print("\n4. DictReader (data.csv):")
try:
    with open("data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            for k, v in row.items():
                print(k, ":", v)
            print()
except FileNotFoundError:
    print("data.csv not found")


# -----------------------------------------------------------
# 5. Add a new row to marks.csv
# -----------------------------------------------------------
print("5. Adding new row to marks.csv...")
try:
    with open("marks.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Rohan", "Math", 95])
    print("Row added")
except FileNotFoundError:
    print("marks.csv not found")


# -----------------------------------------------------------
# 6. Count rows in data.csv
# -----------------------------------------------------------
print("\n6. Row count in data.csv:")
count = 0
try:
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for _ in reader:
            count += 1
    print("Total rows:", count)
except FileNotFoundError:
    print("data.csv not found")


# -----------------------------------------------------------
# 7. Read sales.csv and calculate total sales
# -----------------------------------------------------------
print("\n7. Total sales from sales.csv:")
try:
    total_sales = 0
    with open("sales.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_sales += float(row["price"]) * int(row["quantity"])
    print("Total Sales =", total_sales)
except FileNotFoundError:
    print("sales.csv not found")


# -----------------------------------------------------------
# 8. Convert list of lists into a CSV file
# -----------------------------------------------------------
print("\n8. Creating output.csv from a list of lists...")
data = [
    [1, "Riya"],
    [2, "Aman"],
    [3, "Neha"]
]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name"])
    writer.writerows(data)

print("output.csv created")


# -----------------------------------------------------------
# 9. Filter rows from people.csv where age > 30
# -----------------------------------------------------------
print("\n9. people.csv rows where age > 30:")
try:
    with open("people.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row["age"]) > 30:
                print(row)
except FileNotFoundError:
    print("people.csv not found")


# -----------------------------------------------------------
# 10. Copy source.csv ➜ copy.csv
# -----------------------------------------------------------
print("\n10. Copying source.csv to copy.csv...")
try:
    with open("source.csv", "r") as src, open("copy.csv", "w", newline="") as dst:
        reader = csv.reader(src)
        writer = csv.writer(dst)
        for row in reader:
            writer.writerow(row)
    print("copy.csv created")
except FileNotFoundError:
    print("source.csv not found")
