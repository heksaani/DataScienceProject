#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a module for the data in the interactive Jupyternotebook.
"""
import matplotlib.pyplot as plt
import ipywidgets as widgets
import pandas as pd
import numpy as np
import seaborn as sns
import pickle
import questionnaire_module as qm

data = pd.read_csv("./data/data_combined_final.csv")


def get_data():
    """Function to get the data."""
    return data

def get_user_feedback(user_value, data, variable):
    """This functions return the user feedback when comparing the user input data to the data in the dataset"""
    if user_value < data[variable].mean():
        feedback = f"You have a lower value than the average person. \n The difference is {round(data[variable].mean() - user_value, 2)}."
    elif user_value == data[variable].mean():
        feedback = f"You have the same value as the average person."
    else:
        feedback = f"You have a higher value than the average person. \n The difference is {round(user_value - data[variable].mean(), 2)}."
    return feedback

def plot(dataset, userdata, plotted_variables):
    """Function to plot a scatterplot of the data  with the input of the user
    if the input plotted_variables is length is one the x-axis does not have any value 
    and the y-axis is the value of the variable in plotted_variables"""

    if len(plotted_variables) == 1:
        variable = plotted_variables[0]
        y_data = dataset[variable]
        x_data = [0.5]*len(y_data)
        y_user = userdata[variable]
        x_user = 0.5
    
    else:
        x_data = dataset[plotted_variables[0]]
        y_data = dataset[plotted_variables[1]]
        x_user = userdata[plotted_variables[0]]
        y_user = userdata[plotted_variables[1]]
    

    # if the plotted is just one variable the x-axis does not have any value name and any values
    if len(plotted_variables) == 1:
        plt.figure(figsize=(10, 6))
        plt.xlabel(' ')
        plt.xticks([])
        plt.ylabel(plotted_variables[0])

        plt.scatter(x_data, y_data, color='pink', marker='o', s=100, alpha=0.5, label='Data')
        plt.scatter([x_user], [y_user], color='purple', marker='o', s=100, label=userdata['Name'])
        plt.axhline(y=y_data.mean(), color='black', linestyle='--', label=f"Average {plotted_variables[0]}")
        y_min, y_max = plt.ylim()
        x_min, x_max = plt.xlim()
        feedback = get_user_feedback(userdata[plotted_variables[0]], dataset, plotted_variables[0])
        plt.text(x_min + 0.56*(x_max-x_min), y_min + 0.4*(y_max-y_min), feedback, fontsize = 10)
        plt.legend()
    # if the plotted is two variables the x-axis and y-axis have values and value names
    else:
        plt.figure(figsize=(10, 6))

        plt.xlabel(plotted_variables[0])
        plt.ylabel(plotted_variables[1])

        plt.scatter(x_data, y_data, color='pink', marker='o', s=100, alpha=0.5, label='Data')
        plt.scatter([x_user], [y_user], color='purple', marker='o', s=100, label=userdata['Name'])
        plt.axhline(y=y_data.mean(), color='black', linestyle='--', label= f"Average {plotted_variables[1]} " )
        #plt.axvline(x=x_data.mean(), color='black', linestyle='--', label= f"Average {plotted_variables[0]}")
        y_min, y_max = plt.ylim()
        x_min, x_max = plt.xlim()
        feedback_x = get_user_feedback(userdata[plotted_variables[0]], dataset, plotted_variables[0])
        feedback_y = get_user_feedback(userdata[plotted_variables[1]], dataset, plotted_variables[1])
        #plt.text(x_min + 0.56*(x_max-x_min), y_min + 0.4*(y_max-y_min), feedback_x, fontsize = 10)
        plt.text(x_min + 0.56*(x_max-x_min), y_min + 0.3*(y_max-y_min), feedback_y, fontsize = 10)
        plt.legend()

