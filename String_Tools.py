my_name = "Ayra Chemitiganti"
for character in my_name:
    print(character)

def print_vowels(string_in):
    vowels = "aeiouAEIOU"
    for character in string_in:
        if character in vowels:
            print(character)


print_vowels(my_name)

def multiply(x, y):
    print(x*y)

multiply(2, 7)

def subtract(x, y):
    print(x-y)

subtract(22, 16)

def add(x, y):
    print(x+y)

add(33, 22)

def divide(x, y):
    print(x/y)

divide(45, 5)

def minutes_to_seconds(minutes):
    print(minutes*60)

minutes_to_seconds(4)
minutes_to_seconds(10)

def seconds_to_minutes(seconds):
    print(seconds/60)

seconds_to_minutes(605)
seconds_to_minutes(360)

def minutes_to_hours(minutes):
    print(minutes/60)

minutes_to_hours(45)

def hours_to_minutes(hours):
    print(hours*60)

hours_to_minutes(2)

def backwards_printer(forwards_string):
    backwards = ""
    for index in range(len(forwards_string)-1, -1, -1):
        backwards = backwards + forwards_string[index]
    print(backwards)

backwards_printer("I like cats")
