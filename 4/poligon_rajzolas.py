from turtle import Turtle

def sokszog_rajzolas(t: Turtle, n: int, sz: int):
    fok: int = 360 // n
    for i in range(n):
        t.forward(sz)
        t.left(fok)
