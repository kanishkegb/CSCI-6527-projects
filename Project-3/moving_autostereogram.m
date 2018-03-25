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

% for r = min_r:max_r
    im_frame = draw_cir_on_image(im_tunnel, 50, 0, x0, y0);
    im_out = autostereogram(im_frame);
% end

% imshow(im)
hold on
axis equal
hold off
imshow(im_out)