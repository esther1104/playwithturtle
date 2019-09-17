import turtle as t

t.setup(500, 500)
t.shape("turtle")

def goto_mouse_click_position(x, y):
    print("x:" + str(x) + ", y:" + str(y))
    t.goto(x, y)

def mouse_right_button_click(x, y):
    print("right button click - x:" +str(x) + ", y:" +str(y))

def mouse_wheel_push(x, y):
    print("wheel push - x:" + str(x) + ", y:" + str(y))

t.onscreenclick(goto_mouse_click_position)
t.onscreenclick(mouse_wheel_push, btn = 2)
t.onscreenclick(mouse_right_button_click, btn = 3)

t.done()

print("피곤해서 숙제 내일 함")