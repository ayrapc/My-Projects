#What is the square root of 1024?
square_root = 1024 ** (1/2)
print("The square root of 1024 is" , square_root)

#What is the fourth root of 4096?
fourth_root = 4096 ** (1/4)
print("The 4th root of 4096 is" , fourth_root)

#What is the fifth root of 100000?
fifth_root = 100000 ** (1/5)
print("The 5th root of 100,000 is" , fifth_root)


#What is 5 to the 3rd power times 5 to the 2nd power? Is that equal to 5 to the 5th power or to 5 to the 6th power?
exponent_first = 5 ** 3 * 5 ** 2
print(exponent_first)
exponent_five = 5 ** (5)
exponent_six = 5 ** (6)
if exponent_first == exponent_five:
    print("Exponent_first is equal to Exponent_five")
else:
    print("Exponent_first is equal to Exponent_six")

#What is 2 to the 4th power time 2 to the 2nd power? Is that equal to 2 to the 6th power or 2 to the 8th power?
exponent_second = (2 ** (4)) * (2 ** (2))
print(exponent_second)
exponent_sixth = 2 ** (6)
exponent_eight = 2 ** (8)
if exponent_second == exponent_sixth:
    print("Exponent_second is equal to Exponent_sixth")
else:
    print("Exponent_second is equal to Exponent_eight")

# Q - Based on exercises 4 and 5, when we multiply two numbers that have the same base number, what do we do with the exponents?
# A - When we multiply two numbers with the same base and different exponents we add the exponents and keep the base the same


# Check the internet for the radius of each planet in the solar system. Create meaningfully named variables to store this data.
# Use the formula pi times radius squared to display the circumference of each planet. Use 3.14 for pi. Display your answers in context.
radius_mercury = 1516
circum_mercury = 2 * 3.14 * radius_mercury
print("The circumference of Mercury is" , circum_mercury, "miles")

radius_earth = 3958.8
circum_earth = 2 * 3.14 * radius_earth
print("The circumference of the Earth is" , circum_earth , "miles")

radius_venus = 3760
circum_venus = 2 * 3.14 * radius_venus
print("The circumference of Venus is" , circum_venus, "miles")

radius_mars = 2106
circum_mars = 2 * 3.14 * radius_mars
print("The circumference of Mars is" , circum_mars, "miles")

radius_neptune = 15299
circum_neptune = 2 * 3.14 * radius_neptune
print("The circumference of Neptune is" , circum_neptune, "miles")

radius_jupiter = 43441
circum_jupiter = 2 * 3.14 * radius_jupiter
print("The circumference of Jupiter is" , circum_jupiter, "miles")

radius_saturn = 36184
circum_saturn = 2 * 3.14 * radius_saturn
print("The circumference of Saturn is" , circum_saturn, "miles")

radius_uranus = 15759
circum_uranus = 2 * 3.14 * radius_uranus
print("The circumference of Uranus is" , circum_uranus, "miles")

#Create a variable to represent the money in your bank account;
#pick an initial balance. Use functional equivalents to demonstrate receiving your allowance of $20 for three weeks.
account_balance = 30
count = 0
while (count < 3):
    account_balance += 20
    print("My account balance is" , account_balance)
    count += 1

#Rolling down a hill on roller-skates, your speed doubles every second.
#If your speed is 1 at the top of the hill, what is your speed after 4 seconds. Use functional equivalents.
speed = 1
count = 0
while (count < 4):
    speed *= 2
    print("My speed is now" , speed)
    count += 1











          
