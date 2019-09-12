print("매개변수는 값이 정해져 있지 않는 것 같고 전달인자는 그 매개변수에 대입하는 값인 것 같다 그래서 값이 정해져 있고 넣을 때마다 그 값을 변경할 수 있음")

import turtle as t
t.speed(2)
def triangle(x):
    for i in range(3):
        t.fd(x)
        t.lt(120)

triangle(50)
triangle(150)
triangle(250)

t.done()