import turtle

win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("green")
win.setup(width=700, height=500)
win.tracer(0)

# Player 1
player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.color("red")
player_1.penup()
player_1.goto(-320, 0)

# Player 2
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.shapesize(stretch_wid=5, stretch_len=1)
player_2.color("red")
player_2.penup()
player_2.goto(320, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.1

# Move Players
def player_1_up():
    y = player_1.ycor()
    y +=25
    player_1.sety(y)
def player_1_down():
    y = player_1.ycor()
    y -=25
    player_1.sety(y)

def player_2_up():
    y = player_2.ycor()
    y +=25
    player_2.sety(y)
def player_2_down():
    y = player_2.ycor()
    y -=25
    player_2.sety(y)

# Introducing the keys
win.listen()
win.onkeypress(player_1_up, "w")
win.onkeypress(player_1_down, "s")

win.onkeypress(player_2_up, "Up")
win.onkeypress(player_2_down, "Down")

# Main loop
while True:
    win.update()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  
    ball.sety(ball.ycor() + ball.dy)
    # The wall colider
    if ball.ycor() > 250:
        ball.sety(250)
        ball.dy *= -1
    if ball.ycor() < -250:
        ball.sety(-250)
        ball.dy *= -1
    if ball.xcor() < -350:
        ball.setx(-350)
        ball.dx *= -1
    if ball.xcor() > 350:
        ball.setx(350)
        ball.dx *= -1
    # Ball & Players collisions
    if (ball.xcor() < 290 and ball.xcor() > 330) and (ball.ycor() < player_1.ycor() + 50 and ball.ycor() > player_1.ycor() -50):
        ball.setx(290)
        ball.dx *= -1
    if (ball.xcor() < -290 and ball.xcor() > -330) and (ball.ycor() < player_2.ycor() + 50 and ball.ycor() > player_2.ycor() -50):
        ball.setx(290)
        ball.dx *= -1


