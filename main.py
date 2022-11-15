# firstly it is important to import required modules so I imported important modules
import turtle
import time
import random

# this lines are for the speed and the scores of the snakes movements and eats
delay = 0.11
score = 0
high_score = 0

# Firstly, it leads to get create a window screen
win = turtle.Screen()
win.title("Hungry Snake Game")
win.bgcolor("white")
# the windows screen's width and height can be put regarding user's choice
win.setup(width=700, height=600)
win.tracer(0)

# I will write this in order to create the head of the sneak
head = turtle.Turtle()
head.shape("circle")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# it is for the food that is in the game snake will get longer
food = turtle.Turtle()
colors = random.choice(['black', 'yellow', 'red'])
food.shape("circle")
food.speed(0)
food.color(colors)
food.penup()
food.goto(0, 100)

# I will write the lines special for the text that mentions above the project to show the scores
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(-100, 250)
pen.write("Score : 0 High Score : 0", align="center",
          font=("arial", 22, "bold"))

# it is for assigning the 4 types of key directions
# it is for the snake going up
def group():
    if head.direction != "down":
        head.direction = "up"

# it is for the snake going down
def godown():
    if head.direction != "up":
        head.direction = "down"

# it is for the snake going left
def goleft():
    if head.direction != "right":
        head.direction = "left"


# it is for the snake going right
def goright():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


#it is the calling keys to move snake
win.listen()
win.onkeypress(group, "w")
win.onkeypress(godown, "s")
win.onkeypress(goleft, "a")
win.onkeypress(goright, "d")