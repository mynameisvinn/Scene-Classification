## what is this?
a scene classifier for 360 photos. built for vrb.

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
docker pull mynameisvinn/vrb_scenes
```

### option 2: build locally
```
git clone https://github.com/mynameisvinn/vrb_scenes
cd vrb_scenes
docker build .
```

## run

### option 1 (recommended)

from command line, do

```
docker run mynameisvinn/vrb_scenes python run_scene.py images/park.jpg

```
if youve made it this far, you should see top 5 predictions: 

* orchard
* tree farm
* topiary garden
* lawn
* park

### option 2

from command line, do

```
docker run -it mynameisvinn/vrb_scenes
```

then do

```
$ python run_scene.py images/park.jpg
```
