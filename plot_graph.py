import matplotlib.pyplot as plt
from mapping import *
import numpy as np
import os

def plot_graph(class_label, metric_name):

    class_name: str = mapping[class_label]
    file_name: str = class_name + "_" + metric_name + ".txt"
    path_to_file: str = "Plots/" + metric_name + "_Plots/Textfiles/" + file_name
    path_to_plot: str = "Plots/" + metric_name + "_Plots/Graphs/" + file_name.rstrip(".txt")

    x_axis = []
    y_axis = []

    try:
        os.remove(path_to_plot)
    except FileNotFoundError:
        pass

    try:
            open(path_to_file)
            existance = True

    except FileNotFoundError:
            existance = False

         
    if existance == False :
        print("There is no file for this metric \n")
    

    elif existance == True :
        with open(path_to_file, "r") as p:
          for row in p:
            row = row.split(' : ')
            x_axis.append(int(row[0]))
            y_axis.append(float(row[1]))
        p.close()

    x = np.linspace(1, len(x_axis), len(x_axis))#This is done because we would get type problems if we were to use x_axis with float() or int() and so on
    a, b, c, d = np.polyfit(x, y_axis, deg=3)#Tried a few and this seems to deliver the best results
    y_est = a * x**3 + b * x**2 + c * x + d#3rd degree polynome
    y_err = (np.array(y_axis)-y_est).std() * np.sqrt(1/len(x) + (x - x.mean())**2 / np.sum((x - x.mean())**2))#This gives the mean error for the fill between

    plt.plot(x, y_est, "-")
    plt.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
    plt.plot(x_axis, y_axis, "o", color="tab:red")

    plt.xlabel('Number of iterations ', fontsize = 12)
    plt.ylabel('Value of ' + metric_name, fontsize = 12)

    plt.axis([1, None, -0.05, 1.05])# y min is 0 and y max is 1 (0 to 100 percent)
    plt.yticks(np.arange(0, 1.05, 0.05))# makes y stepwidth be 5 percent
    plt.xticks(np.arange(1, len(x_axis) + 1, int(1 + len(x_axis)/10)))# makes x stepwidth be 1
    plt.xticks(rotation = 90)
  
    plt.title( class_name + " " + metric_name + ' over time', fontsize = 20)
    plt.savefig(path_to_plot)
    plt.cla()