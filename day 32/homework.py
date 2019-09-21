import turtle as t

t.setup(1000, 1000)
t.shape("turtle")

t.pencolor("black")
t.pensize(5)

def drawRectangle(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.fd(width)
    t.lt(90)
    t.fd(height)
    t.lt(90)
    t.fd(width)
    t.lt(90)
    t.fd(height)
    t.lt(90)
    t.end_fill()

drawRectangle(300, 100, "red")

drawRectangle(200, 50, "yellow")

drawRectangle(100, 25, "blue")


