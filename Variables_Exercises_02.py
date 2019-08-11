#Exercise 1
#1) Write code that has a suitable variable representing the money in your bank account. Assume that you have $20 in your account.
#2) You receive an allowance of $10 dollars and a birthday check for $50. Record each of these changes to your account.
#3) You buy a pair of sandals for $17.85. Record this change.
#4) You clean out under your bed and find 17 quarters, 8 dimes, and 62 pennies. Deposit this change
#into your account.
#5) Show how much is in your account at the beginning and after each change.
my_money = 20.00
my_money = my_money + 10.00 + 50.00
print("I have $" , my_money)
my_money = my_money - 17.85
print("I have $" , my_money)
my_money = my_money + 5.67
print("I have $" , my_money)


print("End of Exercise 1")

#Exercise 2
#Exercises: (Use the above example to do these problems)
#1) There are 3 students in the class and 27 apples. If the apples are divided equally among the students, how many does each student get?
#2) There are 5 students in the class and 10 oranges. If the oranges are divided equally among the students, how many does each student get?
#3) Judy wants to buy enough boxes to store all her markers. Each box can hold 12 markers. If she has 72 markers, how many boxes does she need?
apples = 27
students = 3
apples_divided = apples / students
print(apples_divided , "apples per student")

oranges = 10
students = 5
oranges_divided = oranges / students
print(oranges_divided , "oranges per student")

markers = 72
markers_per_box = 12
boxes = markers / markers_per_box
print(boxes , "boxes of markers, 12 markers each")

print("End of Exercise 2")



#Exercise 3
#Exercises:
#1) There are 3 students in the class and 31 apples. If the apples are divided equally among the students, how many does each student get, and how many are left over?
#2) There are 5 students in the class and 12 oranges. If the oranges are divided equally among the students, how many does each student get, and how many are left over?
#3) Judy wants to buy enough boxes to store all her markers. Each box can hold 12 markers. If she has 76 markers, how many boxes does she need, and how many are in the last box?
students = 3
apples = 31
apples_divided = apples // students
print(apples_divided , "apples per student")
apples_remaining = apples % students
print(apples_remaining , "apples left over")

students = 5
oranges = 12
oranges_divided = oranges // students
print(oranges_divided , "oranges per student")
oranges_remaining = oranges % students
print(oranges_remaining , "oranges left over")

markers = 76
markers_per_box = 12
boxes = markers // markers_per_box
print(boxes , "boxes of markers, 12 markers each")
markers_remaining = markers % markers_per_box
print(markers_remaining , "markers left over")

print("End of Exercise 3")
