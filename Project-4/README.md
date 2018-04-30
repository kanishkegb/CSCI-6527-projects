[Home](https://github.com/kanishkegb/CSCI-6527-projects)
# Project 4: Humpback Whale Identification Challenge

<a name="contents"></a>
## Contents
1. [Introduction](#intro)

<a name="intro"></a>
## 1. Introduction
Whaling has been a practiced for many centuries by human at different areas/countries of the world, mainly for meat and whale oil. After the industrialization of the whaling at the 17th century, competitive whaling nations exponentially increased, leading to kill around 50,000 whales a year by 1930s ([see details](http://www.thecanadianencyclopedia.ca/en/article/whaling/)). This resulted in rapid depletion of the most of the known whale stocks around the world. As a result, the International Whaling Commission (IWC) banned commercial whaling in 1986, while imposing whaling quotas instead of a total ban on few traditionally whaling nations. The graph below shows how the whaling changed over the course of years for reported data from few whaling nations (image from [Wikipedia](https://en.wikipedia.org/wiki/Whaling#/media/File:Whales_Nordic.png)).

<center>
  <img src="./images/whale_count.png"  width="300"/>
</center>

After centuries of those intense whaling, the whales are still in the recovery step. Further, they have to deal with man-made environmental disasters such as global warming. The anti-whaling movement use photo surveillance for their whale conservation efforts. The shape and the unique markings on the whale's tale/fluke (see image below) to identify the each whale species and track their motions and behaviors.

<center>
  <img src="./images/fluke.jpg"  width="300"/>
</center>

Currently, the identification is done manually. The [Kaggle](https://www.kaggle.com/c/whale-categorization-playground) initiated a project to help automate the whale identification. I thought I would contribute to this project for my final project.

<!-- Names of everyone in your group.
Introduction (problem –Why, with real‐world applications), and one illustrative example output.
Related Work (What has been done, with a few references)
Your Approach (How you are going to do it, with algorithms, equations, figures)
Your Implementation and Analysis (What you do, with images, tables, and numbers)
Your Conclusions (Itemized conclusions, observations and discussions)  -->

## Dependencies
1. HDF5 for saving data
  ```
  conda install h5py
  ```
