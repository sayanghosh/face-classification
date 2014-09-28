This repository contains Python scripts for downloading facial images from the Yale PubFig dataset at http://www.cs.columbia.edu/CAVE/databases/pubfig/, splitting them into training and test splits based on an user-defined split, resizing them to a target size and then writing them out into a Caffe
friendly file format, as well as Google Protocol Buffer files for defining training and tetsing networks and the optimization solver. The network configuration defined in these files has been found to give a 71% testing accuracy, which is close to state-of the art approaches, given that the facial images are in the wild.

Requirements 
================

1. Caffe, a library for training deep networks, please visit http://caffe.berkeleyvision.org

2. Python 2.7 or above, with Numpy and Scipy

Usage
================

1. Download development and evaluation URL lists dev_urls.txt and eval_urls.txt from http://www.cs.columbia.edu/CAVE/databases/pubfig/download/ 

2. Run read_pub_fig.py from the command line for retrieval of images from URLs as :

     python read_pub_fig.py datafile_name path 

datafile_name is the URL list file, dev_urls.txt or eval_urls.txt
path is the output directory where the downloaded images are stored

3. Run fileprocess.py to split the images into training and tets/development sets, specifying the input and output folders, and the Caffe listfile to be generated

4. Run train_face.sh to train the network, assuming that the directory is under /caffe/examples/
