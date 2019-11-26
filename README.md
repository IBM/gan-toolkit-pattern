# Generating Fashion Images using GAN, without Writing Single Line of Code!

## Introduction 

Deep learning models used to perform classification tasks, are upper bounded by the number of images available in the training data. Data augmentation is often used to synthetically generated more data, looking very similar to the original data. GAN (Generative Advesarial Networks) are some state of the art models used for generating synthetic real-looking images. 

Fashion MNIST is a 10-class classification dataset which is a drop-in replacement for MNIST digit classification dataset. Plenty of deep learning models are trained for performing classification on Fashion MNIST dataset (https://developer.ibm.com/patterns/train-a-model-on-fashion-dataset-using-tensorflow-with-ffdl/). The performance of these classifiers could be improved, if the training dataset could be augmented with more images.

## How to Generate New Images

Consider, Deep Convolutional GAN (DCGAN) model which is a GAN for generating high quality fashion MNIST images. The DCGAN model is as shown below:
<p align="center">
<img src="images/dcgan.png" height="150" /> 
</p>

*Fig. 1: Deep Convolutional GAN model (DCGAN) for generating fashion images*

Let's try to implement the DCGAN model.

 - The  PyTorch  implementation  of  the  model  would  roughly  contain 150 lines  of  code (https://github.com/pytorch/examples/blob/master/dcgan/main.py)  
 - The Tensorflow implementation would require 500 lines of code (https://github.com/carpedm20/DCGAN-tensorflow/blob/master/model.py) 
  - Requires expertise in deep learning and Python libraries. 
  
However, we propose a simple JSON representation of defining a GAN model, extending the modules explained in the previous section. The most simplistic realization of the DCGAN architecture is shown below:

```json
{ 
    "generator":{
        "choice":"dcgan"
    },
    "discriminator":{
        "choice":"dcgan"
    },
    "data_path":"datasets/fmnist.p",
    "metric_evaluate":"MMD"
}
```
 or, we could customize this architecture by using a DCGAN-Generator and a Vanilla-Discriminator, as follows:

 ```json
{ 
    "generator":{
        "choice":"dcgan"
    },
    "discriminator":{
        "choice":"gan" #Just change the choice here! 
    },
    "data_path":"datasets/fmnist.p",
    "metric_evaluate":"MMD"
}
```

## Flow Diagram

![GAN Architecture](images/flow_diagram.png?raw=true "Modular GAN Architecture")
*Fig. 2: Modularized GAN architecture to be able to design any generator-discriminator combination in PyTorch*

## Featured Technologies

* [Python](https://www.python.org/): Python is a programming language that lets you work more quickly and integrate
your systems more effectively.
* [Flask](https://palletsprojects.com/p/flask/): A lightweight Python web application framework.
* [PyTorch](https://pytorch.org/): An open source machine learning framework that accelerates the path from research prototyping to production deployment.
* [Tensorflow](https://www.tensorflow.org/): An end-to-end open source machine learning platform.

## Build the Web App and Deploy in IBM Cloud

Follow these steps to setup and run this code pattern. The steps are
described in detail below.

1. [Create an account with IBM Cloud](#1-create-an-account-with-ibm-cloud)
2. [Install IBM Cloud CLI](#2-Install-IBM-Cloud-CLI)
3. [Login to your IBM Cloud account using CLI](#3-Login-to-your-IBM-Cloud-account-using-CLI)
4. [Setup the IBM Cloud Target Org and Space](#4-Setup-the-IBM-Cloud-Target-Org-and-Space)
5. [Clone the Git Repo](#5-Clone-the-Git-Repo)
6. [Create a GAN Config File](#6-Create-a-GAN-Config-File)
7. [Edit the Manifest File and ProcFile](#7-Edit-the-Manifest-File-and-ProcFile)
8. [Push the App to a new Python Runtime in IBM Cloud](#8-Push-the-App-to-a-new-Python-Runtime-in-IBM-Cloud)

### 1. Create an account with IBM Cloud

Sign up for IBM [**Cloud**](https://console.bluemix.net/). By clicking on create a free account you will get 30 days trial account.

### 2. Install IBM Cloud CLI

Download the [latest installer](https://github.com/IBM-Cloud/ibm-cloud-cli-release#downloads) for your specific OS and install the packge. To test the CLI, try running `ibmcloud help` in the terminal.

### 3. Login to your IBM Cloud account using CLI

Set up the IBM Cloud CLI Endpoint:
```
ibmcloud api https://api.ng.bluemix.net
```

Login to the IBM Cloud account:
```
ibmcloud login
```

### 4. Setup the IBM Cloud Target Org and Space

Setup the specific org, space, and resource group in which you would like to deploy the application.
```
ibmcloud target -o <org_name> -s <space_name> -g <resource_group_name>
```

### 5. Clone the Git Repo

Clone the entire code repository

    ```shell
    $ git clone https://github.ibm.com/DARVIZ/gan-toolkit-code-patterns
    $ cd gan-toolkit-code-patterns
    ```

### 6. Create a GAN Config File

The config file is a set of key-value pairs in JSON format. A collection of sample config files are provided [here](./agant/configs/)

The basic structure of the `config` json file is as follows,
```Javascript
    { 
        "generator":{
            "choice":"gan"
        },
        "discriminator":{
            "choice":"gan"
        },
        "data_path":"datasets/dataset1.p",
        "metric_evaluate":"MMD"
    }
```
The detailed documentation of the config files are provided [here](https://github.com/IBM/gan-toolkit/wiki/Config-File-Structure-and-Details)

### 7. Edit the Manifest File and ProcFile

Edit `manifest.yaml` in your root folder with the following content,
```
domain: mybluemix.net
name: <application-name>
host: <application-name>
```
_Note: The `application-name` has to be unique at the entire IBM Cloud level_

Edit `Procfile` in your root folder with the path of your GAN config file,
```
web: python agant/main.py --config <path-to-your-GAN-Config-File>
```

### 8. Push the App to a new Python Runtime in IBM Cloud

```
ibmcloud app push <application-name> -b python_buildpack -f manifest.yaml
```
_Note: The app requires atleast 1GB in memory quota. The maximum memory quota for a `Lite account` is 256 MB and can be increased only by upgrading to a billable account._

### 9. Obtain the GAN Generated Images and Ouput 
Default input and output paths (override these paths in the GAN config file)
    `logs/` : training logs
    `saved_models/` : saved trained models
    `train_results/` : saved all the intermediate and final generated images
    `datasets/` : input dataset path 

## (Or) Run Locally

0. (Optional) If you want to setup an anaconda environment

    a. Install Anaconda from [here](https://conda.io/docs/user-guide/install/index.html#installing-conda-on-a-system-that-has-other-python-installations-or-packages)

    b. Create a conda environment
    ```shell
    $ conda create -n gantoolkit python=3.6 anaconda
    ```

    c. Activate the conda environment
    ```shell
    $ source activate gantoolkit
    ```

1. Clone the code

    ```shell
    $ git clone https://github.com/IBM/gan-toolkit
    $ cd gan-toolkit
    ```

2. Install all the requirements. Tested for Python 3.5.x+

    ```shell
    $ pip install -r requirements.txt
    ```

3. Train the model using a configuration file. (Many samples are provided in the `configs` folder)

    ```shell
    $ cd agant
    $ python main.py --config configs/gan_gan.json
    ```

4. Default input and output paths (override these paths in the config file)
    `logs/` : training logs
    `saved_models/` : saved trained models
    `train_results/` : saved all the intermediate generated images
    `datasets/` : input dataset path 

## Analyze Results

The trained GAN model generates new images that looks very similar to the input dataset, it was trained on. The new generated images are found in the disk, in the `agant/train_results/` folder. The obtained results and the newly generated images look like the following:

<p align="center">
<img src="images/dcgan-dcgan.png" width="250" height="250" /> <img src="images/dcgan-gan.png" width="250" height="250" />
</p>

*Fig. 3: (Left) Fashion images generated using DCGAN model. (Right) Fashion images generated using customized DCGAN-generator and GAN-discriminator*


# Related IBM Developer content
* [Waton Studio](https://www.ibm.com/cloud/watson-studio)
* [Neural Network Modeller](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-canvas-nnd-nodes.html)

# Related links
* [Neural Network Modeller: HowTo](https://www.youtube.com/watch?v=EDQ0AWcUBnE)
* [AuthorGAN: Improving GAN Reproducibility using a Modular GAN Framework](http://learningsys.org/neurips19/schedule.html)
* Vanilla GAN: Generative Adversarial Learning ([Goodfellow et al., 2014](https://arxiv.org/abs/1406.2661))
* C-GAN: Conditional Generative Adversarial Networks ([Mirza et al., 2014](https://arxiv.org/abs/1411.1784))
* DC-GAN: Deep Convolutional Generative Adversarial Network  ([Radford et al., 2016](https://arxiv.org/abs/1511.06434))
* W-GAN: Wasserstein GAN    ([Arjovsky et al., 2017](https://arxiv.org/abs/1701.07875))
* W-GAN-GP: Improved Training of Wasserstein GANs  ([Goodfellow et al., 2017](https://arxiv.org/abs/1704.00028))

# Acknowledgement
Acknowledging the contributions of our academic collaborators
 - [Prof. Mayank Vatsa](https://www.linkedin.com/in/mayankvatsa/) (IIIT Delhi)
 - [Prof. Richa Singh](https://www.linkedin.com/in/richa-singh-40ba237/?originalSubdomain=in) (IIIT Delhi)

## License
This code pattern is licensed under the Apache Software License, Version 2. Separate third-party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1 (DCO)](https://developercertificate.org/) and the [Apache Software License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

[Apache Software License (ASL) FAQ](https://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN)
