# Exercise 3
# Your solution comes here
seconds = int(input("enter a number of seconds"))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = ((seconds % 3600) % 60 ) % 60
print(str(hours) + ":" + str(minutes) + ":" + str(seconds))