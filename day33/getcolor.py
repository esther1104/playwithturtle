import turtle as t

t.setup(500, 500)
t.shape("turtle")

t.pencolor("black")
t.pensize(5)

t.fillcolor("red")
t.begin_fill()

for x in range(2):
    t.fd(60)
    t.lt(90)
t.end_fill()

def print_color(x, y):
    color = get_pixel_color(x, y)
    print(color)

def get_pixel_color(x, y):
    y = -y
    canvas = t.getcanvas()
    ids = canvas.find_overlapping(x, y ,x ,y)
    if ids:
        index = ids[-1]
        color = canvas.itemcget(index, "fill")
        if color:
            return color
    return "white"

t.onscreenclick(print_color)
t.done()