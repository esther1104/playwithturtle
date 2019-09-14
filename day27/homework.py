import turtle as t
t.shape("turtle")
t.speed(1)
y = 50

for x in range(5):
    t.circle(50)
    t.up()
    t.goto(y,0)
    t.down()
    y = y + 50

t.done()