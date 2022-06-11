from pdb import line_prefix
from mapping import *
import os

def log_in_file(class_label, metric_name, metric_number):

    class_name = mapping[class_label]
    file_name = class_name + "_" + metric_name + ".txt"
    path_to_file: str = "Plots/" + metric_name + "_Plots/Textfiles/" + file_name

    try:
        os.makedirs("Plots/" + metric_name + "_Plots/Textfiles")
        os.makedirs("Plots/" + metric_name + "_Plots/Graphs")
    except FileExistsError as e:
        pass

    try:
        open(path_to_file)
        existance = True
    except FileNotFoundError:
        existance = False
            
    if existance == False :
        with open(path_to_file, "w") as p:
            line = "1 : " + str(metric_number)
            p.write(line)
    
    elif existance == True :
        with open(path_to_file, "r+") as p:
            last_line = p.readlines()[-1]
            i = 1 + int(last_line.split(" : ")[0])
            line = "\n" + str(i) + " : " + str(metric_number)
            p.write(line)
        p.close()