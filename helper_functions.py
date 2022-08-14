# Create function to unzip a zipfile into current working directory
# (since we're going to be downloading and unzipping a few files)
import zipfile

def unzip_data(filename,data_dir="data"):
    """
    Unzips filename into the current working directory.
    Args:
        filename (str): a filepath to a target zip folder to be unzipped.
    """
    zip_ref = zipfile.ZipFile(filename, "r")
    zip_ref.extractall(data_dir)
    zip_ref.close()

# Plot the validation and training data separately
import matplotlib.pyplot as plt

def plot_loss_curves(history):
    """
    Shows separate loss curves for training and validation metrics.
    Args:
    history: TensorFlow model History object (see: https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/History)
    """
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    accuracy = history.history['accuracy']
    val_accuracy = history.history['val_accuracy']
    epochs = range(len(history.history['loss']))
    # Plot loss
    plt.plot(epochs, loss, label='training_loss')
    plt.plot(epochs, val_loss, label='val_loss')
    plt.title('Loss')
    plt.xlabel('Epochs')
    plt.legend()
    # Plot accuracy
    plt.figure()
    plt.plot(epochs, accuracy, label='training_accuracy')
    plt.plot(epochs, val_accuracy, label='val_accuracy')
    plt.title('Accuracy')
    plt.xlabel('Epochs')
    plt.legend();

# Function to evaluate: accuracy, precision, recall, f1-score
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

def get_metrics(y_true, y_pred):
    """
    Calculates model accuracy, precision, recall and f1 score of a binary classification model.

    Args:
        y_true: true labels in the form of a 1D array
        y_pred: predicted labels in the form of a 1D array
    Returns:
        a dictionary of accuracy, precision, recall, f1-score.
    """
    # Calculate model accuracy
    model_accuracy = accuracy_score(y_true, y_pred) * 100
    # Calculate model precision, recall and f1 score using "weighted average
    model_precision, model_recall, model_f1, _ = precision_recall_fscore_support(y_true, y_pred, average="weighted")
    model_results = {"accuracy": model_accuracy,
                    "precision": model_precision,
                    "recall": model_recall,
                    "f1": model_f1}
    return model_results

# Generate a metrics report (plots confusion matrix optionally)
from sklearn.metrics import confusion_matrix
import seaborn as sns

def gen_metrics_report(y_true,y_pred,plot_confusion_matrix=True):
    """Generates a metrics report,
       should be used with classification problem.

    Args:
        y_true (ArrayLike): An array of truth labels
        y_pred (ArrayLike): An array of predictions, should be of same shape as y_true
        plot_confusion_matrix (bool, optional): Plots confusion matrix as a heatmap. Defaults to True.
    """

    print(f"Accuracy: {accuracy_score(y_true, y_pred) * 100}")
    model_precision, model_recall, model_f1, _ = precision_recall_fscore_support(y_true, y_pred, average="weighted")
    print(f"Precision: {model_precision}")
    print(f"Recall: {model_recall}")
    print(f"F1-score: {model_f1}")

    if plot_confusion_matrix:
        conf_mat = confusion_matrix(y_true,y_pred)
        sns.heatmap(conf_mat, annot=True,cmap="Blues")
        plt.title("Confusion matrix heatmap")