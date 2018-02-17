% close all; % closes all figures

addpath ./images

% read images and convert to single format
im1 = im2single(imread('bran.jpg'));
im2 = im2single(imread('night_king.jpg'));
x = [81, 275]';
y = [216, 415]';

% im1 = rgb2gray(im1); % convert to grayscale
% im2 = rgb2gray(im2);

% use this if you want to align the two images (e.g., by the eyes) and crop
% them to be of same size
[im2, im1] = align_images(im2, im1);

% uncomment this when debugging hybridImage so that you don't have to keep aligning
% keyboard; 

%% Choose the cutoff frequencies and compute the hybrid image (you supply
%% this code)
cutoff_low = ;
cutoff_high = 1; 
im12 = hybrid_image(im1, im2, cutoff_low, cutoff_high);
% figure(1)
% imagesc(im12);

%% Crop resulting image (optional)
% figure(1), hold off, imagesc(im12), axis image, colormap gray
% disp('input crop points');
% [x, y] = ginput(2);  x = round(x); y = round(y);
im12 = im12(min(y):max(y), min(x):max(x), :);
figure(1)
show_hybrid(im12)
% figure(2)
% imagesc(im12)
% set(gca,'xcolor','w','ycolor','w','xtick',[],'ytick',[])

%% Compute and display Gaussian and Laplacian Pyramids (you need to supply this function)
% N = 5; % number of pyramid levels (you may use more or fewer, as needed)
% pyramids(im12, N);
