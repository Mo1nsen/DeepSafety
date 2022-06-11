def assign(class_names, test_labels):#class_names has the "names" of the classes that appear in the validation in it | test_labels is basically a linspace from 0 to the number of classes-1
    for i in range(len(test_labels)):
        test_labels[i] = class_names[test_labels[i]]
    return test_labels