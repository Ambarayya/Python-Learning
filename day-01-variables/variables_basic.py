
# Exercise 1 — Creating variables

name = "Ambarayya"
age = 23
profession = "AI Developer"
experience = 2
city = "Bangalore"

print(name)
print(age)
print(profession)
print(experience)
print(city)


# Exercise 2 — Finding the datatype of variables

name = "Ambarayya"
age = 23
num = 0.34
is_working = True

print(type(name))
print(type(age))
print(type(num))
print(type(is_working))


# Exercise 3 — Reassigning variables

x = 10
print("The value of x is:", x)

x = 20
print("The new value of x is:", x)

x = "amar"
print("The reassigned value of x is:", x)


# Exercise 4 — Multiple assignment

a, b, c = 10, 20, 30

print(a, b, c)


# Exercise 5 — Swapping variables without a third variable

a = 10
b = 20

print("Before swapping, value of a is:", a)
print("Before swapping, value of b is:", b)

a, b = b, a

print("After swapping, value of a is:", a)
print("After swapping, value of b is:", b)


# Exercise 6 — Type conversion

age = "25"

new_age = int(age) + 5

print(new_age)


value = "0.34"

print(float(value))


price = 99

print(str(price) + " Rupees")


# Exercise 7 — Variable calculations

price = 500
quantity = 3
discount = 50

total_price = price * quantity
price_after_discount = (total_price * discount) / 100

print("The total price is:", total_price)
print("Discount amount is:", price_after_discount)


# Exercise 8 — User input

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello, I am {name}")
print(f"I am {age} years old")


# Exercise 9 — Salary calculation

monthly_salary = int(input("Enter your salary: "))

annual_salary = 12 * monthly_salary
bonus = annual_salary / 10
total_annual_income = annual_salary + bonus

print("Monthly salary:", monthly_salary)
print("Annual salary:", annual_salary)
print("Bonus:", bonus)
print("Total annual income:", total_annual_income)


# Exercise 10 — Student marks

python_marks = int(input("Enter your Python marks: "))
sql_marks = int(input("Enter your SQL marks: "))
ai_marks = int(input("Enter your AI marks: "))
ml_marks = int(input("Enter your ML marks: "))

total_marks = python_marks + sql_marks + ai_marks + ml_marks
average_marks = total_marks / 4

print("Total marks:", total_marks)
print("Average marks:", average_marks)


# Exercise 11 — Temperature conversion

celsius = int(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"The converted temperature is {fahrenheit}°F")


# Exercise 12 — Rectangle

length = int(input("Enter the rectangle length: "))
width = int(input("Enter the rectangle width: "))

perimeter = 2 * (length + width)
area = length * width

print("Perimeter:", perimeter)
print("Area:", area)


# Challenge Problems

# Challenge 1 — Rearrange variables

# Given:
# a = 10
# b = 20
# c = 30

# Make:
# a = 30
# b = 10
# c = 20

a, b, c = 10, 20, 30

print(f"Before swapping: a = {a}, b = {b}, c = {c}")

a, b, c = c, a, b

print(f"After swapping: a = {a}, b = {b}, c = {c}")


# Challenge 2 — Reassignment and references

x = 10
y = x
x = 20

print(x)
print(y)


# Challenge 3 — Dynamic typing

x = 10
x = "hello"
x = 5.5
x = True

print(x)
print(type(x))


# ============================================================
# Exercise 1 - Employee Information
# ============================================================

emp_name = "Ambarayya"
emp_id = 25
emp_salary = 25000
emp_exp = 2
emp_dpt = "Software"

print(f"Employee Name is: {emp_name}")
print(f"Employee ID is: {emp_id}")
print(f"Employee Salary is: {emp_salary}")
print(f"Employee has {emp_exp} years experience.")
print(f"Employee works in {emp_dpt} Department")


# ============================================================
# Exercise 2 - Salary Calculation
# ============================================================

"""
Monthly salary = 45000
Annual salary
Monthly tax = 10%
Salary after tax
"""

monthly_salary = 45000
monthly_tax = 10

annual_salary = monthly_salary * 12
monthly_salary_after_tax = monthly_salary - (monthly_salary * monthly_tax) / 100
annual_salary_after_tax = monthly_salary_after_tax * 12

print(f"Monthly salary is: {monthly_salary}")
print(f"The monthly tax deduction is: {monthly_tax}%")
print(f"Monthly salary after tax is: {monthly_salary_after_tax}")
print(f"Annual salary is: {annual_salary}")
print(f"Annual salary after tax is: {annual_salary_after_tax}")


# ============================================================
# Exercise 3 - Shopping Bill
# ============================================================

item_price = 2300
quantity = 4
discount = 15

total_price = item_price * quantity
discount_amount = (total_price * discount) / 100
final_bill = total_price - discount_amount

print(f"The total price is: {total_price}")
print(f"The discount amount for {discount}% is: {discount_amount}")
print(f"The final bill after discount is: {final_bill}")


# ============================================================
# Exercise 4 - Understanding Variable Assignment
# ============================================================

x = 10
y = x

x = 20

print(f"Value of x: {x}")
print(f"Value of y: {y}")


# ============================================================
# Exercise 5 - String and Integer Concatenation
# ============================================================

"""
The following code produces an error because an integer
cannot be directly concatenated with a string using +.

age = 23

print("I am " + age + " years old")
"""

# Method 1 - Type conversion

age = 23

print("I am " + str(age) + " years old")


# Method 2 - Using f-string

print(f"I am {age} years old")


# ============================================================
# Exercise 6 - User Input
# ============================================================

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print(f"My name is {name}")
print(f"I am {age} years old")
print(f"I live in {city}")


# ============================================================
# Exercise 7 - Calculate Age
# ============================================================

birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter the current year: "))

age = current_year - birth_year

print(f"Your age is: {age}")