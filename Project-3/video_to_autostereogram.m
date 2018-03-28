% convert video file to autostereogram video

vid_file = 'vid.mp4';
filename = 'vid.gif';

v = VideoReader(vid_file);
out_v = VideoWriter('depth_vid.avi');
open(out_v);

i = 0;
while hasFrame(v)
    i = i + 1
    if i > 100
        break
    end
    
    
    f = readFrame(v);
    g = imcomplement(im2double(rgb2gray(f)));

    [h, w] = size(g);
    if i == 1
        cmap = rand(h, w, 3);
    end
    
    a = autostereogram(g, cmap);
    imshow(a);
    
    [A,map] = rgb2ind(impyramid(a, 'reduce'), 256);
    if i == 1
        imwrite(A, map, filename,'gif', 'LoopCount', Inf, ...
            'DelayTime', .01);
    else
        imwrite(A, map, filename, 'gif', 'WriteMode', 'append', ...
            'DelayTime', .01);
    end
    
    % writeVideo(out_v, a);
end

close(out_v)