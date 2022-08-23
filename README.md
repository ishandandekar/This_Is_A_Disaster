[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ishandandekar/This_Is_A_Disaster/blob/main/This_Is_A_Disaster_nbk.ipynb)

# This_Is_A_Disaster

:wave: Hello and welcome to **This_Is_A_Disaster**. This is my first natural-language-processing project and also my first attempt to a formal machine-learning competition! My personal best was rank 229 :smile:.

## Introduction

In this project, I try to classify tweets which are related to a natural disaster or not. I make an attempt on the **`nlp-getting-started`** competition available on Kaggle. Check the competition [here](https://www.kaggle.com/competitions/nlp-getting-started/overview). The objective of the competition was to classify whether a tweet is related to a natural disaster or not. The target is set as `1` if the tweet is related to a disaster and `0` otherwise.

## Data

The dataset was given by the competition organisers (Kaggle) themselves. The data contained the text and some information about the tweets, which could benefit modelling experiments adn thus, the predictions. The comptition made a training, test and sample submission csv(s) available. The training csv contained five columns which were: _id_ (id of the row), _text_ (containing the actual text/tweet), _location_ (the location of the tweet was sent from), _keyword_ (particular keyword from the tweet), _target_ (`1` if the text was related to a disaster, `0` otherwise). The test csv did not contain the target column. The competition required us to submit the predictions on the test csv. The submission were required in a typical format. Sample submission csv had the format in which they wanted the submissions. For evaluating models validation set was created using the training samples itself.

## Models

I made three models using Tensorflow library. Instead of making a `TextVectozier` and `Embedding` layer, I used a pretrained **[USE](https://tfhub.dev/google/universal-sentence-encoder/4)** to convert text-to-vectors. All of these models were compiled using binary cross-entropy loss, which is best suited for binary classification problems, and Adam optimizer.

- **Model 0**: For the first experiment, I used the **USE** as a layer to convert text-to-vectors. I set the trainable parameter as False, so that the weightsin the pretraine module don't change. I added a dense layer with 64 neurons with ReLU activation function, to add more trainable parameters. As an output layer, I added a Dense layer with 1 neuron with sigmoid activation function to finally classify the tensors. After evaluating the model on validation set, it gave an accuracy of 82%.
- **Model 1**: For the next iteration, I used the same architecture, but added a Dropout layer to regularize the neural network. I also added another Dense layer with 64 neurons using ReLU activation.
- **Model 2**: As a last try I wanted to train a model on the whole training set (before validation split). Due to this, I could not evaluate the model on the valdiation set (data leakage issue). I could not add callbacks during training stage (callbacks depend on the loss and accuracy on the validation set). Although, this is alarming but I wanted to know how will it perform on the test set.

> Check the notebook to see how these models performed the test data.

## Future development

This was my first attempt to a NLP competition. A web app with the best performing model would be great. I would also like to add a web scraper such that, if you add the tweets's URL the scraper would extract the text. This is to make the web app more automated. I would also like to do more modelling experiments to get better score in the competitions.

## Tools and libraries

- Python
- Keras
- Kaggle
- Tensorflow
- Pandas
- Git and Github

## Contents of the repository

- _.gitignore_ : To get the data into Colab notebook I used Kaggle API. The API needs keys which were obtained via Kaggle itself. As this is a private key I omitted to upload the `.json` file using `.gitignore` file.
- _helper_functions.py_ : This python script contains various functions which were required during the modelling experiments.
- _README.md_ : This is a markdown file which is used to document the project. This is displayed on the repository page on Github.
- _This_Is_A_Disaster_nbk.ipynb_ : This is the jupyter/ Colab notebook used for the competition. The notebook has been modified to make it more beautiful and readable.
  > :warning:**Note** : The last run of this notebook is dated 23 August '22. The evaluation of these models have been done by the results which were present on this date only.

## Contributions

I appreciate feedback on potential improvements and/or if you see an error that I've made! If you would like to contribute on improveing the code or even the documentation then do a pull request with the notebook and helper functions! and help in the future development :smile: If you have any doubts regarding the code, make sure to add an 'Issue' in the issues tab of the repository and I'll get to it as soon as I can.

A special thanks to [Daniel Bourke](https://www.mrdbourke.com/) for this project.
