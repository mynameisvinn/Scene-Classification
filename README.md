## what is this?
a scene classifier for photos. 

205 scenes are recognized including mountains, aquariums, bookstores, soccer fields, etc. exotic settings are included too - castles, chalets, and catacombs. in its current form, top-1 accuracy is 50.04% and top-5 accuracy is 81.10%. 

## specs
* Ubuntu 14.04
* [Caffe](http://caffe.berkeleyvision.org/)
* [Numpy](http://www.numpy.org/), [SciPy](https://www.scipy.org/), [Pandas](http://pandas.pydata.org/), [Scikit Learn](http://scikit-learn.org/), [Matplotlib](http://matplotlib.org/)

## ml deets
trained on 2.5m images comprising 205 unique scene categories from mit's csail places dataset (http://places.csail.mit.edu/). for more information on approach and dataset, refer to "places: an image database for deep scene understanding" (http://places.csail.mit.edu/places2_arxiv.pdf).


## get docker image

building caffe from source ruined my weekend. it is not for the faint of heart so you should do one of the following:

### option 1: pull from docker hub

```
docker pull mynameisvinn/vrb_scene_classification
```

### option 2: build locally
```
git clone https://github.com/mynameisvinn/vrb_scene_classification
cd vrb_scene_classification
docker build .
```

## run

from command line, do

```
docker run -it -p 8888:8888 -p 6006:6006 -v /sharedfolder:/root/sharedfolder mynameisvinn/vrb_scene_classification
```

then do

```
$ python run_scene.py images/mountains.jpg
```
if youve made it this far, it should print the top 5 predictions: 

* mountain_snowy
* glacier
* mountain
* snowfield
* volcano
