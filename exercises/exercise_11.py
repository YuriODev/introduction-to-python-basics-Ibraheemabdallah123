# Exercise 11
# Your solution comes here
s = int(input("enter an amount of money"))
note500 = s // 500
note100 = (s % 500) // 100
note10 = ((s % 500) % 100) // 10
note5 = (((s % 500) % 100) % 10) // 5
note2 = ((((s % 500) % 100) % 10) % 5) // 2
note1 = (((((s % 500) % 100) % 10) % 5) % 2) // 1
print(note500,"500s", note100,"100s", note10,"10s", note5,"5s", note2,"2s", note1,"1s")