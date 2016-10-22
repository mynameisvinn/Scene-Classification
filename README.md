## Docker Image for Scene Classification
Scene classifier using Caffe framework. 

## Specs
* Ubuntu 14.04
* [Caffe](http://caffe.berkeleyvision.org/)
* [Numpy](http://www.numpy.org/), [SciPy](https://www.scipy.org/), [Pandas](http://pandas.pydata.org/), [Scikit Learn](http://scikit-learn.org/), [Matplotlib](http://matplotlib.org/)

## Scene Classifier
Trained on 2.5 million images comprising 205 unique scene categories from MIT's CSAIL Places Dataset (http://places.csail.mit.edu/)

Top-1 accuracy is 50.04% and Top-5 accuracy is 81.10%.

For more information on approach and dataset, refer to "Places: An Image Database for Deep Scene Understanding" (http://places.csail.mit.edu/places2_arxiv.pdf).

## Running Docker Image

To spin up container, do

```
docker run -it -p 8888:8888 -p 6006:6006 -v /sharedfolder:/root/sharedfolder mynameisvinn/vrb_scene_classification
```

Then, from command line, do

```
$ cd /src/caffe
$ python run_scene.py
```