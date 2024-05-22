# Exercise 3
# Your solution comes here
seconds = int(input("enter a number of seconds"))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = ((seconds % 3600) % 60 ) % 60
# print(hours + ":" + minutes + ":" + seconds)
print(f"{hours}:{minutes:02d}:{seconds:02d}")
