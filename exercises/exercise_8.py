# Exercise 8
# Your solution comes here
num = int(input("enter a number to sort in a list"))
num1 = int(input("enter a number to sort in a list"))
num2 = int(input("enter a number to sort in a list"))
if num > num1 and num > num2 and num2 > num1:
  print(num)
  print(num2)
  print(num1)
elif num > num1 and num > num2 and num2 < num1:
  print(num)
  print(num1)
  print(num2)
elif num1 > num and num1 > num2 and num > num2:
  print(num1)
  print(num)
  print(num2)
elif num1 > num and num1 > num2 and num < num2:
  print(num1)
  print(num2)
  print(num)
elif num2 > num and num2 > num1 and num > num1:
  print(num2)
  print(num)
  print(num1)
else:
  print(num2)
  print(num1)
  print(num)