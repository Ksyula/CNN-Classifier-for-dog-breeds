#!/bin/sh
#                                                                             
# PROGRAMMER: Ksenia Legostay
# DATE CREATED: 6/5/2023
# PURPOSE: Runs all three models to test which provides 'best' solution.
#          The output from each run has been piped into a text file.
#
# Usage: sh run_models_batch.sh    -- will run program from commandline within Project Workspace
#  
python check_images.py --dir pet_images/ --arch resnet  --dogfile dognames.txt > output/resnet_pet-images.txt
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > output/alexnet_pet-images.txt
python check_images.py --dir pet_images/ --arch vgg  --dogfile dognames.txt > output/vgg_pet-images.txt
