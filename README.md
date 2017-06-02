## what is this?
a scene classifier for 360 photos.

205 scenes are recognized including mountains, aquariums, bookstores, soccer fields, etc. exotic settings are included too - castles, chalets, and catacombs. top-1 accuracy is 50.04% and top-5 accuracy is 81.10%. 

## specs
* Ubuntu 14.04
* [Caffe](http://caffe.berkeleyvision.org/)
* [Numpy](http://www.numpy.org/), [SciPy](https://www.scipy.org/), [Pandas](http://pandas.pydata.org/), [Scikit Learn](http://scikit-learn.org/), [Matplotlib](http://matplotlib.org/)

## ml deets
trained on 2.5m images comprising 205 unique scene categories from [mit's csail places](http://places.csail.mit.edu/). for details, read ["places: an image database for deep scene understanding"](http://places.csail.mit.edu/places2_arxiv.pdf).

## get da docker
building caffe from source is not for the faint of heart so you should do the following:
```
git clone https://github.com/mynameisvinn/scene_classification
cd scene_classification
docker build -t scene_classification .
```

## run
### option 1 (recommended)
from command line, do
```
docker run scene_classification python run_scene.py images/triple.jpg
```
you should see top five predictions, in order of confidence: water park, ocean, lagoon, beach, coast.
### option 2
from command line, do
```
docker run -it mynameisvinn/scene_classification
```
then do
```
$ python run_scene.py images/park.jpg
```
