#!/usr/bin/env python3
#
# PROGRAMMER: Ksenia Legostay
# DATE CREATED: 6/4/2023
# PURPOSE: Create a function calculates_results_stats that calculates the
#          statistics of the results of the programrun using the classifier's model
#          architecture to classify the images. This function will use the
#          results in the results dictionary to calculate these statistics.
#         This function creates and returns the Results Statistics Dictionary with the following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs


def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model
    architecture to classifying pet images. Then puts the results statistics in a
    dictionary so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value.
                     Counts:
                        Number of Images
                        Number of Dog Images
                        Number of "Not-a" Dog Images
                     Percentages:
                        % Correctly Classified Dog Images
                        % Correctly Classified "Not-a" Dog Images
                        % Correctly Classified Breeds of Dog Images
    """

    results_stats_dic = dict()

    n_images = len(results_dic)
    n_pet_dog = 0
    n_class_cdog = 0
    n_class_cnotd = 0
    n_match_breed = 0

    for key in results_dic:
        if results_dic[key][2] == 1:
            # isa dog (pet label) & breed match
            if results_dic[key][3] == 1:
                n_pet_dog += 1
                # isa dog (classifier label) & breed match
                if results_dic[key][4] == 1:
                    n_class_cdog += 1
                    n_match_breed += 1

            # NOT dog (pet_label)
            else:
                # NOT dog (classifier label)
                if results_dic[key][4] == 0:
                    n_class_cnotd += 1

        # NOT - match (not a breed match if a dog)
        else:
            # NOT - match
            # isa dog (pet label)
            if results_dic[key][3] == 1:
                n_pet_dog += 1
                # isa dog (classifier label)
                if results_dic[key][4] == 1:
                    n_class_cdog += 1

            # NOT dog (pet_label)
            else:
                # NOT dog (classifier label)
                if results_dic[key][4] == 0:
                    n_class_cnotd += 1

    results_stats_dic["n_images"] = n_images
    results_stats_dic["n_dogs_img"] = n_pet_dog
    n_pet_notd = n_images - n_pet_dog
    results_stats_dic["n_notdogs_img"] = n_pet_notd
    results_stats_dic["pct_correct_dogs"] = (n_class_cdog / n_pet_dog) * 100
    if n_pet_notd:
        results_stats_dic["pct_correct_notdogs"] = (n_class_cnotd / n_pet_notd) * 100
    else:
        results_stats_dic["pct_correct_notdogs"] = 0
    results_stats_dic["pct_correct_breed"] = (n_match_breed / n_pet_dog) * 100

    return results_stats_dic
