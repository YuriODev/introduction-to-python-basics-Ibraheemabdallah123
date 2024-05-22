# Exercise 4
# Your solution comes here
fourdigit = input("enter a four digit number: ")
if len(fourdigit) == 3:
  fourdigit = str(0) + fourdigit
elif len(fourdigit) == 2:
  fourdigit = str(0) + str(0) + fourdigit
elif len(fourdigit) == 1:
  fourdigit = str(0) + str(0) + str(0) + fourdigit
if fourdigit[0] == fourdigit[3] and fourdigit[1] == fourdigit[2]:
  print(1)
else:
  print(0)