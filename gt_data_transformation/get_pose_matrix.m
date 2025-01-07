function [pose,str] = get_pose_matrix(translations,euler_angles,direction, deg)
%GET_POSE_MATRIX Summary of this function goes here
%   Detailed explanation goes here

if deg == true
    euler_angles = deg2rad(euler_angles);
end


if direction == -1
   
    
    pose =  eye(4);
    %pose(1:3,1:3) = angle2dcm(euler_angles(1),euler_angles(2),euler_angles(3),'XYZ');
    pose(1:3,1:3)  = inv(eul2rotm(euler_angles,'XYZ'));
    pose(1:3,4) = -translations;

    str = "";
   
elseif direction ==1
    pose =  eye(4);
    %pose(1:3,1:3) = angle2dcm(euler_angles(1),euler_angles(2),euler_angles(3),'XYZ');
    pose(1:3,1:3)  =eul2rotm(euler_angles,'XYZ');
    pose(1:3,4) = translations;

    str = "";

else
    str= "warning invalid direction, defaulting to positive direction";
    disp(str)
    pose =  eye(4);
    %pose(1:3,1:3) = angle2dcm(euler_angles(1),euler_angles(2),euler_angles(3),'XYZ');
    pose(1:3,1:3)  =eul2rotm(euler_angles,'XYZ');
    pose(1:3,4) = translations;
   
end

