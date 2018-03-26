function cube()

hold on;
% fill3([1 1 1 1], [-1 -1 1 1], [-1 1 1 -1], [1 1 1 1])
% fill3(-1*[1 1 1 1], [-1 -1 1 1], [-1 1 1 -1], [1 1 1 1])
% fill3([1 -1 -1 1], [-1 -1 1 1], [1 1 1 1], [1 1 1 1])
% fill3([1 -1 -1 1], [-1 -1 1 1], -1*[1 1 1 1], [1 1 1 1])
% fill3([1 1 -1 -1], [1 1 1 1], [-1 1 1 -1], [1 1 1 1])
% fill3([1 1 -1 -1], -1*[1 1 1 1], [-1 1 1 -1], [1 1 1 1])
% 

x = [1 1 1 1 -1 -1 -1 -1];
y = [-1 -1 1 1 1 -1 -1 1];
z = [-1 1 1 -1 -1 -1 1 1];

V = [x', y', z'];
F = [1 2 3 4;
     1 2 7 6;
     1 6 5 4;
     2 7 8 3;
     3 8 5 4;
     5 6 7 8];
     
patch('Faces',F,'Vertices',V);

view(3);
colormap gray
material SHINY
% shading interp
axis equal
lightangle(-37.5, +30)
camlight HEADLIGHT
% camlight RIGHT

% h.FaceLighting = 'gouraud';
% h.AmbientStrength = 0.3;
% h.DiffuseStrength = 0.8;
% h.SpecularStrength = 0.9;
% h.SpecularExponent = 25;
% h.BackFaceLighting = 'unlit';



hold off;