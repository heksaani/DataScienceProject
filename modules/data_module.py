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

data = pd.read_csv("./data/data_combined_final.csv")