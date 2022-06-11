import tensorflow as tf

def class_accuracy(predictions, test_labels): #how accurate is the ai on certain classes

    class_predictions = {}
    class_accuracies = {}

    for prediction, test_label in zip(predictions, test_labels):
        if test_label in class_predictions:#if we have already put something of that class in class predictions
            class_predictions[test_label].append(prediction == test_label)#appends a true or false to the array so that we can count the matches later
        else:#if it is a "new" class then we have to put something at the first position first
            class_predictions[test_label] = [prediction == test_label]

    for k, v in class_predictions.items():
        count = 0
        for match in v:#checks for true in our class_predictions
            if match:
                count += 1         
        class_accuracies[k] = count/len(v)#this gives the accuracy as we divide the amount of true values by all values

    return class_accuracies


def accuracy(predictions, test_labels): #how accurate is the ai overall
    
    metric = tf.keras.metrics.Accuracy()
    metric.update_state(predictions, test_labels)

    return metric.result().numpy()

def precision(predictions, test_labels): #how often is the class correct if the ai thinks it is a certain class (true positives/(false+true positives))
    class_predictions = {}
    class_accuracies_pre = {}

    for prediction, test_label in zip(predictions, test_labels):#more or less the same as above but now we check the predictions and not the ground truths
        if prediction in class_predictions:
            class_predictions[prediction].append(prediction == test_label)#appends true or false, true if the prediction predicted the class correctly and falls if it thought it was a certain class but it wasnt
        else:
            class_predictions[prediction] = [prediction == test_label]

    for k, v in class_predictions.items():
        count = 0
        for match in v:
            if match:
                count += 1         
        class_accuracies_pre[k] = count/len(v)#now we divide the amount of true positives by the amount of true and false positives

    return class_accuracies_pre