import turtle
import random
import time

main_screen = turtle.Screen()
main_screen.title('Classic Snake Game')
main_screen.setup(width=700, height=700)
main_screen.tracer(0)
turtle.bgcolor('light yellow')

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color('brown')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

score = 0
delay = 0.1

snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color("dark green")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'

snake_food = turtle.Turtle()
snake_food.speed(0)
snake_food.shape('circle')
snake_food.color('light blue')
snake_food.penup()
snake_food.goto(30, 30)

old_snake_food = []

high_score = turtle.Turtle()
high_score.speed(0)
high_score.color("black")
high_score.penup()
high_score.hideturtle()
high_score.goto(0, 300)
high_score.write("Score :", align="center", font=("Courier", 24, "bold"))


def snake_up():
    if snake.direction != "down":
        snake.direction = "up"


def snake_down():
    if snake.direction != "up":
        snake.direction = "down"


def snake_left():
    if snake.direction != "right":
        snake.direction = "left"


def snake_right():
    if snake.direction != "left":
        snake.direction = "right"


def snake_move():
    if snake.direction == "up":
        _y = snake.ycor()
        snake.sety(_y + 20)

    if snake.direction == "down":
        _y = snake.ycor()
        snake.sety(_y - 20)

    if snake.direction == "left":
        _x = snake.xcor()
        snake.setx(_x - 20)

    if snake.direction == "right":
        _x = snake.xcor()
        snake.setx(_x + 20)


main_screen.listen()
main_screen.onkeypress(snake_up, "Up")
main_screen.onkeypress(snake_down, "Down")
main_screen.onkeypress(snake_left, "Left")
main_screen.onkeypress(snake_right, "Right")


while True:
    main_screen.update()
    if snake.distance(snake_food) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        snake_food.goto(x, y)
        high_score.clear()
        score += 1
        high_score.write("Score:{}".format(score), align="center", font=("Courier", 24, "bold"))
        delay -= 0.001

        new_snake_food = turtle.Turtle()
        new_snake_food.speed(0)
        new_snake_food.shape('square')
        new_snake_food.color('light green')
        new_snake_food.penup()
        old_snake_food.append(new_snake_food)

    for index in range(len(old_snake_food) - 1, 0, -1):
        a = old_snake_food[index - 1].xcor()
        b = old_snake_food[index - 1].ycor()

        old_snake_food[index].goto(a, b)

    if len(old_snake_food) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_snake_food[0].goto(a, b)
    snake_move()

    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        main_screen.clear()
        main_screen.bgcolor('brown')
        high_score.goto(0, 0)
        high_score.write("   GAME OVER \n Your Score is {}".format(score), align="center", font=("Courier", 30, "bold"))

    for food in old_snake_food:
        if food.distance(snake) < 20:
            time.sleep(1)
            main_screen.clear()
            main_screen.bgcolor('brown')
            high_score.goto(0, 0)
            high_score.write("   GAME OVER \n Your Score is {}".format(score), align="center", font=("Courier", 30, "bold"))

    time.sleep(delay)
    turtle.Terminator()
