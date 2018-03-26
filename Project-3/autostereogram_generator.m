close all;
clear;

addpath ./images

depth_image = 'tunnel.png';
im_check = imread(depth_image);

if length(size(im_check)) == 3
    im = im2double(rgb2gray(imread(depth_image)));
else
    im = im2double(imread(depth_image));
end

% im = imcomplement(im);
im_out = autostereogram(im);

% imagesc(im_out)
% axis equal
imshow((im_out))