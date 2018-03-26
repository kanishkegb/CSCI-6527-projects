function im = draw_cir_on_image(im, r, depth, x0, y0)
% Draws a circle on a given image at a given depth to be used on
% autostereograms.
%
% Args:
%   im - image for the circle to be drawn on
%   r - radius of the circle in pixels
%   depth - depth of the circle (1 - deeper, 0 - closer)
%   x0, y0 - center of the circle in pixels
%
% Returns:
%   im - original with the circle drawn over it

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