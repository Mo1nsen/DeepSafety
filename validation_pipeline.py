# This is the seed for your validation pipeline. It will allow you to load a model and run it on data from a directory.

# //////////////////////////////////////// Setup

import numpy as np
import tensorflow as tf
from sklearn.metrics import classification_report
import assign
import accuracy
import plot_file
import plot_graph 

# //////////////////////////////////////// Load model
model_name = "1650903661"
import_path = "/home/bart/home/DeepLearning/DeepSafety/tmp/saved_models/{}".format(int(model_name))
model = tf.keras.models.load_model(import_path)

# //////////////////////////////////////// Load data
# You will need to unzip the respective batch folders.
# Obviously Batch_0 is not sufficient for testing as you will soon find out.
data_root = "/home/bart/home/DeepLearning/DeepSafety/safetyBatches/Batch_6/"
batch_size = 32
img_height = 224
img_width = 224

test_ds = tf.keras.utils.image_dataset_from_directory(
  data_root,
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size,
  shuffle=False #Dat kann man bestimmt ändern
)

# Get information on your classes
class_names = np.array(test_ds.class_names)
print('Classes available: ', class_names)

# get the ground truth labels
test_labels = np.concatenate([y for x, y in test_ds], axis=0)

# Remember that we had some preprocessing before our training this needs to be repeated here
# Preprocessing as the tensorflow hub models expect images as float inputs [0,1]
normalization_layer = tf.keras.layers.Rescaling(1./255)
test_ds = test_ds.map(lambda x, y: (normalization_layer(x), y))  # Where x—images, y—labels.


# //////////////////////////////////////// Inference.
predictions = model.predict(test_ds)
predictions = np.argmax(predictions, axis=1)
print('Predictions: ', predictions)
test_labels = assign.assign(class_names, test_labels)# addded a function to assign the correct classes to the positions in the array 
print('Ground truth: ', test_labels)




print('Accuracy: ', accuracy.accuracy(predictions, test_labels))



for i in range(len(test_labels)):
  plot_file.log_in_file(test_labels[i], "Accuracy", accuracy.accuracy(predictions[i], test_labels[i]))
  plot_graph.plot_graph(test_labels[i], "Accuracy")

for name, acc in accuracy.class_accuracy(predictions, test_labels).items():
  plot_file.log_in_file(name, "class_accuracy", acc)
  plot_graph.plot_graph(name, "class_accuracy")

for name, acc in accuracy.precision(predictions, test_labels).items():
  plot_file.log_in_file(name, "precision", acc)
  plot_graph.plot_graph(name, "precision")

print(accuracy.class_accuracy(predictions, test_labels))
print(accuracy.precision(predictions, test_labels))
# There is more and this should get you started: https://www.tensorflow.org/api_docs/python/tf/keras/metrics
# However it is not about how many metrics you crank out, it is about whether you find the meangingful ones and report on them.
# Think about a system on how to decide which metric to go for..

# You are looking for a great package to generate your reports, let me recommend https://plotly.com/dash/