# Refer to your exercises above. Create a variable that has an integer of your choosing in it. If the integer is even print it and a string stating that it’s even.
# If not, print it and a string stating that it’s odd.

number = 2256
if(number % 2 == 0):
    print("Even")
else:
    print("Odd")


# Create a variable to store the hour of day. If the hour is before noon,
# print good morning.
# Otherwise, print good afternoon.
    
hour_of_day = 16
if(hour_of_day <= 12):
    print("Good Morning")
else:
    print("Good Afternoon")

#This is a simplification. A leap year is a year that is divisible by 4 with no remainder. Create a variable that stores
# the year. Create an if else statement that prints if it’s a leap year or not.

leap_year = 2005
if(leap_year % 4 == 0):
    print("This is a leapyear")
else:
    print("This is not a leapyear")




