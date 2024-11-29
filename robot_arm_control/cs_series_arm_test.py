from robot import Robot

#from robot import Robot
#help(robot)


warehouse_bot = Robot("192.168.0.1")


# Connect to the robot
connection, message = warehouse_bot.connect()
print(message)


'''
if connection:
    # Accessing the value of System Variable B at address 1
    _, result = warehouse_bot.getVariable("SysVarB", 1)
    print("Value of SysVarB at addr 1: ", result)

    # Disconnection the robot
    result, message = warehouse_bot.disconnect()
    print(message)

print("hello")
'''