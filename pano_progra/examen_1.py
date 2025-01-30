cadena = str(input("Escribe la suma que quieras hacer: "))

first_number = ""
operator = ""
second_number = ""

for char in cadena:
  if char.isdigit() and operator == "":
    first_number += char
  elif char in "+-*/":
    operator = char
  elif char.isdigit():
    second_number += char

num1 = int(first_number)
num2 = int(second_number)

print(f"First number: {num1}")
print(f"Operator: {operator}")
print(f"Second number: {num2}")