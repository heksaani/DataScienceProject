#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a module for the questionnaire in the interactive Jupyternotebook.
"""
from IPython.display import display
import ipywidgets as widgets
from ipywidgets import VBox, HBox, Layout

data = {}

def labeled_widget(label, widget):
    """Function to create a labeled widget."""
    return widgets.VBox([widgets.Label(label), widget], layout=widgets.Layout(margin='0 0 20px 0'))
def parse_value(value, parse_func=int):
    """Function to parse the value from the questionnaire."""
    return parse_func(value.split(":")[0]) if ":" in value else parse_func(value)


def on_button_click(b):
    """Function to get the data from the questionnaire."""
    global data

    for key, widget in widgets_dict.items():
        if key in special_parsing:
            data[key] = special_parsing[key](widget.value)
        else:
            data[key] = widget.value

questions = {
    "Name": {"type": widgets.Text, "options": {}, "label": "Name:"},
    "Age": {"type": widgets.IntText, "options": {"min":0}, "label": "Age:"},
    "Sleeptime (h)": {"type": widgets.FloatText, "options": {"min": 0.0}, "label": "Hours slept on average a night:"},
    "Latency": {"type": widgets.IntText, "options": {"min": 0}, "label": "How long does it take you to fall asleep in minutes?:", "parse_func": parse_value},
    "Restfulness": {"type": widgets.Dropdown, "options": {"options": ["1: Yes, almost always", "2: Yes, often", "3: Rarely, or almost never"]}, "label": "Do you feel rested when you wake up in the morning?:", "parse_func": parse_value},
    "Wakes": {"type": widgets.Dropdown, "options": {"options": ["0", "1", "2", "3", "4", "5 or more"]}, "label": "How many times do you wake up during the night?:", "parse_func": parse_value},
    "Stress": {"type": widgets.Dropdown, "options": {"options": ["1: Not stressed at all", "2", "3", "4", "5", "6", "7: Consumed by stress"]}, "label": "Stress, on a scale from 1 to 7:", "parse_func": parse_value},
    "Steps": {"type": widgets.IntText, "options": {"min": 0}, "label": "Daily steps:"},
    "Food" : {"type": widgets.Dropdown, "options": {"options": ["1: Never" , "2: Yes, sometimes", "3: Often"]}, "label": "When buying/acquiring food, do you take health factors into account?:", "parse_func": parse_value},
    "Exercise scale" : {"type": widgets.Dropdown, "options": {"options":  ['0: Not at all or very seldom',
                                                                           "1: 1-3 times a month",
                                                                           "2: Roughly once a week",
                                                                           "3: 2-3 times a week",
                                                                           "4: 4-6 times a week",
                                                                           "5: Daily"]},
                                                                           "label": "How often do you take more vigorous physical exercise at the minimum for 30 minutes at a time?:", "parse_func": parse_value},
}


special_parsing = {
    "Sleep quality": parse_value,
    "Stress": parse_value,
    "Food": parse_value,
    "Wakes": parse_value,
    "Restfulness": parse_value,
    "Exercise scale": parse_value,
}

widgets_dict = {}
all_widgets = []

for key, question in questions.items():
    widget_type = question["type"]
    widget_options = question["options"]
    widget_label = question["label"]
    widget = widget_type(**widget_options)
    widgets_dict[key] = widget
    lw = labeled_widget(widget_label, widget)
    all_widgets.append(lw)
    spacer = widgets.Label(value='', layout=Layout(height='5px'))
    all_widgets.append(spacer)  # Add spacer to list

button = widgets.Button(description="Submit")
button.on_click(on_button_click)

all_widgets.append(button)
display(VBox(all_widgets)) 

def get_data():
    """Function to get the data from the questionnaire."""
    return data