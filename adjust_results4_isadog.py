#!/usr/bin/env python3
#                                                                             
# PROGRAMMER: Ksenia Legostay
# DATE CREATED: 6/4/2023
# PURPOSE: The function adjusts the results dictionary to indicate whether or not the pet image 
#          label is of-a-dog, and to indicate whether or not the classifier image label is of-a-dog. 
#          All dog labels from both the pet images and the classifier function will be found in the dognames.txt file. 

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files.
    Returns:
           None - results_dic is mutable data type so no return needed.
    """

    dog_names = dict()

    with open(dogfile) as f:
        for line in f:
            if "," in line:
                names_list = line.split(", ")
                for name in names_list:
                    dog_names[name.strip()] = 1
            else:
                dog_names[line.strip()] = 1

    # index 3 = 1/0 (int) where 1 = pet image 'is-a' dog and 0 = pet Image 'is-NOT-a' dog. 
    for key in results_dic:
        if dog_names.get(results_dic[key][0], 0):
            is_dog = 1
        else:
            is_dog = 0
        results_dic[key].append(is_dog)
            
    # index 4 = 1/0 (int)  where 1 = Classifier classifies image 'as-a' dog and 0 = Classifier classifies image 'as-NOT-a' dog.
    for key in results_dic:
        for dog in results_dic[key][1].lower().split(", "):
            if dog_names.get(dog, 0):
                is_dog = 1
                break
            else:
                is_dog = 0
        results_dic[key].append(is_dog)