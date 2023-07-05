#!/usr/bin/env python3
#                                                                             
# PROGRAMMER: Ksenia Legostay
# DATE CREATED: 6/3/2023
# PURPOSE: A function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
from argparse import ArgumentParser

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """
    
    parser = ArgumentParser()

    parser.add_argument('--dir', type = str, default = 'pet_images/',
                        help = 'path to the folder of pet images')
    parser.add_argument('--arch', type = str, default = 'vgg',
                        help = 'model')
    parser.add_argument('--dogfile', type = str, default = 'dognames.txt',
                        help = 'file that contains dognames')
    
    return parser.parse_args()
