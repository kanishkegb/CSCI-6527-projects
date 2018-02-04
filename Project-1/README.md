# Project 1: Image Alignment and Color Compositing

This project aims to automatically align and composite images from [ Prokudin-Gorskii photo collection](http://www.loc.gov/exhibits/empire/gorskii.html). This photo collection was created by the Russian photographer [Sergei Mikhailovich Prokudin-Gorskii](http://en.wikipedia.org/wiki/Prokudin-Gorskii) (1863-1944) by photos he captured throughout the Russia during a time where the color cameras were not even invented.

He came up with a simple idea to produce color photos: record three exposures of every scene onto a glass plate using a red, a green, and a blue filter and then project the monochrome pictures with correctly colored light to reproduce the color image. Below image shows the scanned version of one of his glass plates.

<p align="center">
<img src=images/00804v.jpg alt="raw image" width="200">
</p>

The objective of this project is to automatically generate the color image from the glass plate image with three separate layers.

## 1. Single-Scale Aligning

This function aligns an image based on exhaustive search on specified windows.

Running the code:

```
python single_scale_align.py images\01725u.jpg
```
