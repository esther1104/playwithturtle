import turtle as t

t.setup(500, 500)
t.shape("turtle")

def init():
    colors = ["Red", "Green", "blue", "Yellow", "Black", "white", "Brown", "pink", "gold", "Cyan"]
    t.pensize(10)

    t.up()
    t.goto(-240, 240)
    t.down()
    drawRectangle(480, 480, "white")

    for x in range(0, 10):
        drawRectangle(48, 48, colors[x])
        t.fd(48)

    t.up()
    t.pencolor("black")
    t.goto(0, 0)
    t.down()

def drawRectangle(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for x in range(2):
        t.fd(width)
        t.right(90)
        t.fd(height)
        t.right(90)
    t.end_fill()

init()

turtle.done()