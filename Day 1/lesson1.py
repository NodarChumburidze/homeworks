from turtle import *

#we want to paint a house

#step 1:
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
#end of scuare

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

#drawing a window

penup()
goto(200, 100)
pendown()
color("green")   
begin_fill()
left(-60)
forward(50)
right(90)
forward(60)
right(90)
forward(50)
end_fill()

penup()
goto(0, 100)
begin_fill()
pendown()
forward(50)
left(90)
forward(60)
left(90)
forward(50)
end_fill()

exitonclick()
