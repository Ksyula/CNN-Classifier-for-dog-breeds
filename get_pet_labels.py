#!/usr/bin/env python3
#
# PROGRAMMER: Ksenia Legostay
# DATE CREATED: 6/3/2023
# PURPOSE: A function get_pet_labels creates the pet labels from the image's filename. This function inputs:
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    ## Retrieve the filenames from folder
    filename_list = listdir(image_dir)

    ## Creates empty dictionary named results_dic
    results_dic = dict()

    for idx in range(len(filename_list)):
        if filename_list[idx] not in results_dic:
            low_pet_image = filename_list[idx].lower()
            word_list_low_pet_image = low_pet_image.split("_")

            pet_name = ""

            for word in word_list_low_pet_image:
                if word.isalpha():
                    pet_name += word + " "

            results_dic[filename_list[idx]] = [pet_name.strip()]

    return results_dic
