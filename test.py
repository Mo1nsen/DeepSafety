import plot_file
import plot_graph
import accuracy
from mapping import *

test_labels = [1, 2, 3, 2, 1, 5, 3, 2, 5, 6, 8 ,8, 9]
predictions = [1, 2, 2, 3, 1, 5, 2, 1, 5, 6, 8, 7, 9]

#test_labels = [2, 5, 3, 2, 4, 5, 3, 2, 7, 6, 8 ,8, 9]
#predictions = [2, 5, 2, 2, 4, 5, 3, 2, 5, 6, 8, 8, 4]

print(accuracy.class_accuracy(predictions, test_labels))

for i in range(len(test_labels)):
  plot_file.log_in_file(test_labels[i], "Accuracy", accuracy.accuracy(predictions[i], test_labels[i]))
  plot_graph.plot_graph(test_labels[i], "Accuracy")

for name, acc in accuracy.class_accuracy(predictions, test_labels).items():
  plot_file.log_in_file(name, "class_accuracy", acc)
  plot_graph.plot_graph(name, "class_accuracy")

for name, acc in accuracy.precision(predictions, test_labels).items():
  plot_file.log_in_file(name, "precision", acc)
  plot_graph.plot_graph(name, "precision")