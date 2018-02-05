# Project 1: Image Alignment and Color Compositing

## Contents
1. [Introduction](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#1-introduction)
2. [Single-Scale Aligning](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#)
3. [Multi-Scale Aligning](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#2-single-scale-aligning)
4. [Cropping Outer Border](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#4-cropping-outer-border)
5. [Cropping Aligned Image](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#5-cropping-aligned-image)
6. [Contrast Adjustment](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#6-contrast-adjustment)
7. Gallery: [single-scale low resolution](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1/aligned_images/multi_scale#high-resolution-gallery), [multi-scale high resolution](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1/aligned_images/single_scale#low-resolution-gallery)

## 1. Introduction
This project aims to automatically align and composite images from [ Prokudin-Gorskii photo collection](http://www.loc.gov/exhibits/empire/gorskii.html). This photo collection was created by the Russian photographer [Sergei Mikhailovich Prokudin-Gorskii](http://en.wikipedia.org/wiki/Prokudin-Gorskii) (1863-1944) by photos he captured throughout the Russia during a time where the color cameras were not even invented.

He came up with a simple idea to produce color photos: record three exposures of every scene onto a glass plate using a red, a green, and a blue filter and then project the monochrome pictures with correctly colored light to reproduce the color image. Below image shows the scanned version of one of his glass plates.

<p align="center">
<img src=aligned_images/report/1-raw.jpg alt="raw image" width="200">
</p>

The objective of this project is to automatically generate the color image from the glass plate image with three separate layers.

[back to contents](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#contents)

## 2. Single-Scale Aligning

This algorithm aligns an image based on exhaustive search on a specified pixel window. Below shows the basic steps in this algorithm.

1. Read the raw image.
<p align="center">
<img src=aligned_images/report/1-raw.jpg alt="raw image" width="170">
</p>

2. Detect the outside black border and crop the image to remove the white space outside the border (details in [Section 4](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#4-cropping-outer-border)).
<p align="center">
<img src=aligned_images/report/2-cropped.png alt="borders cropped" width="600">
</p>

3. Split the image into blue, green and red layers based on its size
<p align="center">
<img src=aligned_images/report/3-split.png alt="split" width="800">
</p>

4. Move the green layer over blue layer ±15 pixels in both vertical and horizontal directions and calculate the sum of square differences (SSD).

5. Two layers are considered to be coincide when the SSD values is minimum. Shift the green layer in vertical and/or horizontal directions with the pixel displacement when the minimum SSD was calculated.

6. Repeat same steps as 4-5 except now the it's the red layer, not green layer.

7. Crop the aligned image you get at step 6 to avoid artifacts near the borders due to extra/missing layers (details in [Section 5](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#5-cropping-aligned-image)).
<p align="center">
<img src=aligned_images/report/4-aligned-cropped.png alt="aligned cropped" width="800">
</p>

8. Adjust the contrast of each layer (details in [Section 6](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#6-contrast-adjustment)).
<p align="center">
<img src=aligned_images/report/5-final.png alt="results" width="450">
</p>

This method works effectively on relatively smaller images. When the number of pixels in an image increases, the processing time increases significantly.

### Code
Running the code: python single_scale_align.py path\to\image.
For example:
```
python single_scale_align.py images\01725u.jpg
```

[back to contents](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#contents)

## 3. Multi-Scale Aligning
This algorithm aligns a larger image based on multi-scale alignment. Below are the basic steps in this algorithm.

1. Read the raw image.

2. Detect the outside black border and crop the image to remove the white space outside the border (details in [Section 4](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#4-cropping-outer-border)).
<p align="center">
<img src=aligned_images/report/7-cropped.png alt="borders cropped" width="800">
</p>

3. Split the image into blue, green and red layers based on its size

4. Resize the image by half and blur it using an averaging filter

5. Repeat above step 4 until resized image width is smaller than 100 pixels. Below figure shows the blurred and resized image that was used for exhaustive search. This has low resolution which makes is faster to align the layers.
<p align="center">
<img src=aligned_images/report/8-blurred.png alt="aligned cropped" width="300">
</p>

6. Repeat steps 4 to 6 in single-scale alignment algorithm.

7. Based on the alignment performed in above step 6, check for minimum SSD value in image intermediate resized image in the step 5 by varying each green and red layers vertically and horizontally in ±2 pixels.
<p align="center">
<img src=aligned_images/report/9-aligned.png alt="aligned" width="800">
</p>

8. Crop the aligned image you get at step 6 to avoid artifacts near the borders due to extra/missing layers (details in [Section 5](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#5-cropping-aligned-image)).
<p align="center">
<img src=aligned_images/report/10-aligned-cropped.png alt="aligned cropped" width="800">
</p>

9. Adjust the contrast of each layer (details in [Section 6](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#6-contrast-adjustment)).
<p align="center">
<img src=aligned_images/report/11-contrast.png alt="results" width="800">
</p>

### Code
Running the code: python multi_scale_align.py path\to\image.
For example:
```
python multi_scale_align.py images\00458u.jpg
```

[back to contents](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#contents)

## 4. Cropping Outer Border

Each figure has a black outer border. But, outside that border, a white space can be observed. The procedure is that the image is split into blue, green, and red channels based on the height of the image. If this outer white space is not removed while doing that, splitting will not accurately slice the image into the three layers. Therefore, if everything outside the black outer border is cropped out, the algorithms will generate a better result.

For cropping out these white area, simply the difference between white and back pixels is used. The white pixels have value closer to 255 while the black pixels have a value closer to 0. Since the black may have slight variances on its brightness, a threshold value of 40 is used for detecting black. That is, if the pixel value is lower than threshold value, it is considered black.

<p align="center">
<img src=aligned_images/report/12-border-detect.png alt="results" width="500">
</p>

Above plot shows how the values vary throughout one row of pixels in an image. At the left and right corners, the white pixels with values closer to 255 can be observed. The sudden drop when moving inwards of the plot shows the black border. Based on this sudden drop of pixel values, the outer border is recognized and everything outside was cropped.

The below figure shows the difference between the original image and the image with cropped outside border.

<p align="center">
<img src=aligned_images/report/7-cropped.png alt="borders cropped" width="800">
</p>

[back to contents](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#contents)

## 5. Cropping Aligned Image

The aligning processes described above include shifting layers vertically or horizontally with respect to another layer. This may result in some pixel windows near border with one or two layers missing in that region. These regions can be observed in the left image below where green and yellow regions visible on top and bottom.

These regions are cropped out as follows. First, since we know how much the each layer is moved around in order to align, that region is removed from the figure. Then, two percent of the image is cropped in all borders to remove the black border from the image.

<p align="center">
<img src=aligned_images/report/10-aligned-cropped.png alt="aligned cropped" width="800">
</p>

[back to contents](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#contents)

## 6. Contrast Adjustment

There is no guarantee that the filters used by the photographer to generate each color layer is accurate. The contrast may differ based on the filter. This was done simply by mapping the lowest value and the highest value of each layer of image to 0 and 255 respectively.   

<p align="center">
<img src=aligned_images/report/11-contrast.png alt="results" width="800">
</p>

[back to contents](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#contents)

## 7. Gallery

To reduce the loading time, image gallery is moved here. Please use the below links to access the gallery.
  * [single-scale low resolution](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1/aligned_images/multi_scale#high-resolution-gallery),
  * [multi-scale high resolution](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1/aligned_images/single_scale#low-resolution-gallery)

[back to contents](https://github.com/kanishkegb/CSCI-6527-projects/tree/master/Project-1#contents)
