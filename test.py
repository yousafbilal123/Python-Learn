num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = num1 * num2


with open("multiplication_result.txt", "w") as file:
    file.write(f"The result of the multiplication is {result}")

print("Result written to multiplication_result.txt")