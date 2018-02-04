# Project 1: Image Alignment and Color Compositing

## 1. Introduction
This project aims to automatically align and composite images from [ Prokudin-Gorskii photo collection](http://www.loc.gov/exhibits/empire/gorskii.html). This photo collection was created by the Russian photographer [Sergei Mikhailovich Prokudin-Gorskii](http://en.wikipedia.org/wiki/Prokudin-Gorskii) (1863-1944) by photos he captured throughout the Russia during a time where the color cameras were not even invented.

He came up with a simple idea to produce color photos: record three exposures of every scene onto a glass plate using a red, a green, and a blue filter and then project the monochrome pictures with correctly colored light to reproduce the color image. Below image shows the scanned version of one of his glass plates.

<p align="center">
<img src=aligned_images/report/1-raw.jpg alt="raw image" width="200">
</p>

The objective of this project is to automatically generate the color image from the glass plate image with three separate layers.

## 2. Single-Scale Aligning

This algorithm aligns an image based on exhaustive search on a specified pixel window. Below shows the basic steps in this algorithm.
1. Read the raw image.
<p align="center">
<img src=aligned_images/report/1-raw.jpg alt="raw image" width="200">
</p>
2. Detect the outside black border and crop the image to remove the white space outside the border.
<p align="center">
<img src=aligned_images/report/2-cropped.png alt="borders cropped" width="600">
</p>
3. Split the image into blue, green and red layers based on its size
<p align="center">
<img src=aligned_images/report/3-split.png alt="split" width="600">
</p>
4. Move the green layer over blue layer ±15 pixels in both vertical and horizontal directions and calculate the sum of square differences (SSD).
5. Two layers are considered to be coincide when the SSD values is minimum. Shift the green layer in vertical and/or horizontal directions with the pixel displacement when the minimum SSD was calculated.
6. Repeat same steps as 4-5 except now the it's the red layer, not green layer.
7. Crop the aligned image you get at step 6 to avoid artifacts near the borders due to extra/missing layers
<p align="center">
<img src=aligned_images/report/4-aligned-cropped.png alt="aligned cropped" width="300">
</p>
8. Display the aligned image.
<p align="center">
<img src=aligned_images/report/5-final.png alt="results" width="300">
</p>

[](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#41-cropping-outer-border)

Running the code:

```
python single_scale_align.py images\01725u.jpg
```

## 3. Multi-Scale Aligning

## 4. Cropping Outer Border
## 5. Cropping Aligned Image
## 6. Contrast Adjustment
