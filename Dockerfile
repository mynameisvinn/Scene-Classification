FROM floydhub/dl-docker:cpu

COPY . /root/caffe

RUN cd /root/caffe/models_places

RUN wget http://places2.csail.mit.edu/models_places365/alexnet_places365.caffemodel

RUN wget https://raw.githubusercontent.com/metalbubble/places365/master/deploy_alexnet_places365.prototxt