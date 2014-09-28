#!/usr/bin/env sh
# The directory structure assumed here is that the file is in the .../caffe/examples/faceclassification directory 
# It is also assumed that the leveldb directories are in the same location, where facetraindb and facetestdb are the locations of the train and test (or validation) directories
# PATH_IM is the location of the directories for training and testing images, which are referred to as 
PATH_IM=.
TOOLS=../../build/tools
# First create the leveldb for training set
$TOOLS/convert_imageset.bin -g $PATH_IM/database_train_v1/ $PATH_IM/database_train_v1/trainfile_list facetraindb 1 leveldb 40 40
# Create leveldb for testing set
$TOOLS/convert_imageset.bin -g $PATH_IM/database_test_v1/ $PATH_IM/database_test_v1/testfile_list facetestdb 1 leveldb 40 40
# Compute image mean
$TOOLS/compute_image_mean.bin facetraindb face_mean.binaryproto

GLOG_logtostderr=1 $TOOLS/train_net.bin face_solver.prototxt
