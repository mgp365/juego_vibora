from turtle import *
from random import randrange, choice
from freegames import square, vector
import random

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


# Regina Aguilar Garcia - A00841923 (cambios de color)
snake_color = random.choice(['blue', 'orange', 'purple', 'green', 'cyan'])
food_color = random.choice(['gray', 'brown', 'teal', 'lime', 'black'])

current_vel = 200 #Mariana Guerrero Pérez - A00840918 (velocidad)
def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)
    #Gianmarco Barboza Alvarado - A00843087
    if not inside(head,wall) or head in snake or wall in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
    #Gianmarco Barboza Alvarado - A00843087
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        wall.x = randrange(-15, 15) * 10
        wall.y = randrange(-15, 15) * 10
        current_vel = max(50, current_vel - 20) #aumentar velocidad
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)
    #Gianmarco Barboza Alvarado - A00843087    
    square(wall.x,wall.y,9, 'red')
    square(food.x, food.y, 9, food_color)
    update()
    #ontimer(move, v)
    ontimer(move, current_vel) #aumentar frames

#Cesar Tadeo Bernal Sauceda - A00841810
def move_food():
    "Move food randomly one step, staying inside boundaries."
    directions = [vector(10,0), vector(-10,0), vector(0,10), vector(0,-10)]
    move = choice(directions)
    new_food = food.copy()
    new_food.move(move)

    if inside(new_food):
        food.move(move)

    ontimer(move_food, 1500) 

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

move_food()
done()