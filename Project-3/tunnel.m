function im = tunnel(num_circles)
h = 600;
w = 800;

im = zeros(h, w);

x0 = h/2;
y0 = w/2;

max_r = 600;
min_r = 100;

for cir = 1:num_circles
    depth = cir/num_circles;
    r = (max_r - min_r) * (num_circles - cir) / num_circles
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