#Create a variable that represents your age.
#Create code to print out the number of decades that you’ve been alive along with the number of years until you turn the next decade.
#Test this concept with 4 different ages.

my_age = 13
my_decades = my_age // 10
print("I have lived for" , my_decades , "decades")
years_left = my_age % 10
print(years_left)
years_left = 10 - years_left
print("I have" , years_left , "years left until the next decade")


my_age = 22
my_decades = my_age // 10
print("I have lived for" , my_decades , "decades")
years_left = my_age % 10
print(years_left)
years_left = 10 - years_left
print("I have" , years_left , "years left until the next decade")



my_age = 38
my_decades = my_age // 10
print("I have lived for" , my_decades , "decades")
years_left = my_age % 10
print(years_left)
years_left = 10 - years_left
print("I have" , years_left , "years left until the next decade")


my_age = 69
my_decades = my_age // 10
print("I have lived for" , my_decades , "decades")
years_left = my_age % 10
print(years_left)
years_left = 10 - years_left
print("I have" , years_left , "years left until the next decade")

#Create a variable for each of your teachers from last year.
#The variable name should incorporate the subject and the value should be their name.



my_social_studies_teacher = ("Dr. Crowley")
my_math_teacher = ("Mrs. Landry")
my_english_teacher = ("Mr. Miller")
my_science_teacher = ("Mr. Foster")
my_non_fiction_writing_teacher = ("Mrs.Palic")

#If there are 37 players on your soccer team and each bus holds 15 players,
#tell me how many busses you’ll need and how many people will be on the last bus.

number_of_players = 37
number_of_players_per_bus = 15
number_of_buses = (number_of_players // number_of_players_per_bus) + 1
print("They will need" , number_of_buses , "buses")
number_of_players_left = number_of_players - (number_of_players_per_bus) * 2
print("Number of players left" , number_of_players_left , "players")

#What do I have to multiply 46 by to get 3772?

answer = 3772 / 46
print("The answer is" , answer)

#I multiply a number by 7, the answer is 497. What is the number?


number = 497 / 7
print("The answer is" , number)

#How many quarters are in $37.75?

money = 37.75
quarter = .25
quarters_in_money = money / quarter
print("The amount of quarters in $37.75 is" , quarters_in_money)

#If your pay rate is $8.50 and you work 37 hours in a week, what is your gross pay?

hours_in_a_week = 37
pay_rate = 8.50
gross_pay = hours_in_a_week * pay_rate
print("Your gross pay is", gross_pay)

#From the previous question: if you pay 23% in taxes, what is your net pay?
gross_pay = 314.50
tax_rate = .23
taxes_paid = gross_pay * tax_rate
print("The amount paid in taxes is $" , taxes_paid)
net_pay = gross_pay - taxes_paid
print("The net pay is $" , net_pay)

#From the previous question: if you pay $100 in rent every week, how much do you have left
#after getting paid this week?

rent = 100
amount_remaining = net_pay - rent
print("The amount remaining is $" , amount_remaining)

#If your take home pay is $187.24 for the week, you pay $120 in rent every week, your taxes are
#21%, and you worked 41 hours, what is your pay rate.

take_home_pay = 187.24
hours_worked = 41
tax_rate = .21
total_pay = take_home_pay / .72
print(total_pay)
pay_rate = total_pay / hours_worked
print("The pay rate is $" , pay_rate , "per hour")




