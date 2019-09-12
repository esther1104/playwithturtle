import turtle as t
t.speed(2)
def rectangle(width):
    for i in range(4):
        t.fd(width)
        t.rt(90)
rectangle(100)
rectangle(200)
rectangle(300)
t.done()