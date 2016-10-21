import turtle
import random

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")

    sunil = turtle.Turtle()
    sunil.shape("turtle")
    sunil.color("orange")
    sunil.fillcolor("green")
    sunil.speed(30)
    for i in range(1,37):
        draw_square(sunil)
        sunil.right(10)

    nita = turtle.Turtle()
    nita.shape("classic")
    nita.color("pink")
    nita.speed(30)
    for i in range(1,25):
        nita.circle(20)
        nita.right(20)
       

    subash = turtle.Turtle()
    subash.shape("classic")
    subash.color("green")
    subash.speed(25)
    subash.forward(200)




    window.exitonclick()
draw_art()

