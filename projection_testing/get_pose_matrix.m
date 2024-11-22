function [pose] = get_pose_matrix(translations,euler_angles)
%GET_POSE_MATRIX Summary of this function goes here
%   Detailed explanation goes here

pose =  zeros(4);
%pose(1:3,1:3) = angle2dcm(euler_angles(1),euler_angles(2),euler_angles(3),'XYZ');
pose(1:3,1:3)  = inv(quat2rotm(euler_angles));
pose(1:3,4) = -1*translations;
pose(4,4) = 1;



end

