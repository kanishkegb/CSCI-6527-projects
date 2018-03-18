[x,y,z]=cylinder(1, 100);

cyl_thickness = 1;
surf([x(1,:); x(2,:)],[y(1,:); y(2,:)],[z(1,:); z(2,:)], 'EdgeColor','none')
hold on
fill3(x(1,:), y(1,:), z(1,:), z(1,:))
fill3(x(2,:), y(2,:), z(2,:), z(2,:))
colormap gray
shading interp
lightangle(+0,80)
axis equal