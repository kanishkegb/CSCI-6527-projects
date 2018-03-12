close all;
clear;

addpath ./images

depth_image = 'depth.jpg';
im = im2double((imread(depth_image)));
[h, w] = size(im);

im_out = -1*ones(h, w);
for r = 1:h
    % start at the left pixel of each row
    for c = 1:w
        if im_out(r, c) >= 0
            continue
        end
        
        
        x = c;
        
        % randomly pick color C
        color = [rand(1), rand(1), rand(1)];
        color = rand(1);
        im_out(r, x) = color;
        
        gap = 100;
        
        %  map depth onto a displacement d
        d = gap + floor(255*im(r, x)/2);
        x = x + d;
        
        % if x is still in the image 
        while x <= w 
            % then loop to "color location x..."
            im_out(r, x) = color;
            
            d = gap + floor(255*im(r, x)/2);
            x = x + d;
        end
    end
end
% imagesc(im_out)
% axis equal
imshow(im_out)