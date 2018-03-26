vid_file = '/images/vid.mp4';

v = VideoReader(vid_file);
out_v = VideoWriter('depth_vid.avi');
open(out_v);

i = 0;
cmap = rand(h, w, 3);
while hasFrame(v)
    i = i + 1
    if i > 40
        break
    end
    
    f = readFrame(v);
    g = imcomplement(im2double(rgb2gray(f)));
    low_g = g;
    [h, w] = size(low_g);
    
    a = autostereogram(low_g, cmap);
    imshow(a);
    
    writeVideo(out_v, a);
end

close(out_v)