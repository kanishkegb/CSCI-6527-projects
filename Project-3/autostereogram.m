function im_out = autostereogram(im)

[h, w] = size(im);

gap = floor(w/40);
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

end