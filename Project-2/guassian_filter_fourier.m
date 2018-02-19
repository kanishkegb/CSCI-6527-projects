function [im_fil_fft, im_fil] = guassian_filter_fourier(im, hs)
% applies a Gaussian filter to an image in Fourier domain and returns
% the image in Fourier domain and as an image

% hs = 7; % filter half-size
fil = fspecial('gaussian', hs*2+1, 10); 

fftsize = 1024; % should be order of 2 (for speed) and include padding
im_fft  = fft2(im,  fftsize, fftsize);  % 1) fft im with padding
fil_fft = fft2(fil, fftsize, fftsize);  % 2) fft fil, pad to same size as image
im_fil_fft = im_fft .* fil_fft;  % 3) multiply fft images

im_fil = ifft2(im_fil_fft);  % 4) inverse fft2
im_fil = im_fil(1+hs:size(im,1)+hs, 1+hs:size(im, 2)+hs); % 5) remove padding

end