#!/usr/bin/env python3
#
# PROGRAMMER: Ksenia Legostay
# DATE CREATED: 6/3/2023
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task.
#          Note that the true identity of the pet (or object) in the image is
#          indicated by the filename of the image.
##

# Imports python modules
from time import time
import os.path
import pandas as pd

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results
from print_functions_for_lab_checks import *


def main():
    start_time = time()

    # 1. Function that checks command line arguments using in_arg
    # Folder that contains the pet images --dir
    #     pet_images/
    # The CNN model architecture to use --arch
    #     resnet, alexnet, or vgg (pick one as the default). You will find them in classifier.py.
    # The file that contains the list of valid dognames --dogfile
    #     input/dognames.txt
    in_arg = get_input_args()

    check_command_line_arguments(in_arg)

    # 2. Creates a dictionary of pet labels based upon the filenames of the image files.
    results = get_pet_labels(in_arg.dir)

    check_creating_pet_image_labels(results)

    # 3. Creates Classifier Labels with classifier function, Compares Labels, and adds these results to the results dictionary
    classify_images(in_arg.dir, results, in_arg.arch)

    # Function that checks Results Dictionary using results
    check_classifying_images(results)

    # 4. Adjusts the results dictionary to determine if classifier correctly classified images as 'a dog' or 'not a dog'.
    # This demonstrates if the model can correctly classify dog images as dogs (regardless of breed)
    adjust_results4_isadog(results, in_arg.dogfile)

    # Function that checks Results Dictionary for is-a-dog adjustment using results
    check_classifying_labels_as_dogs(results)

    # 5. Calculates results of run and puts statistics in the Results Statistics
    results_stats = calculates_results_stats(results)

    # Function that checks Results Statistics Dictionary using results_stats
    check_calculating_results(results, results_stats)

    # 6. Prints summary results, incorrect classifications of dogs (if requested) and incorrectly classified breeds (if requested)
    print_results(results, results_stats, in_arg.arch, True, True)

    # 7. Write the stats of the model to the model comparison file
    header = [
        "CNN Model Architecture:",
        "% Not-a-Dog Correct",
        "% Dogs Correct",
        "% Breeds Correct",
    ]
    df = pd.DataFrame(
        [
            [
                in_arg.arch,
                results_stats["pct_correct_notdogs"],
                results_stats["pct_correct_dogs"],
                results_stats["pct_correct_breed"],
            ]
        ],
        columns=header,
    )
    if os.path.isfile("models_comparison/models_comparison.csv"):
        df.to_csv(
            "models_comparison/models_comparison.csv",
            mode="a",
            header=False,
            index=False,
        )
    else:
        df.to_csv("models_comparison/models_comparison.csv", header=True, index=False)
    ###

    end_time = time()

    tot_time = end_time - start_time

    print(
        "\n** Total Elapsed Runtime:",
        str(int((tot_time / 3600)))
        + ":"
        + str(int((tot_time % 3600) / 60))
        + ":"
        + str(int((tot_time % 3600) % 60)),
    )


if __name__ == "__main__":
    main()
