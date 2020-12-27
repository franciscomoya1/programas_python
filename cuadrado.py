import turtle

window = turtle.Screen()
flecha = turtle.Turtle()

def arriba():
   flecha.setheading(90)
   flecha.forward(100)

def derecha():
   flecha.setheading(0)
   flecha.forward(100)

def abajo():
   flecha.setheading(270)
   flecha.forward(100)

def izquierda():
   flecha.setheading(180)
   flecha.forward(100)


window.onkeypress(arriba, "Up")
window.onkeypress(derecha, "Right")
window.onkeypress(abajo, "Down")
window.onkeypress(izquierda, "Left")

window.listen()

turtle.mainloop()