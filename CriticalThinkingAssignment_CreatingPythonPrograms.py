# CRITICAL THINKING ASSIGNMENT - Module 1 Creating Python Programs

# Part 1 - Addition and Subtraction of User Inputted Numbers
print('Addition and Subtraction')
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print(num1, '+', num2, '=', num1 + num2)
print(num1, '-', num2, '=', num1 - num2)

print()
print()
# Part 2 - Multiplication and Division of User Inputted Numbers
print('Multiplication and Division')
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print(num1, '*', num2, '=', num1 * num2)
if (num2 != 0):
    print(num1, '/', num2, '=', num1 / num2)
else:
    print('Cannot Divide by 0')