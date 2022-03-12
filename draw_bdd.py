import turtle

from bdd import*

major = input("请输入你的专业班级（例如：电气20-4）： ")
name = input("请输入中文姓名（例如：张三）： ")

n = len(major + name)
n = int(n)
n = n + 2

speed = input("请输入你希望的绘制速度，1慢，2快（输入数字）: ")
speed = int(speed)
if speed == 2:
    ret = 0
else:
    ret = 3

print("请稍等，正在为你画属于你的冰墩墩！")

turtle.setup(800, 600)
turtle.speed(ret)  # 速度
turtle.title("BingDunDun")

left_hand()
left_hand_in()
head()
left_ear()
left()
left_leg()
right_leg()
right_hand()
right()
right_ear()
right_hand_in()
left_ear_in()
right_hand_in2()
left_leg_in()
right_leg_in2()
right_eye_socket()
eyeball()
left_eye_socket()
eyeball2()
nose()
mouse()
rainbow_circle()
red_heart()
five_rings()
username(major, name)
name_heart(n)

print("绘制完成！")
turtle.hideturtle()
turtle.done()