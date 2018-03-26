function [x, y] = circle_coordinates(r, reso)

th = 0:reso:2*pi;
x = r * cos(th);
y = r * sin(th);

end