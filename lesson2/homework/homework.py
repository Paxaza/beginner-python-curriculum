# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lines.
x1 = input("First number: ")
y1 = input("Second number: ")
x = int(x1)
y = int(y1)
print("Quotient: ", (x / y))
print("Remainder: ", (x % y))


# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"
animal = input("What is your favorite animal? ")
color = input("What is your favorite color? ")
print("Okay, I will remember to get you a ", color, animal, " plush for your birthday!")


# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).
for i in range (0, 11):
    if (i % 2) == 0:
        print(i)

# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.
pushstr = input("How many pushups can you do? ")
push = int(pushstr)
print("That's impressive! I bet I couldn't do", (push*7), "push-ups in a week!")


# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)
for i in range (1, 7):
    print(i**2)