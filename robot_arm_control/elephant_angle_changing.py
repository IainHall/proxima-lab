from pymycobot.mycobot import MyCobot
import time
import argparse
from datetime import datetime
import json
import os

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


args = parse_args()

angle = args.angle
joint = args.joint
save_path = args.save_path

print("hello")

mc = MyCobot('COM3', '115200')
out = mc.get_coords()
print(out)

# Gets the current angle of all joints

print("angle ", angle)
print("joint ", joint)
# Set 1 joint to move to 40 and speed to 20

mc.send_angle(joint, angle, 20)

time.sleep(3)
angles = mc.get_angles()
print("end angles ", angles)
pose =  mc.get_coords()

#
# Writing out data
##

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
        
id = len(data_out_list)
#time_data = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
#print(f"writing out at {time_data}")
out_dict= {"id": id,
            "angles": angles,
            "cpose": pose
            }
data_out_list.append(out_dict)

with open(save_path,'w') as f:
    json.dump(data_out_list,f)