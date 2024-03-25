import turtle
from time import sleep

# initial setup
t = turtle.Turtle()
t.speed(10) # fastest speed is 10
turtle.tracer(False)

# change colour scheme
turtle.bgcolor("black")
t.color("white")

# config vars
hourhandlength = 40
minutehandlength = 100

def clear():
    t.clear()

def reset(thickness):
    t.setheading(90) # look north
    t.penup()
    t.goto(0,0) # move back to initial pos
    t.pendown()
    t.width(thickness)

def drawcircle():
    reset(10)
    t.right(90)
    t.penup()
    t.forward(minutehandlength)
    t.pendown()
    t.left(90)
    t.circle(100)

def drawhand(thickness, direction, distance):
    reset(thickness)
    t.right(direction) 
    t.forward(distance)
    t.goto(0,0) # move back to initial pos

def drawclock(hours, minutes):
    # clear screen
    clear()
    
    # draw stuff
    drawcircle()
    drawhand(4, hours*30, 40) # move 30 per hour
    drawhand(2, minutes*6, 100) # move 6 per minute

    # update screen
    turtle.update()

while True:
    for hours in range(0,12): 
        for minutes in range(0,60):
            drawclock(hours, minutes)
            sleep(0.2)

#t.screen.exitonclick() # end the program on screen click