# Problem 1
# Ask the user for their age.
# Calculate and print how many decades old they are, rounded to the nearest whole number.
age_i = input ("How old are you? ")
age = int(age_i)
decades = (age // 10)
print("Ah so you're ", str(age) + ". That's around", str(decades) + " decades!")
if decades <=2:
    print("Be safe. You still have a long life to live.")
    if decades >=6:
        print("You've hopefully lived a fufilling life so far. Continue to enjoy the freedom that comes with old age.")
else:
    print("Continue living life. No matter what challenges you face. You can do hard things!")


# Problem 2
# Ask the user to enter a number.
# Print the result of multiplying that number by 5.
imp_number = input ("Now, enter a number. Any number... ")
nwnum = int(imp_number)
numfnl = (nwnum * 5)
print("Ah... your result appears to be", str(numfnl) + ".")


# Problem 3
# Use a for loop to print "I will learn Python!" 3 times.
pyth = str("I will learn Python")
for i in range (3):
    print(pyth)


# Problem 4
# Ask the user for their name and age.
# Print their name and how old they will be one year in a single sentence.
name = input("What is your name? ")
agei = input("How old are you? ")
age = int(agei)
print("So if what you're saying is correct, your name is", str(name) + ", and you are", str(age) + " years old?")


# Problem 5
# Use a for loop to print the numbers from 2 to 8, one per line.
for i in range (2,8):
    print(i)
