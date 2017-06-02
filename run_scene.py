"""
scene classification with a pretrained alexnet caffe model.
"""

import sys
import pickle
import numpy as np
import caffe

def classify_scene(fpath_design, fpath_weights, fpath_labels, fpath_mean, image):
    """
    call a pretrained convnet to perform scene classification. for more 
    information, refer to   

    parameters
    ----------
    fpath_design : str
        file containing convnet architecture in json format.
    fpath_weights : str
        file containing pretrained convnet weights.
    fpath_labels : str
        file containing labels corresponding to pretrained model.

    returns
    -------
    top_k : list
        list containing top five predictions.
    """
    net = caffe.Net(fpath_design, fpath_weights, caffe.TEST)
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_mean('data', np.load(fpath_mean).mean(1).mean(1))
    transformer.set_transpose('data', (2, 0, 1))
    transformer.set_channel_swap('data', (2, 1, 0))
    transformer.set_raw_scale('data', 255.0)
    net.blobs['data'].reshape(1, 3, 227, 227)  # resize to 227x227 
    net.blobs['data'].data[...] = transformer.preprocess('data', image)
    out = net.forward()

    with open(fpath_labels, 'rb') as f:
        labels = pickle.load(f)
        top_k = net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
        return top_k

if __name__ == '__main__':
    # pretrained model
    MODEL_TYPE = 'models_places/deploy_alexnet_places365.prototxt'
    WEIGHTS = 'models_places/alexnet_places365.caffemodel'
    MEAN = 'python/caffe/imagenet/ilsvrc_2012_mean.npy'
    LABELS = 'labels/labels.pkl'

    test_image = caffe.io.load_image(sys.argv[1])
    predictions = classify_scene(MODEL_TYPE, WEIGHTS, LABELS, MEAN, test_image)
    for i, k in enumerate(predictions):
        print i, labels[k]