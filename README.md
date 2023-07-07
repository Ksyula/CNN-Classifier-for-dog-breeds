# :dog: Dog Breed Classification

This repository contains code and resources to help you classify dog images and identify their specific breeds using [Convolutional Neural Networks](https://en.wikipedia.org/wiki/Convolutional_neural_network) (CNNs).

<p float="left">
  <img src="pet_images/Dalmatian_04068.jpg" width="200" />
  <img src="pet_images/Collie_03797.jpg" width="200" /> 
  <img src="pet_images/Beagle_01170.jpg" width="200" />
</p>

- [:dog: Dog Breed Classification](#dog-dog-breed-classification)
  - [Description](#description)
  - [Features](#features)
  - [Project Structure](#project-structure)
  - [Getting Started](#getting-started)
    - [1. Set up the Environment](#1-set-up-the-environment)
    - [2. Classify Images Using the Service](#2-classify-images-using-the-service)
    - [3. Batch Classification](#3-batch-classification)
  - [How Does It Work](#how-does-it-work)
  - [Performance Comparison of CNN Models](#performance-comparison-of-cnn-models)
  - [Classify Your Own Image](#classify-your-own-image)


## Description
This service utilizes pre-trained CNN models to accurately determine whether an image represents a dog, and if so, it further predicts the specific breed of the dog. By leveraging state-of-the-art deep learning techniques, the service offers robust and accurate classification results.

## Features
The Dog Breed Classification service provides the following features:

1. **Dog Image Detection:** Given an input image, the service determines whether the image contains a dog or not.
2. **Breed Identification:** If the image is identified as a dog, the service performs breed classification and provides the predicted breed of the dog.

## Project Structure
```
classifier                        # application of torchvision models
   |-- classifier.py
   |-- test_classifier.py
utils                             # utils for extracting arguments, labels, producing results and checking the code
   |-- adjust_results4_isadog.py
   |-- calculates_results_stats.py
   |-- get_input_args.py
   |-- get_pet_labels.py
   |-- print_functions_for_lab_checks.py
   |-- print_results.py
input                             # .txt files with dog breeds
output                            # .txt files with model performance and results of classification
models_comparison                 # .csv with performances comparison of different classificators        

pet_images                        # folder with images of animals for a model evaluation
uploaded_images                   # folder to upload your images to classify them

check_images.py                   # main script with general logic of the service
classify_images.py                # script for calling a classifier for images

requirements.txt                  # environmental requirements

run_models_batch.sh               # script to run models evaluation in a batch
run_models_batch_uploaded.sh      # script to produce models inferences for uploaded images
```

## Getting Started

To get started with the Dog Breed Classification Service, please follow the steps below:

### 1. Set up the Environment
Before using the service, ensure that you have the required dependencies installed in a virtual environment. Follow these steps:

* If you don't already have virtualenv installed, run the following command:
```
pip install virtualenv
```
* Create a new virtual environment by executing the following command:
```
virtualenv venv
```
* Activate the virtual environment by running the appropriate command based on your operating system:
  - On Unix/Linux:
        ```
        source venv/bin/activate
        ```
  - On Windows:
        ```
        venv\Scripts\activate
        ```
* Install the necessary dependencies by executing the following command:
```
pip install -r requirements.txt
```

### 2. Classify Images Using the Service
To classify images and determine the breed of dogs, you can utilize the service via the terminal. Follow these steps:

* Ensure that you have activated the virtual environment.
* Run the following command to execute the service:
```
python3 check_images.py --dir pet_images/ --arch vgg --dogfile input/dognames.txt
```
Use default parameters from terminal call or customise them: 
  - Folder that contains the pet images `--dir`
          `pet_images/`
          `uploaded_images/`
  - The CNN model architecture to use `--arch`
          `resnet` 
          `alexnet`
          `vgg`
  - The file that contains the list of valid dognames `--dogfile`
          `input/dognames.txt`

### 3. Batch Classification
Run bash script to classify the images with 3 different CNN models:
```
sh run_models_batch.sh
```
check the generated statistics per CNN model architecture in the `output/` folder.

## How Does It Work
The Dog Breed Classification Service employs a set of pre-trained CNN models to classify dog images and predict their breeds. Here's an overview of the process:

1. **Image Label Extraction:** The service extracts the pet image label from the filename. It assumes that the filename contains the label information, which is typically the breed of the dog. For example, if the filename is "golden_retriever_01.jpg," the extracted label would be "golden retriever."

2. **Image Classification:** After extracting the image label, the service proceeds to classify the image using a pre-trained CNN model. The CNN model has been trained on a large dataset of dog images and is capable of recognizing various dog breeds. The image is fed into the model, and the service obtains a probability distribution over different dog breeds.

3. **Breed Prediction:** Based on the probability distribution generated by the CNN model, the service predicts the most likely breed of the dog in the submitted image. The breed with the highest probability is selected as the predicted breed.

4. **Model Comparison:** The Dog Breed Classification Service goes a step further by comparing the performance of three different CNN model architectures. These models have been trained using various techniques and architectures to improve classification accuracy. The service evaluates the performance of each model and provides a comparison of their results.

5. **Summary Statistics:** To assist users in understanding the comparative performance of the CNN models, the service generates short summary statistics. These statistics can be found in the `models_comparison/` folder and provide insights into the accuracy and effectiveness of each model in classifying dog breeds.


## Performance Comparison of CNN Models

In this image classification task, we have used three different pre-trained CNN models with distinct architectures. The table below presents the evaluation results for the comparison of these models:

| CNN Model Architecture | % Not-a-Dog Correct | % Dogs Correct | % Breeds Correct |
|-------------|:-----:|------:|------|
| **RESNET**  |  90.0 | 100.0 | 90.0 |
| **ALEXNET** | 100.0 | 100.0 | 80.0 |
| **VGG**     | 100.0 | 100.0 | 93.3 |

Based on the performance comparison, the **VGG** model architecture demonstrated the best performance in classifying the dog breeds on a sample of the images from the `pet_images/` folder. It achieved the highest accuracy in identifying the correct dog breeds compared to the **RESNET** and **ALEXNET** architectures.

## Classify Your Own Image
Follow these steps:

1. **Upload Your Images:** Place your images in the `uploaded_images/` folder. Ensure that your images meet the following image requirements:
   - Images should be in JPEG format with the extension `.jpg`.
   - Images should be approximately square in shape, meaning their height and width have approximately the same number of pixels.
   - Follow the naming convention for your images. The name format should be `object_number.jpg`. If the animal name consists of multiple words, separate them with an underscore `_`. For example: `Dog_01.jpg`, `Animal_Name_25.jpg`, `Black_bear_01.jpg`, `Coffee_mug_01.jpg`.
Note that you can upload images of dogs, animals, or even objects. The service will indicate if the image does not contain a dog.

2. **Run the Classifiers:** To classify the uploaded images using the different CNN models, follow these options:
* Option 1: Manual Execution from Terminal
```
python check_images.py --dir uploaded_images/ --arch resnet --dogfile input/dognames.txt > output/resnet_uploaded-images.txt
python check_images.py --dir uploaded_images/ --arch alexnet --dogfile input/dognames.txt > output/alexnet_uploaded-images.txt
python check_images.py --dir uploaded_images/ --arch vgg --dogfile input/dognames.txt > output/vgg_uploaded-images.txt
```
* Option 2: Automated Execution via Bash Script
```
sh run_models_batch_uploaded.sh
```
These commands will run the three different classifiers on the uploaded images and generate result files in the `output/` folder.
