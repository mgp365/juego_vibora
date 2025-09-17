from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


current_vel = 200 #inicializar variable de vel
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    global current_vel

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        current_vel = max(50, current_vel - 20) #aumentar velocidad
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    #ontimer(move, v)
    ontimer(move, current_vel)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
velocity = 10
onkey(lambda: change(velocity, 0), 'Right')
onkey(lambda: change(-velocity, 0), 'Left')
onkey(lambda: change(0, velocity), 'Up')
onkey(lambda: change(0, -velocity), 'Down')
move()

done()