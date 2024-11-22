function [projection,object] = pose_to_projection(camera_intrinsic, poses, object, correction_matrix, params)



%{
if length(object(1,:)) ==3
    for i_object = 1: size(object,1)
    object(i_object,4) = 1;
    end
end
%}
% poses should be an array going from object frame to camera frame

for i_pose = 1:size(poses,1)
    i_pose
    squeeze(poses(i_pose,:,:))
    for i_object = 1: size(object,1)
        pose = squeeze(poses(i_pose,:,:));
        translated = object(i_object,:)'+ pose(1:3,4);
        rotated = pose(1:3,1:3)*translated;
        
        object(i_object,:) = rotated';
    end
end

projection = zeros(size(object,1),3);

for i_object = 1:size(object,1) 
    projection(i_object,:) = camera_intrinsic * correction_matrix * object(i_object,1:3)';
    projection(i_object,:) = projection(i_object,:)/  projection(i_object,3);
end


end

