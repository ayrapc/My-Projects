import turtle

#make a turtle called sheldon
sheldon = turtle.Turtle()


##for index in range(4):
##    sheldon.forward(100)
##    sheldon.right(90)
##
##for index in range(3):
##    sheldon.forward(200)
##    sheldon.right(120)
##
##for index in range(5):
##    sheldon.forward(150)
##    sheldon.right(72)

def draw_shape(num_sides, side_length):
    sum_of_angles = (num_sides - 2) * 180
    interior_angle = sum_of_angles / num_sides
    angle = 180 - interior_angle
    
    for index in range(num_sides):
        sheldon.forward(side_length)
        sheldon.right(angle)

draw_shape(4, 100)
draw_shape(3, 200)
draw_shape(5, 150)
draw_shape(7, 75)

##sheldon.forward(100)
##sheldon.right(90)
##sheldon.forward(100)
##sheldon.right(90)
##sheldon.forward(100)
##sheldon.right(90)
##sheldon.forward(100)
##
##sheldon.right(60)
##sheldon.forward(60)
##sheldon.right(60)
##sheldon.forward(60)
##
##sheldon.forward(200)
##sheldon.right(72)
##sheldon.forward(200)
##sheldon.right(72)
##sheldon.forward(200)
##sheldon.right(72)
##sheldon.forward(200)
##sheldon.right(72)
##sheldon.forward(200)



