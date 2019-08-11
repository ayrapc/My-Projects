#Exercise 1: Create a function that converts fahrenheit to celcius
def f_to_c (fahrenheit):
    celcius = fahrenheit - 32
    celcius /= 1.8
    return (celcius)

print(f_to_c(32))
print(f_to_c(212))

#Exercise 2: Create a function that calculates the circumference of a planet when the radius is given

def circumference (radius):
    circum = radius * 3.14 * 2
    return circum

radius_mercury = 1516
print("The circumference of Mercury is" , circumference(radius_mercury) , "miles")


radius_venus = 3760
print("The circumference of Venus is" , circumference(radius_venus) , "miles")



radius_mars = 2106
print("The circumference of Mars is" , circumference(radius_mars) , "miles")



radius_neptune = 15299
print("The circumference of Neptune is" , circumference(radius_neptune) , "miles")



radius_jupiter = 43441
print("The circumference of Jupiter is" , circumference(radius_jupiter) , "miles")



radius_saturn = 36184
print("The circumference of Saturn is" , circumference(radius_saturn) , "miles")


radius_uranus = 15759
print("The circumference of Uranus is" , circumference(radius_uranus) , "miles")



#Exercise 3: Create a function that calculates the Surface Area of a planet when it's radius is given

def surface_area(radius):
    sarea = 4* 3.14 * (radius ** 2)
    return sarea

radius_mercury = 1516
print("The surface area of Mercury is" , surface_area(radius_mercury) , "square miles")


radius_venus = 3760
print("The surface area  of Venus is" , surface_area (radius_venus) , "square miles")



radius_mars = 2106
print("The surface area of Mars is" , surface_area (radius_mars) , "square miles")



radius_neptune = 15299
print("The surface area of Neptune is" , surface_area (radius_neptune) , "square miles")



radius_jupiter = 43441
print("The surface area of Jupiter is" , surface_area (radius_jupiter) , "square miles")



radius_saturn = 36184
print("The surface area of Saturn is" , surface_area (radius_saturn) , "square miles")


radius_uranus = 15759
print("The surface area of Uranus is" , surface_area(radius_uranus) , "square miles")

#Exercise 4: Create a function that calculates the volume of a planet when the radius is given


def volume(radius):
    vol = 4/3 * 3.14 * (radius ** 3)
    return vol

radius_mercury = 1516
print("The volume of Mercury is" , volume(radius_mercury) , "cubic miles")


radius_venus = 3760
print("The volume of Venus is" , volume(radius_venus) , "cubic miles")



radius_mars = 2106
print("The volume of Mars is" , volume(radius_mars) , "cubic miles")



radius_neptune = 15299
print("The volume of Neptune is" , volume(radius_neptune) , "cubic miles")



radius_jupiter = 43441
print("The volume of Jupiter is" , volume(radius_jupiter) , "cubic miles")



radius_saturn = 36184
print("The volume of Saturn is" , volume(radius_saturn) , "cubic miles")


radius_uranus = 15759
print("The volume of Uranus is" , volume(radius_uranus) , "cubic miles")





