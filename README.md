[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ishandandekar/This_Is_A_Disaster/blob/main/This_Is_A_Disaster_nbk.ipynb)

# This_Is_A_Disaster

:wave: Hello and welcome to **This_Is_A_Disaster**. This is my first natural-language-processing project. Also, make sure to visit the official website of this project.

## Introduction

In this project, I try to classify tweets which are related to a natural disaster or not. I make an attempt on the **`nlp-getting-started`** competition available on Kaggle. Check the competition [here](https://www.kaggle.com/competitions/nlp-getting-started/overview). In this competition, we have to classify whether these tweets are about a natural disaster. I use neural networks, create models and try to improve on them using various layers and methods.

## Data

The dataset was given by the competition organisers (Kaggle) themselves. The data contained the text and some information about the tweets, which could benefit modelling experiments adn thus, the predictions. The comptition made a training, test and sample submission csv(s) available. The training csv contained five columns which were: _id_ (id of the row), _text_ (containing the actual text/tweet), _location_ (the location of the tweet was sent from), _keyword_ (particular keyword from the tweet), _target_ (`1` if the text was related to a disaster, `0` otherwise). The test csv did not contain the target column. The competition required us to submit the predictions on the test csv. The submission were required in a typical format. Sample submission csv had the format in which they wanted the submissions. For evaluating models validation set was created using the training samples itself.

## Models

I made three models using Tensorflow library. Instead of making a `TextVectozier` and `Embedding` layer, I used a pretrained **[USE](https://tfhub.dev/google/universal-sentence-encoder/4)** to convert text-to-vectors. All of these models were compiled using binary cross-entropy loss and Adam optimizer.

- Model 0: For the first experiment, I used the **USE** as a layer to convert text-to-vectors. I set the trainable parameter as False, so that the weightsin the pretraine module don't change. I added a dense layer with 64 neurons with ReLU activation function, to add more trainable parameters. As an output layer, I added a Dense layer with 1 neuron with sigmoid activation function to finally classify the tensors. After evaluating the model on validation set, it gave an accuracy of 82%.
- Model 1: For the next iteration, I used the same architecture, but added a Dropout layer to regularize the neural network. I also added another Dense layer with 64 neurons using ReLU activation.

## App

## Future development

## Tools and libraries

## Contents of the repository

#### TODO:

- [ ] Update documentation
- [x] Finish notebook
- [x] Make **Open in colab** button to open notebook
- [ ] Get model
- [ ] Get some examples (tweets from tests set for the web app)
