from turtle import *
from random import randrange, choice
from freegames import square, vector
import random

# Estado inicial
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
wall = vector(0, 10)

# Regina Aguilar Garcia - A00841923 (cambios de color aleatorios para serpiente y comida)
snake_color = random.choice(['blue', 'orange', 'purple', 'green', 'cyan'])
food_color = random.choice(['gray', 'brown', 'teal', 'lime', 'black'])

# Mariana Guerrero Pérez - A00840918 (velocidad inicial configurable)
current_vel = 200  

def change(x, y):
    """Cambia la dirección de la serpiente."""
    aim.x = x
    aim.y = y

def inside(head):
    """Devuelve True si la cabeza está dentro de los límites."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    """Mueve la serpiente un segmento hacia adelante."""
    global current_vel  # Mariana Guerrero Pérez - necesario para modificar la velocidad global

    head = snake[-1].copy()
    head.move(aim)

    # Gianmarco Barboza Alvarado - A00843087 (detección de colisiones con bordes, cuerpo y pared)
    if not inside(head) or head in snake or head == wall:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    # Gianmarco Barboza Alvarado - A00843087 (al comer se genera nueva comida y pared aleatoria)
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        wall.x = randrange(-15, 15) * 10
        wall.y = randrange(-15, 15) * 10
        current_vel = max(50, current_vel - 20)  # Mariana Guerrero Pérez - aumenta velocidad progresiva
    else:
        snake.pop(0)

    clear()

    # Regina Aguilar Garcia - A00841923 (serpiente dibujada con color aleatorio)
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    # Gianmarco Barboza Alvarado - A00843087 (pared roja en posición aleatoria)
    square(wall.x, wall.y, 9, 'red')

    # Regina Aguilar Garcia - A00841923 (comida dibujada con color aleatorio)
    square(food.x, food.y, 9, food_color)

    update()
    ontimer(move, current_vel)

# Cesar Tadeo Bernal Sauceda - A00841810 (movimiento aleatorio de la comida dentro de los límites)
def move_food():
    """Mueve la comida un paso aleatorio dentro de los límites."""
    directions = [vector(10,0), vector(-10,0), vector(0,10), vector(0,-10)]
    step = choice(directions)
    new_food = food.copy()
    new_food.move(step)

    if inside(new_food):
        food.move(step)

    ontimer(move_food, 1500) 

# Configuración de la ventana
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
