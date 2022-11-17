# Firstly I wrote import required modules to run my project
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Secondly, I used the screen setup to creating a window screen
winscreen = turtle.Screen()
winscreen.title("Snake Game")
winscreen.bgcolor("blue")
# it is getting the width and height can be put as user's choice
winscreen.setup(width=700, height=600)
winscreen.tracer(0)

# then I wrote the code to create the head of the snake
head = turtle.Turtle()
head.shape("circle")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# and it is for the creating the food in the game that snake eats it and get longer
food = turtle.Turtle()
colors = random.choice(['red', 'black'])
food.speed(0)
food.shape("circle")
food.color(colors)
food.penup()
food.goto(0, 100)

# then i wrote this in order to get the text that shows the score of the user in a project mentions above the win screen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score : 0", align="center",
          font=("arial", 22, "bold"))


# these lines are importat to move the snake with 4 key directions
def group():
    if head.direction != "down":
        head.direction = "up"

# it is for going down
def godown():
    if head.direction != "up":
        head.direction = "down"

#it is moving to left
def goleft():
    if head.direction != "right":
        head.direction = "left"

# it is for moving to right
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

# these are calling the moving directions on the keyboard
winscreen.listen()
winscreen.onkeypress(group, "w")
winscreen.onkeypress(godown, "s")
winscreen.onkeypress(goleft, "a")
winscreen.onkeypress(goright, "d")


# From these line getting some segments for our project
segments = []

# it is the special part the calling Main Gameplay to control all objects of the project
maingameplay = True
while maingameplay:
    winscreen.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(['red', 'blue'])
        head.shape('circle')
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # here for adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 5
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("arial", 22, "bold"))
    # Checking for head collisions with body segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue'])
            head.shape('circle')
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("arial", 22, "bold"))
    time.sleep(delay)

winscreen.mainloop()