import turtle as t

t.shape("turtle")
t.speed(1)

def go(distance, up = False):
    if(up == True):
        t.up()
    else:
        t.down()
    t.fd(distance)

go(30)
go(30, True)
go(30)
go(30, True)
go(30)

t.done()