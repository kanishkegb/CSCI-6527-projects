close all;
clear;

addpath ./images

% depth_image = 'tunnel0.png';
% im_check = imread(depth_image);
% 
% if length(size(im_check)) == 3
%     im = im2double(rgb2gray(imread(depth_image)));
% else
%     im = im2double(imread(depth_image));
% end

% im = imcomplement(im);

t_data = struct;
t_data.h = 600;
t_data.w = 800;
t_data.x0 = t_data.h/2;
t_data.y0 = t_data.w/2;
t_data.max_r = 300;
t_data.min_r = 100;
t_data.num_circles = 8;

im = imgaussfilt(tunnel(t_data), 2);
im_out = autostereogram(im);

% imshow(im)
hold on
axis equal
hold off
imshow(im_out)