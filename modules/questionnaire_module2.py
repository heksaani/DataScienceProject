#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a module for the questionnaire in the interactive Jupyternotebook.
"""

from IPython.display import display
import ipywidgets as widgets

name_value = ""
age_value = 0
hours_slept_value = 0.0
sleep_quality_value = ""
stress_value = ""
exercise_value = ""
daily_steps_value = 0
alcohol_consumption_value = 0.0
food_value = ""
socialize_minutes_value = 0
latency = 0
wakes = ""
restfulness = ""
wakes_scale = ""
exercise_scale = ""
alcohol_scale = ""

def labeled_widget(label, widget):
    return widgets.VBox([widgets.Label(label), widget], layout=widgets.Layout(align_items='stretch'))

name = widgets.Text(
    value='',
    placeholder='Type something',
    disabled=False)


age = widgets.IntText(
    value=0, 
    placeholder='Type something',
    disabled=False,
    min=0)

hours_slept = widgets.FloatText(
    value=0.0,
    placeholder='Type something',
    disabled=False,
    min=0.0,)

sleep_quality = widgets.Dropdown(
    options=["1: Yes, almost always", "2: Yes, often", "3: Rarely, or almost never"],
    value="1: Yes, almost always",
    disabled=False)

stress = widgets.Dropdown(
    options=["1: Not stressed at all", "2", "3", "4", "5", "6", "7: Cosumed by stres"],
    value = "1: Not stressed at all",
    disabled=False)

exercise = widgets.Dropdown(
    options=["Yes", "No"],
    value="Yes",
    disabled=False)

daily_steps = widgets.IntText(
    value=0, 
    placeholder=0,
    disabled=False,
    min=0)

food = widgets.Dropdown(
    options=["1: Never" , "2: Yes, sometimes", "3: Often"],
    value="1: Never",
    disabled=False)


latency = widgets.IntText(
    value=0,
    placeholder=0,
    disabled=False,
    min=0)

wakes = widgets.Dropdown(
    options = ["0", "1", "2", "3", "4", "5 or more"],
    value = "0",
    disabled=False)

restfulness = widgets.Dropdown(
    options = ["1: Yes, nearly always", "2: Yes, often", "3: Seldom or hardly ever", "4: Can't say"],
    value = "1: Yes, nearly always",
    disabled=False)

wakes_scale = widgets.Dropdown(
    options = ["0: No", "1:Occationally", "2: Weekly", "3: Daily or almost daily"],
    value = "0: No",
    disabled=False)

exercise_scale = widgets.Dropdown(
    options =  ['0: Not at all or very seldom', "1: 1-3 times a month", "2: Roughly once a week",
                "3: 2-3 times a week", "4: 4-6 times a week", "5: Daily"],
    value = "0: Not at all or very seldom",
    disabled=False)

alcohol_scale = widgets.Dropdown(
    options = ["0: Never", "1: Monthly or less often", "2: 2-3 times a month","3: Once a week", "4: 2-3 times a week", "5: Four times a week or more often"],
    value = "0: Never",
    disabled=False)




button = widgets.Button(description="Submit")

# Define a function to handle button click event
def on_button_click(b):
    global name_value, age_value, hours_slept_value, sleep_quality_value, \
    stress_value, exercise_value, daily_steps_value, alcohol_consumption_value, \
    food_value, socialize_minutes_value, leave_house_value, number_of_people_contact, \
    latency, wakes, student, restfulness, wakes_scale, nervousness, depression, \
    insomnia, exercise_scale, alcohol_scale

    name_value = name.value
    age_value = age.value
    hours_slept_value = hours_slept.value
    sleep_quality_value = int(sleep_quality.value.split(":")[0])
    if stress.value == "1: Not stressed at all" or stress.value == "7: Cosumed by stres":
        stress_value = int(stress.value.split(":")[0])
    else:
        stress_value = int(stress.value)
    exercise_value = 1 if exercise.value == "Yes" else 0
    daily_steps_value = daily_steps.value
    alcohol_consumption_value = int(alcohol_consumption.value)
    food_value = int(food.value.split(":")[0])
    socialize_minutes_value = socialize_minutes.value
    leave_house_value = int(leave_house.value.split(":")[0])
    number_of_people_contact = number_of_people_contact.value
    latency = latency.value
    if wakes.value == "5 or more":
        wakes = 5
    else:
        wakes = int(wakes.value)
    restfulness = int(restfulness.value.split(":")[0])
    wakes_scale = int(wakes_scale.value.split(":")[0])
    nervousness = int(nervousness.value.split(":")[0])
    depression = int(depression.value.split(":")[0])
    anxiety = int(anxiety.value.split(":")[0])
    insomnia = int(insomnia.value.split(":")[0])
    exercise_scale = int(exercise_scale.value.split(":")[0])
    alcohol_scale = int(alcohol_scale.value.split(":")[0])


# Set the function to be called on button click
button.on_click(on_button_click)

# Create labeled widgets
name_labeled = labeled_widget('Name:', name)
age_labeled = labeled_widget('Age:', age)
hours_slept_labeled = labeled_widget('Hours slept on average:', hours_slept)
sleep_quality_labeled = labeled_widget('Do you feel you sleep enough?:', sleep_quality)
stress_labeled = labeled_widget('Stress, on a scale from 1 to 7:', stress)  
daily_steps_labeled = labeled_widget('Daily steps:', daily_steps)  
food_labeled = labeled_widget('When buying/acquiring food, do you take health factors into account?:', food)
latency_labeled = labeled_widget('How long does it take you to fall asleep in minutes?:', latency)
wakes_labeled = labeled_widget('How many times do you wake up during the night?:', wakes)
restfulness_labeled = labeled_widget('Do you feel rested when you wake up?:', restfulness)
insomnia_labeled = labeled_widget('Have you recently lost sleep over worry?:', insomnia)
exercise_scale_labeled = labeled_widget('How often do you take more vigorous physical exercise at \n \
                                        the minimum for 30 minutes at a time and becoming at least a bit \
                                        out of breath and sweaty (e.g. jogging/fast walking, cycling, swimming, gymnastics, ball games)? :',
                                        exercise_scale)
