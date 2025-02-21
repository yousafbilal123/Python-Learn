first = int(input("Enter the number: "))  
operator = input("Enter operator (+, -, *, /, %): ")


second = int(input("Enter the number: ")) 

if operator == '+':
    print(first + second)
elif operator == '-':
    print(first - second)
elif operator == '*':
    print(first * second)
elif operator == '/':
    if second != 0:
        print(first / second)
    else:
        print("Cannot divide by zero.")
elif operator == '%':
    print(first % second)
else:
    print("Invalid operator.")
