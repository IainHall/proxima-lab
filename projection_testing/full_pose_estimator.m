

%%%
% This script is for estimating the full pose from lab gathered data 
%%%

%% load in data
lab_folder = "example_output_folder";
files = dir(lab_folder);

lab_data_set = {};

for i_file = 1:length(files)

    if contains(files(i_file).name, ".xlsx")
        file_path = lab_folder + "/" + files(i_file).name;
    
        lab_setup_table = readtable(file_path,'Sheet','DATA', VariableNamingRule='preserve');
        lab_meta_data = readtable(file_path,'Sheet','META_DATA', VariableNamingRule='preserve');

        lab_data_set = [lab_data_set; {lab_setup_table,lab_meta_data }];
    end

end
%% carry out full pose estimation
poses_out  = {};
for i_data = 1:size(lab_data_set,1)
lab_setup_table = lab_data_set{i_data,1};
num_poses = size(lab_setup_table,1);
poses = zeros(num_poses, 4,4);

for i_pose = 1: num_poses
    poses(i_pose,:,:) = get_pose_matrix(table2array(lab_setup_table(i_pose,2:4)),table2array(lab_setup_table(i_pose,5:8)),table2array(lab_setup_table(i_pose,9)));
end

pose_out = eye(4);
for i_pose = 1:num_poses 
    pose_out = squeeze(poses(i_pose,:,:))*pose_out;
end

poses_out = [poses_out;pose_out];
end
%% write out data

for i_pout = 1:size(poses_out,1)

    out_folder=  lab_folder+"/out_folder" ;
    mkdir(out_folder)
    meta_data_table = lab_data_set{i_pout,2};
    file_out_name = "id_"+meta_data_table{1,'id'}{1}+"_pose.xlsx";
    writematrix(poses_out{i_pout},out_folder+"/"+file_out_name, 'Sheet','POSE')
    writetable( meta_data_table , out_folder+"/"+file_out_name,'Sheet','META_DATA');

end

