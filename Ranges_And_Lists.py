Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> for index in range(10):
	print(index)

	
0
1
2
3
4
5
6
7
8
9
>>> 
>>> for index in range(11)
SyntaxError: invalid syntax
>>> for index in range(0,10):
	print(index)

	
0
1
2
3
4
5
6
7
8
9
>>> for index in range(-5,6):
	print(index)

	
-5
-4
-3
-2
-1
0
1
2
3
4
5
>>> for index in range(-20,7)
SyntaxError: invalid syntax
>>> for index in range(-20,7):
	print(index)

	
-20
-19
-18
-17
-16
-15
-14
-13
-12
-11
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
0
1
2
3
4
5
6
>>> for index in range(-20,7,2):
	print(index)

	
-20
-18
-16
-14
-12
-10
-8
-6
-4
-2
0
2
4
6
>>> for index in range(10,-1):
	print(index)

	
>>> 
>>> for index in range(10,-1,-1):
	print(index)

	
10
9
8
7
6
5
4
3
2
1
0
>>> for index in range(5,0):
	print(index)

	
>>> for index in range(5,0,-1):
	print(index)

	
5
4
3
2
1
>>> for index in range(20,-1,2):
	print(index)

	
>>> for index in range(20,-1,-2):
	print(index)

	
20
18
16
14
12
10
8
6
4
2
0
>>> for index in range(1,9,4):
	print(index)

	
1
5
>>> for index in range(1,10,4):
	print(index)

	
1
5
9
>>> for index in range(1,23,10):
	print(index)

	
1
11
21
>>> my_family = ["Vamsi" , "Neha" , "Ayra" , "Kabir"]
>>> print(my_family)
['Vamsi', 'Neha', 'Ayra', 'Kabir']
>>> for name in my_family:
	print(name)

	
Vamsi
Neha
Ayra
Kabir
>>> for name in my_family:
	print(name , "is in my family")

	
Vamsi is in my family
Neha is in my family
Ayra is in my family
Kabir is in my family
>>> planets = ["Mercury" , "Venus" , "Earth" , "Mars" , "Jupiter" , "Saturn" , "Uranus" , "Neptune"]
>>> print(planets , "is in our solar system")
['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'] is in our solar system

>>> for planet in planets:
	print(planet , "is in our solar system")

	
Mercury is in our solar system
Venus is in our solar system
Earth is in our solar system
Mars is in our solar system
Jupiter is in our solar system
Saturn is in our solar system
Uranus is in our solar system
Neptune is in our solar system
>>> my_favorite_foods = ["popcorn" , "cotton candy grapes" , "waffles"]
>>> for food in my_favorite_foods:
	print(food , "is one of my favorite foods")

	
popcorn is one of my favorite foods
cotton candy grapes is one of my favorite foods
waffles is one of my favorite foods
>>> social_media = ["Instagram" , "Snapchat"]
>>> for media in social_media:
	print("I use" , media)

	
I use Instagram
I use Snapchat
>>> pet_names = ["Cinna" , "Cashmere"]
>>> for pet in pet_names:
	print("I have a pet named" , pet_names)

	
I have a pet named ['Cinna', 'Cashmere']
I have a pet named ['Cinna', 'Cashmere']
>>> for pet in pet_names:
	print("I have a pet named" , pet)

	
I have a pet named Cinna
I have a pet named Cashmere
>>> len(social_media)
2
>>> 
>>> len(my_favorite_foods)
3
>>> len(my_family)
4
>>> my_family_ages = [43 , 43 , 5 , 13]
>>> average_age = 0
>>> for age in my_family_ages:
	average_age += age

	
>>> print(average_age)
104
>>> average_age /= len(my_family_ages)
>>> print(average_age)
26.0
>>> 
