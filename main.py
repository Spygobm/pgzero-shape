import pgzrun
import random

WIDTH = 300
HEIGHT = 300

def draw():
    w = WIDTH
    h = HEIGHT - 200
    r = 255
    g = 0
    b = random.randint(63,255)
    for i in range(20):
        rectangle = Rect((0,0),(w,h))
        rectangle.center = 150,150
        screen.draw.rect(rectangle,(r,g,b))
        h += 10
        w -= 10
        r -= 10
        g += 10

pgzrun.go()