close all;
clear;

addpath ./images

h = 600;
w = 800;
x0 = h/2;
y0 = w/2;
max_r = 300;
min_r = 100;
num_circles = 8;

t_data = struct('h', h, 'w', w, 'x0', x0, 'y0', y0, 'max_r', max_r, ...
    'min_r', min_r, 'num_circles', num_circles);

im_tunnel = imgaussfilt(tunnel(t_data), 2);
reso = 10;
frames = 1:round((max_r - min_r) / reso);

cmap = rand([h, w, 3]);

flag_first_run = 1;
filename = 'animation.gif';
for r = max_r:-50:min_r
    x0 = x0 + 1;
    im_frame = draw_cir_on_image(im_tunnel, round(r/5), 0, x0, y0);
    im_frame = imgaussfilt(im_frame, 2);
    im_out = autostereogram(im_frame, cmap);
    imshow(im_out)
    axis equal
    
    [A,map] = rgb2ind(im_out, 256);
    if flag_first_run == 1
        flag_first_run = 0;
        imwrite(A, map, filename,'gif', 'LoopCount', Inf, 'DelayTime', 1);
    else
        imwrite(A, map, filename, 'gif', 'WriteMode', 'append', ...
            'DelayTime', 1);
    end
end

% imshow(im)
% hold on
% axis equal
% hold off
% imshow(im_out)