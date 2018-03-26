close all;
clear;

addpath ./images

h = 600;
w = 800;
x0 = h/2;
y0 = w/2;
max_r = 300;
min_r = 50;
num_circles = 50;

t_data = struct('h', h, 'w', w, 'x0', x0, 'y0', y0, 'max_r', max_r, ...
    'min_r', min_r, 'num_circles', num_circles);

% im_tunnel = imgaussfilt(tunnel(t_data), 2);
reso = 5;
num_frames = round((max_r - min_r) / reso)
frames = 1:num_frames;

cmap = rand([h, w, 3]);

flag_first_run = 1;
filename = 'animation.gif';

depth = ones(num_frames, num_circles);
for i = frames
    max_depth = i / num_frames;
    depth(i, :) = linspace(0, max_depth, num_circles);
end

for i = frames
    i
    im_tunnel = imgaussfilt(tunnel(t_data, depth(i, :)), 2);
    im_out = autostereogram(im_tunnel, cmap);
    
    imshow(im_out)
    axis equal
    
    [A,map] = rgb2ind(im_out, 256);
    if flag_first_run == 1
        flag_first_run = 0;
        imwrite(A, map, filename,'gif', 'LoopCount', Inf, ...
            'DelayTime', .01);
    else
        imwrite(A, map, filename, 'gif', 'WriteMode', 'append', ...
            'DelayTime', .01);
    end
end

depth = flipud(depth);
for i = frames
    i
    im_tunnel = imgaussfilt(tunnel(t_data, depth(i, :)), 2);
    im_out = autostereogram(im_tunnel, cmap);
    
    imshow(im_out)
    axis equal
    
    [A,map] = rgb2ind(im_out, 256);
    
    imwrite(A, map, filename, 'gif', 'WriteMode', 'append', ...
        'DelayTime', .01);
end

% imshow(im)
% hold on
% axis equal
% hold off
% imshow(im_out)