
from turtle import Turtle, Screen
import random

colors = ["green", "blue", "red", "purple"]
animal = "turtle"
size = 5
the_race_continue = True

# Set a screen and screen size
screen = Screen()
screen.setup(width=1000, height=800)

# Create a new objects
tim = Turtle()
jeff = Turtle()
monica = Turtle()
kate = Turtle()

turtles = [tim, jeff, monica, kate]

# For loop with counter, setting turtles attributes
for i, turtle in enumerate(turtles):
    turtle.color(colors[i])
    turtle.shape("turtle")
    turtle.turtlesize(5)


# Functions to get our turtles to the start
def tim_start():
    tim.penup()
    tim.backward(400)
    tim.left(90)
    tim.forward(300)
    tim.right(90)
    tim.pendown()


def jeff_start():
    jeff.penup()
    jeff.backward(400)
    jeff.left(90)
    jeff.forward(100)
    jeff.right(90)
    jeff.pendown()


def monica_start():
    monica.penup()
    monica.backward(400)
    monica.right(90)
    monica.forward(100)
    monica.left(90)
    monica.pendown()


def kate_start():
    kate.penup()
    kate.backward(400)
    kate.right(90)
    kate.forward(300)
    kate.left(90)
    kate.pendown()


def random_move(turtle):
    move = random.randint(10, 20)
    turtle.forward(move)


# def colision():

# Set our turtles on the start
tim_start()
jeff_start()
monica_start()
kate_start()

color = "default"
our_guess = screen.textinput("Color", "Chose which turtle is gonna win")


while the_race_continue:
    for turtle in turtles:
        random_move(turtle)

        # Set a collision if turtle will get in the end of the screen
        if turtle.xcor() > 500 - 100:

            # The winner is turtle who just arrive to the end of screen
            the_winner = turtle

            # if that turtle has the sam color that we guess
            if the_winner.color()[0] == our_guess:
                print("You had right!")

                # Wont continue with while loop
                the_race_continue = False

            else:
                print(f"The winner was {turtle.color()[0]}")

                # Wont continue with while loop
                the_race_continue = False

            # end for loop
            break

screen.exitonclick()
