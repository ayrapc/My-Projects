import random
#rock beats scissors
#scissors beats paper
#paper beats rock
choices = ["rock" , "paper" , "scissors"]


computer_choice = random.randint(0,2)
#print(choices[computer_choice])
for index in range(len(choices)):
    print(index , choices[index])

user_choice = int(input("enter your choice: "))
print(choices[user_choice], choices[computer_choice])

#code to determine the winner
#code to keep score
