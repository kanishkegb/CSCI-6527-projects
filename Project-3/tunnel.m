function im = tunnel(t_data)

h = t_data.h;
w = t_data.w;
x0 = t_data.x0;
y0 = t_data.y0;

im = zeros(h, w);

max_r = t_data.max_r;
min_r = t_data.min_r;
num_circles = t_data.num_circles;

for cir = 1:num_circles
    depth = cir/num_circles
    r = min_r + (max_r - min_r) * (num_circles - cir) / num_circles
    for x = -r:r
        for y = -r:r
            if round(sqrt(x^2 + y^2)) < r
                try
                    im(x0+x, y0+y) = depth;
                catch
                    continue
                end
            end
        end
    end
    
end

end