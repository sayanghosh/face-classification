# -*- coding: utf-8 -*-
"""
fileprocess.py takes in a folder of images as input, splits them into training and
test sets, and then writes out the images along with list files containing image filenames and labels
"""

from scipy.misc import imread,imsave,imresize
from cStringIO import StringIO
from os import listdir
import re
from random import random

def image_resize(file_name,target_dimensions):
    """ 
    Function to get a file as input, resize it to 48*48 and crop a 40*40 part randomly from it
    Arguments :file_name : name of the file
                   target_dimensions : tuple containing the resized dimensions 
    """
    # Load the file into StringIO buffer
    img_array=imread(file_name,flatten=True)
    resize_img_array=imresize(img_array,target_dimensions)
    return resize_img_array
        
def split_and_write(split_perc,orig_dir,train_dir,test_dir,listfile_train,listfile_test,target_size): 
    """
    Function split_and_write takes in a path as argument, and then interates over each image,
    randomly choosing whether to put it in the train/test set and then creating listfiles for the train
    and test sets in the format "<FILE_NAME> <PERSON_LABEL>"
    Arguments:
        split_perc : Percentage of images to move into the test set
        orig_dir : Path where original image files are stored
        train_dir : Path where training image files are to be stored
        test_dir : Path where test image files are to be stored
        listfile_train : List file for training images 
        listfile_test : List file for test images
        target_size : Tuple for target image size
    """
    filelist=listdir(orig_dir)
    train_listfile_handle=open(listfile_train,"wt")
    test_listfile_handle=open(listfile_test,"wt")
    person_list=[] # Initialize an empty list of persons
    for file_name in filelist[:]: # Iterate over each file
        # Parse file name to extract name of the person
        person_name=file_name[file_name.find('__')+2:file_name.find('.jpg')]
        #print(file_name)
        # Change person_name suitably to replace the space character
        file_name_changed=file_name.replace(" ","_")
        
        # Add person name to dictionary if not present
        if person_name not in person_list:
            person_list.append(person_name)
        img=image_resize(orig_dir+file_name,target_size)    
        if random()<split_perc : #Decide on training set or test set
            # Write out test set
            imsave(test_dir+file_name_changed,img)
            test_listfile_handle.write(file_name_changed+" "+str(person_list.index(person_name))+"\n")
        else :  # Write out training set
            imsave(train_dir+file_name_changed,img)
            train_listfile_handle.write(file_name_changed+" "+str(person_list.index(person_name))+"\n")
    train_listfile_handle.close()
    test_listfile_handle.close()        
        
if __name__=='__main__':
    """ Configuration below used for our experiments """
    split_and_write(0.10,'.\orig_database\\','.\database_train_v1\\','.\database_test_v1\\','listfile_train','listfile_test',(40,40))
            
                    
        
