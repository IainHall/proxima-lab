

json_path = "..\labels.json";
fixed_data_path = "181224_setup.xlsx";

fixed_data  = readtable(fixed_data_path,"ReadRowNames",true)

fid = fopen(json_path); 
raw = fread(fid,inf); 
str = char(raw'); 
fclose(fid); 
time_data = jsondecode(str);


field_list = {"obj_to_e2","e2_to_arm2","arm2_to_rail","rail_to_tent","tent_to_arm1","arm1_to_e1", "e1_to_cam"};
entry_name = "effector2_to_object";
transform.obj_to_e2 = get_pose_matrix(table2array(fixed_data(entry_name,["x","y","z"])),table2array(fixed_data(entry_name,["rotx","roty","rotz"])),-1);
transform.e2_to_arm2 = [];
entry_name = "rail_to_arm2";
transform.arm2_to_rail = get_pose_matrix(table2array(fixed_data(entry_name,["x","y","z"])),table2array(fixed_data(entry_name,["rotx","roty","rotz"])),-1);
entry_name = "tent_to_rail";
transform.rail_to_tent = get_pose_matrix(table2array(fixed_data(entry_name,["x","y","z"])),table2array(fixed_data(entry_name,["rotx","roty","rotz"])),-1);
entry_name = "tent_to_arm1";
transform.tent_to_arm1 = get_pose_matrix(table2array(fixed_data(entry_name,["x","y","z"])),table2array(fixed_data(entry_name,["rotx","roty","rotz"])),1);
entry_name = "arm1_to_effector1";
transform.arm1_to_e1 = get_pose_matrix(table2array(fixed_data(entry_name,["x","y","z"])),table2array(fixed_data(entry_name,["rotx","roty","rotz"])),1);
entry_name = "arm1_to_effector1";
transform.arm1_to_e1 = get_pose_matrix(table2array(fixed_data(entry_name,["x","y","z"])),table2array(fixed_data(entry_name,["rotx","roty","rotz"])),1);
entry_name = "effector1_to_camera";
transform.e1_to_cam = get_pose_matrix(table2array(fixed_data(entry_name,["x","y","z"])),table2array(fixed_data(entry_name,["rotx","roty","rotz"])),1);

rot_set = {};
eul_set = {};

for i_time =1:length(time_data)
    
    translation = time_data(i_time).cpose(1:3)/1000;
    rotation =  time_data(i_time).cpose(4:6)';
    transform.e2_to_arm2 = get_pose_matrix(translation,rotation,-1);

    rotm = eye(3);
    for i_pose = 1: length(field_list)
        rotm = transform.(field_list{i_pose})(1:3,1:3)*rotm; 
    end
    eulm = rad2deg(rotm2eul(rotm,"XYZ"));
    eul_set = [eul_set; eulm];
    rot_set = [rot_set; rotm];
end

save lab_data.mat -mat eul_set rot_set