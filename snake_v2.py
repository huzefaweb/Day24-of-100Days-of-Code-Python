from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # set screen to on/off and set delay for update drawings

# -------- snake body -----------
snake = Snake()
# -----------------------------------------------------

# ------ food collection -------
food = Food()
# ------------------------------

# ------ Score Board Track --------------
score = Scoreboard()
# -----------------------------------------

# ---------- Snake control ----------------
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# -----------------------------------------

game_is_on = True
while game_is_on:
    screen.update()  # use to update the screen once a complete action is performed
    time.sleep(0.1)  # reduces the speed of movement
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect Collision with wall
    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
        score.reset()
        snake.reset()

    # Detect Collision with tail
    for segment in snake.segments[1:]:  # using slicing this would check whole list except the first element
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
