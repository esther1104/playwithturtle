import turtle as t
t.shape("turtle")

for x in range(1,6):
    t.fd(200)
    if x % 2 == 1:
        t.lt(135)
    else:
        t.rt(135)
t.done()
        