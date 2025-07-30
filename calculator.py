#ask input number from user
first_number = float(input("Enter first number: "))
#ask input number from user
second_number = float(input("Enter second number: "))
#ask for a choice of operation
operation = input("Enter operation (+, -, *, /): ")

#testing the operation
if operation == '+':
    result = f"{first_number} + {second_number} = {first_number + second_number}"
elif operation == '-':
    result = f"{first_number} - {second_number} = {first_number - second_number}"
elif (operation == '*'):
    result = f"{first_number} * {second_number} = {first_number * second_number}"
elif (operation == '/'):
  # comment:     
