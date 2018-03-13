close all;
clear;

addpath ./images

depth_image = 'depth.jpg';
% im = im2double(rgb2gray(imread(depth_image)));
im = im2double((imread(depth_image)));
% im = imcomplement(im);
[h, w] = size(im);

im_out = zeros(h, w, 3);
for r = 1:h
    % start at the left pixel of each row
    for c = 1:w
        if im_out(r, c, 1) > 0
            continue
        end
        
        
        x = c;
        
        % randomly pick color C
        color = [rand(1), rand(1), rand(1)];
        % color = rand(1);
        
        gap = floor(w/10);
        scale = .5;

        % if x is still in the image 
        while x <= w 
            im_out(r, x, :) = color;
            
            d = gap + floor(255*im(r, x)*scale);
            x = x + d;
        end
    end
end
% imagesc(im_out)
% axis equal
imshow((im_out))