
from pymycobot.mycobot import MyCobot

print("hello")

mc = MyCobot('COM3', '115200')
out = mc.get_coords()
print(out)