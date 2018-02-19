% close all; % closes all figures

clear
addpath ./images

% read images and convert to single format
im1 = (double(imread('flash.jpg')) / 255);
im2 = (double(imread('spiderman.jpg')) / 255);
x = [6, 651]';
y = [206, 754]';

% im1 = rgb2gray(im1); % convert to grayscale
% im2 = rgb2gray(im2);

% use this if you want to align the two images (e.g., by the eyes) and crop
% them to be of same size
[im2, im1] = align_images(im2, im1);

% uncomment this when debugging hybridImage so that you don't have to keep aligning
% keyboard; 

%% Choose the cutoff frequencies and compute the hybrid image (you supply
%% this code)
cutoff_low = 7;
cutoff_high = 5;

[imh, imw] = size(im1);

[im1_fil_fft, im1_fil] = guassian_filter_fourier(im1, cutoff_low);
[im2_fil_fft, im2_fil] = guassian_filter_fourier(im2, cutoff_high);

fftsize = 1024; % should be order of 2 (for speed) and include padding
im2_fft  = fft2(im2,  fftsize, fftsize);  % 1) fft im with padding

im2_ = ifft2(im2_fft);  % 4) inverse fft2

hybrid_fft = im1_fil_fft + im2_fft - im2_fil_fft;
hybrid = ifft2(hybrid_fft);
hs = cutoff_high;
hybrid = hybrid(1+hs:size(im2,1)+hs, 1+hs:size(im2, 2)+hs); % 5) remove padding

figure(1)
imagesc(real(hybrid));

low_pass = imgaussfilt(im1, cutoff_low);
high_pass = imgaussfilt(im2, cutoff_high);

im12 = low_pass + im2 - high_pass;
% figure(1)
% imagesc(im12);

%% Crop resulting image (optional)
% figure(1), hold off, imagesc(im12), axis image, colormap gray
% disp('input crop points');
% [x, y] = ginput(2);  x = round(x); y = round(y);
im12 = im12(min(y):max(y), min(x):max(x), :);
% figure(1)
% show_hybrid(im12)
% figure(2)
% imagesc(im12)
set(gca,'xcolor','w','ycolor','w','xtick',[],'ytick',[])
axis equal

%% Compute and display Gaussian and Laplacian Pyramids (you need to supply this function)
% N = 5; % number of pyramid levels (you may use more or fewer, as needed)
% pyramids(im12, N);
