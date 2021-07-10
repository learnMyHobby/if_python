# Write a python program to find the largest of three numbers

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

for i in range(3):
    if number1 > number2:
        print(f"{number1} is greater than {number2} and {number3}")
    elif number2 > number3:
        print(f"{number2} is greater than {number3} and {number1}")
    else:
        print(f"{number3} is greater than {number1} and {number2}")

