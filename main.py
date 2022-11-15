# firstly it is important to import required modules so I imported important modules
import turtle
import time
import random

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

# I will write this in order to create the head of the sneake
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

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(-100, 250)
pen.write("Score : 0 High Score : 0", align="center",
          font=("arial", 22, "bold"))