#!/bin/sh       
#                                                                   
# PROGRAMMER: Ksenia Legostay
# DATE CREATED: 6/4/2023      
# PURPOSE: Runs all three models to test which provides 'best' solution on the Uploaded Images.
#          The output from each run has been piped into a text file.
#
# Usage: sh run_models_batch_uploaded.sh    -- will run program from commandline within Project Workspace
#  
python check_images.py --dir uploaded_images/ --arch resnet  --dogfile dognames.txt > output/resnet_uploaded-images.txt
python check_images.py --dir uploaded_images/ --arch alexnet --dogfile dognames.txt > output/alexnet_uploaded-images.txt
python check_images.py --dir uploaded_images/ --arch vgg  --dogfile dognames.txt > output/vgg_uploaded-images.txt
