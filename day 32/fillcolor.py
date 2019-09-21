import turtle as t

t.setup(500, 500)
t.shape("turtle")

t.pencolor("black")
t.pensize(5)

t.fillcolor("red")
t.begin_fill()
for x in range(4):
    t.forward(60)
    t.left(90)
t.end_fill()

t.done()