# ============================================================
# Problem 1 — Type Conversion Pipeline
# ============================================================

user_id = "1025"
age = "23"
salary = "45000.75"
is_active = "True"

user_id = int(user_id)
age = int(age)
salary = float(salary)
is_active = is_active.lower() == "true"

print(user_id, type(user_id))
print(age, type(age))
print(salary, type(salary))
print(is_active, type(is_active))


# ============================================================
# Problem 2 — Mixed-Type Calculation
# ============================================================

a = "100"
b = 25
c = 10.5

a = int(a)

total = a + b + c

print(total, type(total))


# ============================================================
# Problem 3 — Operator and Type Prediction
# ============================================================

a = 10
b = 3

result1 = a / b
result2 = a // b
result3 = a % b
result4 = a ** b

print(result1, type(result1))
print(result2, type(result2))
print(result3, type(result3))
print(result4, type(result4))


# ============================================================
# Problem 4 — Truthy and Falsy Values
# ============================================================

values = [0, 1, "", "False", "True", None, [], [1]]

for value in values:
    print(value, "=>", bool(value))


# ============================================================
# Problem 5 — Numeric Type Behavior
# ============================================================

a = 10
b = 2.0

x = a + b
y = a * b
z = a / 2
w = a // 2

print(x, type(x))
print(y, type(y))
print(z, type(z))
print(w, type(w))


# ============================================================
# Problem 6 — API Data Normalization
# ============================================================

user_id = "1001"
name = "Ambarayya"
age = "23"
salary = "45000.50"
is_active = "true"
experience = "2"

user_id = int(user_id)
age = int(age)
salary = float(salary)
experience = int(experience)
is_active = is_active.lower() == "true"

converted_data = {
    "user_id": user_id,
    "name": name,
    "age": age,
    "salary": salary,
    "is_active": is_active,
    "experience": experience
}

print(converted_data)