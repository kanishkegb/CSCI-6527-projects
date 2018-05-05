[Home](https://github.com/kanishkegb/CSCI-6527-projects)
# Project 4: Humpback Whale Identification Challenge

<a name="contents"></a>
## Contents
1. [Introduction](#intro)
2. [Basic Classifier](#basic_clf)

<a name="intro"></a>
## 1. Introduction
Whaling has been a practiced for many centuries by human at different areas/countries of the world, mainly for meat and whale oil. After the industrialization of the whaling at the 17th century, competitive whaling nations exponentially increased, leading to kill around 50,000 whales a year by 1930s ([see details](http://www.thecanadianencyclopedia.ca/en/article/whaling/)). This resulted in rapid depletion of the most of the known whale stocks around the world. As a result, the International Whaling Commission (IWC) banned commercial whaling in 1986, while imposing whaling quotas instead of a total ban on few traditionally whaling nations. The graph below shows how the whaling changed over the course of years for reported data from few whaling nations (image from [Wikipedia](https://en.wikipedia.org/wiki/Whaling#/media/File:Whales_Nordic.png)).

<center>
  <img src="./images/whale_count.png"  width="350"/>
</center>

After centuries of those intense whaling, the whales are still in the recovery step. Further, they have to deal with man-made environmental disasters such as global warming. The anti-whaling movement use photo surveillance for their whale conservation efforts. The shape and the unique markings on the whale's tale/fluke (see image below) to identify the each whale species and track their motions and behaviors.

<center>
  <img src="./images/fluke.jpg"  width="350"/>
</center>

Currently, the identification is done manually. The [Kaggle](https://www.kaggle.com/c/whale-categorization-playground) initiated a project to help automate the whale identification. The challenging part is the low number imagery from the each type of whale. I thought I would contribute to this project for my final project. Since this is my first machine learning experience, this way, I get to learn machine learning while helping to save thousands of whales all around the world!

<a name="basic_clf"></a>
## 2. Basic Classifier

Basically, Kaggle provides a set of training data and a set of test data. The training data consist of 9000+ manually labeled image of flukes of different whale species and test data has 15,000 unlabeled data.  The objective is to train a classifier using the train data to identify the each fluke in the test data. The predictions can be updated to the Kaggle website where they check it, score the predictions and put the scores in a [leaderboard](https://www.kaggle.com/c/whale-categorization-playground/leaderboard).

Given that this is my first machine learning project, I started small. First this I tried was using a basic classifier to classify data. I used scikit-learn for this project and choose the Support Vector Machine based on their documentation.

<center>
  <img src="./images/scikit_estimator_map.png"  width="650"/>
</center>


<!-- Names of everyone in your group.
Introduction (problem –Why, with real‐world applications), and one illustrative example output.
Related Work (What has been done, with a few references)
Your Approach (How you are going to do it, with algorithms, equations, figures)
Your Implementation and Analysis (What you do, with images, tables, and numbers)
Your Conclusions (Itemized conclusions, observations and discussions)  -->

## Running the code
### Creating the virtual environment
1. Create a virtual environment
  ```
  conda update -n base conda  # optional
  conda create --name ML
  conda activate ML
  conda install numpy
  conda install scikit-learn
  conda install cython
  pip install --ignore-installed --upgrade tensorflow
  sudo apt-get install protobuf-compiler python-pil python-lxml
  conda install pillow
  conda install matplotlib
  conda install pandas
  conda install h5py
  ```
2. Dependencies for object detection model
  ```

  ```
3. Clone and configure object detection API from TF
  ```
  git clone git@github.com:tensorflow/models.git
  cd models/research/
  protoc object_detection/protos/*.proto --python_out=.
  export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
  # on Windows computers, you need to manually add these paths to the system variables
  ```
4. Test the installation
  ```
  python object_detection/builders/model_builder_test.py
  ```

### Training
