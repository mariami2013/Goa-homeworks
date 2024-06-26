from turtle import *


#we want to paint a house
#step 1: drow a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("blue")
penup()
left(30)
forward(20)
left(90)
forward(20)
pendown()

forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)

penup()
right(90)
forward(120)
pendown()

forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)


exitonclick()