close all;
clear;

addpath ./images

depth_image = 'peaks.png';
im_check = imread(depth_image);

if length(size(im_check)) == 3
    im = im2double(rgb2gray(imread(depth_image)));
else
    im = im2double(imread(depth_image));
end

im = imcomplement(im);
[h, w] = size(im);

gap = floor(w/20);
scale = .5;

im_out = zeros(h, w, 3);
for r = 1:h
    for c = 1:w
        
        % if non zero, a color is already picked
        if im_out(r, c, 1) > 0
            continue
        end

        x = c;
        color = [rand(1), rand(1), rand(1)];
        
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