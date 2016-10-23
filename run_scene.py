import numpy as np
import sys
import caffe

def classify_scene(fpath_design, fpath_weights, im):

	# initialize net
	net = caffe.Net(fpath_design, fpath_weights, caffe.TEST)

	# load input and configure preprocessing
	transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
	transformer.set_mean('data', np.load('python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1)) # TODO - remove hardcoded path
	transformer.set_transpose('data', (2,0,1))
	transformer.set_channel_swap('data', (2,1,0))
	transformer.set_raw_scale('data', 255.0)

	# since we classify only one image, we change batch size from 10 to 1
	net.blobs['data'].reshape(1,3,227,227)

	# load the image in the data layer
	net.blobs['data'].data[...] = transformer.preprocess('data', im)

	# compute
	out = net.forward()

	# predicted predicted class
	print out['prob'].argmax()

	#print predicted labels
	# labels = np.loadtxt("data/ilsvrc12/synset_words.txt", str, delimiter='\t')
	# top_k = net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
	# print labels[top_k]


if __name__ == '__main__':
	# fetch pretrained models
	fpath_design = 'models_places/deploy_alexnet_places365.prototxt'
	fpath_weights = 'models_places/alexnet_places365.caffemodel'

	# fetch image
	im = caffe.io.load_image(sys.argv[1])

	# predict
	classify_scene(im)

