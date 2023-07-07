#!/usr/bin/env python3
#
# PROGRAMMER: Ksenia Legostay
# DATE CREATED: 6/3/2023
# PURPOSE: Create a function classify_images that uses the classifier function
#          to create the classifier labels and then compares the classifier
#          labels to the pet image labels.
#          This function uses the extend function to add items to the list
#          that's the 'value' of the results dictionary.
#
##
# Imports classifier function for using CNN to classify images

from classifier.classifier import classifier


def classify_images(images_dir, results_dic, model):
    """
    Compares pet labels to the classifier labels, and adds the classifier label and the comparison of
    the labels to the results dictionary using the extend function.
    Parameters:
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items:
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """

    for filename in results_dic:
        full_image_path = images_dir + filename

        image_classification = classifier(full_image_path, model)
        # add index 1 = classifier label (string)
        results_dic[filename].append(image_classification.lower().strip())

        image_classification_list = image_classification.lower().strip().split(", ")

        if results_dic[filename][0] in image_classification_list:
            # index 2 = 1/0 (int)  where 1 = match between pet image and classifer labels
            results_dic[filename].append(1)
        else:
            # index 2 = 1/0 (int)  where 0 = no match between labels
            results_dic[filename].append(0)
