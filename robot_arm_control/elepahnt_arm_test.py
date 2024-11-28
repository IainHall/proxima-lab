
from pymycobot.mycobot import MyCobot

print("hello")

mc = MyCobot('COM5', '115200')
out = mc.get_coords()
print(out)