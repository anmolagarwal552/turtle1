import turtle

#Create the turtle.
tut = turtle.Turtle()

#Configure the Turtle.
tut.color('green')
tut.width(3)
tut.speed(1)
tut.shape('turtle')

#move the turtle on the screen.
tut.forward(100)
tut.left(90)
tut.penup()
tut.forward(100)
tut.pendown()
tut.right(90)
tut.forward(100)

#for preventing the screen from closing.
turtle.listen()
turtle.mainloop()
