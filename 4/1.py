# 1. Készíts egy void függvényt, mely egy négyzetet rajzol. Használd fel egy olyan program elkészítéséhez, mely az 1.png ábrát hozza létre. Minden egyes négyzet legyen 20 egység. (Segítség: mire a program véget ér, a teknőc már elmozdul arról a helyről, ahová az utolsó négyzetet rajzolta.)

import turtle
from turtle import Screen, Turtle

ablak: Screen = turtle.Screen()
ablak.bgcolor("lightgreen")

drawer: Turtle = turtle.Turtle()
drawer.pensize(3)
drawer.color("pink3")


def negyzet_rajzolas(teknoc: Turtle, oldal: int):
    for i in range(4):
        teknoc.forward(oldal)
        teknoc.left(90)


def negyzetek_sorban(teknoc: Turtle, oldal: int, darab: int):
    for i in range(darab):
        teknoc.pendown()
        negyzet_rajzolas(teknoc, oldal)
        teknoc.penup()
        teknoc.forward(2 * oldal)


negyzetek_sorban(drawer, 20, 5)

ablak.mainloop()
