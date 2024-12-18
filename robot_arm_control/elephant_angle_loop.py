from pymycobot.mycobot import MyCobot
import time
import argparse
from datetime import datetime
import json
import os
import asyncio

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--angle',
                        help = "path to experiment configuration file",
                        required=False,
                        type=int,
                        default=0)
    parser.add_argument('--joint',
                        help = "path to save experiment data to, should be a folder",
                        required=False,
                        type=int,
                        default=6) 
    parser.add_argument('--save_path',
                        help = "path to save experiment data to, should be a folder",
                        required=False,
                        type=str,
                        default="./labels.json")    

    args = parser.parse_args()

    return args

async def change_angles(mc,joint,angle,speed = 20):
    # Gets the current angle of all joints

    print("angle ", angle)
    print("joint ", joint)
    # Set 1 joint to move to 40 and speed to 20

    mc.send_angle(joint, angle, speed)

    
async def save_data(save_path,data_out_list):
    
    with open(save_path,'w') as f:
        json.dump(data_out_list,f)



async def async_wait(length=5):
    
    await asyncio.sleep(length)

async def main():

    args = parse_args()

    angle = args.angle
    joint = args.joint
    save_path = args.save_path

    print("hello")

    

    if os.path.exists(save_path):
        print(f"editing pre-existing save file {save_path}")
        with open(save_path,"r") as f:
            data_out_list = json.load(f)
    else:
        print(f"No pre-existing save file {save_path}")
        data_out_list= []
        try:
            with open(save_path,'w') as f:
                json.dump(data_out_list,f)
        except Exception as e:
            print(f"unsuccesful in saving data to file {save_path}")
            raise(e)
        else:
            print(f"succesfully saved file {save_path}")
    
    mc = MyCobot('COM3', '115200')
    out = mc.get_coords()
    print(out)
    angle_range = [ang for ang in range(-175,180,5)]

    print("================== starting loop ===========================")
    for i_ang, angle in enumerate(angle_range):
        print("starting loop at ", time.strftime('%X'))
        task1 = asyncio.create_task(async_wait(length= 8))
        
        task2 = asyncio.create_task(change_angles(mc,joint,angle))
        task3 = asyncio.create_task(save_data(save_path,data_out_list))
        await task1
        await task2
        await task3
        print("finished asyncp at ", time.strftime('%X'))
        angles = mc.get_angles()
        print("end angles ", angles)
        pose =  mc.get_coords()
        out_dict= {"id": i_ang,
                    "angles": angles,
                    "cpose": pose
                    }
        print(out_dict)
        data_out_list.append(out_dict)
        print("finishing loop at ", time.strftime('%X'))

    #
    # Writing out data

    with open(save_path,'w') as f:
        json.dump(data_out_list,f)

asyncio.run(main())