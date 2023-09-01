print("Program przedstawia kalkulatro wieku")
imie = input("Jak sie nazywasz?: \n")
age = int(input("Ile masz lat?: \n"))
decades = age // 10
years = age % 10
print("Hi! "+ imie)
print("You are "+ str(decades) + " decades and " + str(years) + " old")
