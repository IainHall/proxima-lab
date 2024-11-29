

import argparse
from datetime import datetime
import yaml
import os
import json
from pymycobot.mycobot import MyCobot

from robot import Robot

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--ex_cfg_path',
                        help = "path to experiment configuration file",
                        required=False,
                        type=str)
    parser.add_argument('--save_path',
                        help = "path to save experiment data to, should be a folder",
                        required=False,
                        type=str)   

    args = parser.parse_args()

    return args



def main():

    print("Starting robot combined control script")
    


    ##
    # Parsing args, config, and checking save path
    ##
    args = parse_args()

    print(args)


    config_path = args.config_path
    save_path = args.save_path


    with open(config_path,'r') as f:
        config = yaml.safe_load(f)



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

    ##
    # Connnecting to the robot arms
    ##      

    print("connecting to object arm")
    try:
        obj_arm = MyCobot('COM3', '115200')
    except:
        raise ValueError("invalid object arm address")
    
    obj_arm_data = obj_arm.get_coords()
    print("object arm pose coordinates")
    print("connecting to camera arm at ip address:", config['cam']['ip_address'])
    try:
        cam_arm = Robot(config['cam']['ip_address'])# Connect to the robot
        connection, message = cam_arm.connect()
        print(message)
    except NameError:
        raise Exception(NameError, " Warning, check that you have the Camera arm library installed correctly")
    except Exception as e:
        print(f"unexpected {e}")


    if connection:
        # Accessing the value of System Variable B at address 1
        _, cam_arm_data = cam_arm.getVariable("SysVarB", 1)
        print("Value of SysVarB at addr 1: ", result)

        # Disconnection the robot
        result, message = cam_arm.disconnect()
        print(message)
    else:
        print("Warning, unsuccseful in connecting to camera arm")


    ##
    # Writing out data
    ##
    time_data = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    print(f"writing out at {time_data}")
    out_dict= {"id": id,
                "obj_arm": obj_arm_data,
               "cam_arm": cam_arm_data,
               "time_data": time_data}
    data_out_list.append(out_dict)
    
    with open(save_path,'w') as f:
        json.dump(data_out_list,f)

if __name__ == '__main__': 

    main()

