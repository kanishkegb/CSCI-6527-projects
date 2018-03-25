function im = tunnel(t_data, depth)

h = t_data.h;
w = t_data.w;
x0 = t_data.x0;
y0 = t_data.y0;

im = zeros(h, w);

max_r = t_data.max_r;
min_r = t_data.min_r;
num_circles = t_data.num_circles;

for cir = 1:num_circles
    r = min_r + (max_r - min_r) * (num_circles - cir) / num_circles;
    im = draw_cir_on_image(im, r, depth(cir), x0, y0);
end

end