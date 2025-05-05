import turtle
import random
screen = turtle.Screen()
screen.screensize( 500,  500)
t = turtle.Turtle()
screen.bgcolor('tan')
t.hideturtle()

t.penup()
t.goto(0, 100)
t.pendown()
t.write("Turtle", font=("arial", 30, "bold"), align="center")

t.penup()
t.goto(0, -100)
t.pendown()
t.write("Presentation", font=("arial", 30, "bold"), align="center")

slide = input('Press Enter to Continue ')
t.clear()

t.penup()
t.goto(0, 200)
t.pendown()
t.write("Favorite Foods", font=("arial", 30, "bold"), align="center")
screen.bgcolor('dodgerblue')

t.penup()
t.goto(-200, 0)
t.pendown()
screen.addshape('steak.gif')
t.shape('steak.gif')
t.stamp()
t.shape('classic')

t.penup()
t.goto(0, 0)
t.pendown()
screen.addshape('chicken.gif')
t.shape('chicken.gif')
t.stamp()
t.shape('classic')

slide = input('Press Enter to Continue ')
t.clear()
t.penup()
t.goto(0, 200)
t.pendown()
t.write("Hobbies", font=("arial", 30, "bold"), align="center")
screen.bgcolor('red')


slide = input('Press Enter to Continue ')
t.clear()
t.penup()
t.goto(0, 200)
t.pendown()
t.write("Favorite Movie", font=("arial", 30, "bold"), align="center")
screen.bgcolor('green')

slide = input('Press Enter to Continue ')
t.clear()
t.penup()
t.goto(0, 200)
t.pendown()
t.write("Favorite Sport", font=("arial", 30, "bold"), align="center")
screen.bgcolor('aquamarine')

slide = input('Press Enter to Continue ')

screen.bgcolor('white')

t.clear()
t.penup()
t.goto(0, 100)
t.pendown()
t.write("The End", font=("arial", 40, "bold"), align="center")































turtle.done()