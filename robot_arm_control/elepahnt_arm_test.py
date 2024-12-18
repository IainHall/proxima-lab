
from pymycobot.mycobot import MyCobot
import time
print("hello")

mc = MyCobot('COM3', '115200')
out = mc.get_coords()
print(out)

# Gets the current angle of all joints
angles = mc.get_angles()
print(angles)

# Set 1 joint to move to 40 and speed to 20
for i in range(6):
    mc.send_angle(i+1, 0, 10)

    time.sleep(5)


angles = mc.get_angles()
print(angles)
