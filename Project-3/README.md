[Home](https://github.com/kanishkegb/CSCI-6527-projects)

# Project 3: Stereo and Depth

<a name="contents"></a>
## Contents
1. [Introduction](#intro)
2. [Procedure](#procedure)
3. [Gallery](#gallery)
4. [Moving Autostereogram](#moving_autostereogram)

<a name="intro"></a>
## 1. Introduction
An autostereogram is basically an optical illusion that trick your eye to see depth in a 2D image. This became popular in 1990's as _Magic Eye_. The objective of this project is to generate an autostereogram from a given depth map.

<center>
  <img src="https://raw.githubusercontent.com/kanishkegb/CSCI-6527-projects/master/Project-3/autostereogram/saturn.jpg"  width="350"/>
</center>  

Above is an example for an autostereogram. If you need any help viewing the image, please visit the [original web page](http://www.magiceye.com/faq_example.htm) for instructions, where this was published.

[back to contents](#contents)

<a name="procedure"></a>
## 2. Procedure
To generate an autostereogram, the first thing one would need is the depth map. For this example, the depth image is chosen as a view of some mountains. Black color shows the closer objects while white areas shows further objects.

<center>
  <img src="https://raw.githubusercontent.com/kanishkegb/CSCI-6527-projects/master/Project-3/images/depth.jpg"  width="350"/>
</center>

The pseudo-code for generating the autostereogram is given below:
```
start at the left pixel of each row.  (ie, let x = 1)
randomly pick color C.
color location x with color C.
    look up the depth (Z) at pixel location x on that row.
    map Z onto a displacement d (something like d = 100 + Z/2).
    x = x + d.
    if x is still in the image
        (that is, if you haven't gone off the right edge)
        then loop to "color location x..."

if x isn't still in the image, set x to the position of the
    leftmost pixel that isn't colored at all yet,
loop to "randomly pick color C"
```

Implementing this algorithm generates the below autostereogram.
<center>
  <img src="https://raw.githubusercontent.com/kanishkegb/CSCI-6527-projects/master/Project-3/autostereogram/depth.png"  width="800"/>
</center>

For more cool images, check the [gallery](#gallery).

[back to contents](#contents)

<a name="gallery"></a>
## 3. Gallery

Below is a gallery of autostereograms developed. If you can't recognize any of the autostereograms or want to see the originals, check this [page](p3_extended).

<center>
  <img src="https://raw.githubusercontent.com/kanishkegb/CSCI-6527-projects/master/Project-3/autostereogram/tunnel.png"  width="800"/>
</center>

<center>
  <img src="https://raw.githubusercontent.com/kanishkegb/CSCI-6527-projects/master/Project-3/autostereogram/shark.png"  width="800"/>
</center>

<center>
  <img src="https://raw.githubusercontent.com/kanishkegb/CSCI-6527-projects/master/Project-3/autostereogram/plane.png"  width="800"/>
</center>

<center>
  <img src="https://raw.githubusercontent.com/kanishkegb/CSCI-6527-projects/master/Project-3/autostereogram/fountain.png"  width="800"/>
</center>

<center>
  <img src="https://raw.githubusercontent.com/kanishkegb/CSCI-6527-projects/master/Project-3/autostereogram/garden.png"  width="800"/>
</center>

<center>
  <img src="https://raw.githubusercontent.com/kanishkegb/CSCI-6527-projects/master/Project-3/autostereogram/gunman.png"  width="800"/>
</center>

<!-- <center>
  <img src="Project-3/autostereogram/peaks.png"  width="800"/>
</center> -->

<!-- <center>
  <img src="Project-3/autostereogram/sphere.png"  width="800"/>
</center> -->


<a name="moving_autostereogram"></a>
## 3. Moving Autostereogram

One another cool feature we can implement with this techniques is a moving autostereogram. Basically depth map we choose must be a function of time. We generate the autostereogram for each frame and combine them into a single sequence of images, as a gif or a video.


### Generating a Time Based Depth image
One way to generate a moving autostereogram is to define the depth map as a function of time. This way, the depth map is generated algorithmically and then the each frame is converted to a autostereogram.

Below is an example of the above case. The depth at the center increases with time and then reduces. The below GIF shows the generated autostereogram.

<center>
  <img src="Project-3/autostereogram/animation.gif"  width="800"/>
</center>


### Generating an Autostereogram from a Video

Below is a depth image generated from a camera fixed on a moving vehicle.
<center>
<iframe width="600" height="400" src="https://www.youtube.com/embed/KlSysxmtJnU?start=42" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</center>

The generated video is uploaded to YouTube. But YouTube compression/codecs tend to break the video generated from Matlab. The below GIF shows a part of the moving autostereogram generated from the above video. Full video can be downloaded [here](https://drive.google.com/file/d/1keisjXLHPdrUTPRqDf9rD6GZ-ulJn-Vf/view?usp=sharing) (size: 878 MBs).
<center>
  <img src="Project-3/autostereogram/vid.gif"  width="800"/>
</center>
