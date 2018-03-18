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

im = imgaussfilt(tunnel(20), 2);
im_out = autostereogram(im);

% imshow(im)
% hold on
axis equal
hold off
imshow(im_out)