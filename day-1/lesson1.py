
from turtle import *

shape("turtle")
#we want to paint house

#step one draw a aquare 
width(4)
color("black")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square 

#drawing a door

begin_fill()
forward(70)
color("silver")
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("gray")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing   N1  windows 

begin_fill()

color("black")
left(30)
forward(50)

color("teal")
begin_fill()

forward(50)
left(90)

forward(50)
left(90)

forward(50)
 
left(90)
forward(50)
end_fill() 
left(90)
forward(50)
right(180)
forward(50)
#drawing  N2 windows 

color("black")
forward(50)
right(90)
forward(200)
right(90)
forward(50)
color("teal")
begin_fill()

right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

end_fill()

#drawing a grass 
begin_fill()
right(90)

color("black")
forward(100)

color("green")
forward(100)
right(90)
forward(540)
right(90)
forward(100)
right(90)
forward(540)
end_fill()










exitonclick()