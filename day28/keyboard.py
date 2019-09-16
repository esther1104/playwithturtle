import turtle as t

t.setup(500, 500)
t.title("Turtle Keys")
t.shape("turtle")

def k1():
    t.fd(45)

def k2():
    t.lt(10)

def k3():
    t.rt(10)

def k4():
    t.back(45)

def k5():
    t.up()

def k6():
    t.down()

def help():
    print("화살표를 눌러서 이동해주세요.")

t.onkey(k1, "Up")
t.onkey(k2, "Left")
t.onkey(k3, "Right")
t.onkey(k4, "Down")
t.onkey(k5, "u")
t.onkey(k6, "d")
t.onkey(help, "h")
t.listen()
t.done()

print("콜백함수는 함수를 대신 호출해줌 잘 모르겠음 대충 알겠는데 설명할 정도론 모르겠음 바인딩은 내가 화살표 누르면 움직이는 것처럼 하는 거")