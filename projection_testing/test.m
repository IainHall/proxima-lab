


focal_length_mm = 30;
pixel_pitch = 1024/36; % pixels per mm
focal_length_pixels =293.2;%focal_length_mm*pixel_pitch;
centre_pixel = [640,480]; % centre pixel in pixels

object_points = readmatrix("object_points.xlsx");
camera_intrinsic = [focal_length_pixels, 0 , centre_pixel(1); ...
                    0, focal_length_pixels ,  centre_pixel(2); ...
                    0 , 0,                      1]; %readmatrix("camera_details.xlsx",)
lab_setup_table = readtable("actual_lab_setup.csv")



n = size(lab_setup_table,1);
poses = zeros(n, 4,4);

%lab_setup_table(end, 6) =   table(deg2rad(-90));
%lab_setup_table(end,5) = table(table2array(lab_setup_table(end,5))+deg2rad(180));
%lab_setup_table = flip(lab_setup_table,1)

for i_pose = 1: size(lab_setup_table,1)
    poses(i_pose,:,:) = get_pose_matrix(table2array(lab_setup_table(i_pose,2:4)),table2array(lab_setup_table(i_pose,5:8)));
end

correction_matrix= eye(3);
correction_matrix(2,2) = -1;
correction_matrix(3,3) = -1;


[projection,object] = pose_to_projection(camera_intrinsic,poses,object_points, correction_matrix,[]);

%%

test_image = imread("test_img_skew30.png");
figure()
imshow(test_image)
hold on 
scatter(projection(:,1),projection(:,2))
scatter(512,512, MarkerFaceColor='r')
hold off





