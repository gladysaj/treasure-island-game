# if /else conditional 
water_level = 50    
if water_level > 80:
    print("Drain water")
else:
    print("Continue")

# Rollercoaster ride
print("Welcome to the Chipmunk's rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("Enjoy the ride!")
else:
    print("Sorry, you have to grow taller before you can ride.")    

# Conditional operators
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# == equal to
# != not equal to

# Modulo operator % modulo operator returns the remainder of a division
10 % 5 # equals to 0

# Odd or even number
check_number = int(input("Write your number"))
print(check_number)

if check_number % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")

# Nested if statements
print("Welcome to the Chipmunk's rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("Enjoy the ride!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    elif age < 22:
        print("Please pay $8")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride.")   


# BMI calculator
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("overweight")

# Multiple if statements
print("Welcome to the Chipmunk's rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("Enjoy the ride!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5")
    elif age <= 18:
        bill = 7
        print("Please pay $7")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Please pay $12")

    wants_photo = input("Do you want a photo? Y or N ")
    if wants_photo == "Y":
        bill += 3

        print(f"Your total bill is ${bill}")    
else:
    print("Sorry, you have to grow taller before you can ride.")   

# Pizza order practice
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their pizza size
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
        bill += 25
else:
    print("Wrong answer")

# todo: how much to add to their bill based on their pepperoni choice
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# todo: how much to add to their bill based on their cheese choice
if extra_cheese == "Y":
        bill += 1

print(f"Your final bill is ${bill}")

# Logical operators
# and (If one is false, the whole statement is false)
# or (If one is true, the whole statement is true)
# not (If the statement is true, it will return false)
