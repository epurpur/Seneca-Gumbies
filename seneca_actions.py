#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 11:37:43 2018

@author: ep9k
"""

import seneca_gumbies_main    #main module
import csv
import time
import random


routes_climbed = []
pitches_climbed = 0
energy_level = 100


def choose_route():
    """After deciding about the weather, you come here and choose a route to climb.
    Reads list of routes from .csv file with names, grades, and pitches."""
    global routes_climbed, pitches_climbed
    
    route_info = {}

    with open('seneca_routes.csv', 'r', encoding='utf-8-sig') as f:     #weird encoding from excel?
        reader = csv.DictReader(f, ('route_name', 'route_grade', 'pitches'))
        print("Choose a route to climb from the following list of classics.")
        print()
        
        for row in reader:
            print(row['route_name'],row['route_grade'])
            route_info[row['route_name']] = row['pitches']

    route_choice = input("Which route do you want to climb? : ")

    if route_choice in route_info.keys():
        routes_climbed.append(route_choice)
        pitches_climbed += int(route_info[route_choice])
        climb_route(route_choice)
    else:
        print("Incorrect route name")
        time.sleep(3)
        choose_route()
    
 
def climb_route(route_choice):
    """After choosing a route, you will climb a route.
    Random module chooses a random # of pieces per route and chooses a random piece for each placement.
    Random pieces are a mix of gear selection and color."""
    global energy_level
    gear_selection = ['cam', 'nut', 'hex', 'tcu']
    gear_color = ['red', 'yellow', 'blue', 'gray', 'purple', 'green', 'red', 'gold']
    gear_placements = random.randint(5,10)
    
    if energy_level < 50:
        eat_food(route_choice)
    
    start_route = input("Are you ready to climb?  Type 'y' when ready : ")
    
    if start_route == 'y':
        print(f"There are {gear_placements} gear placements available on {route_choice}.  Choose wisely or else you'll be running it out.")
        print("A few of the pieces you used were")
        while gear_placements > 0:
            print(random.choice(gear_color), random.choice(gear_selection))
            gear_placements -= 2
        energy_level -= 30
    else:
        dead("You weren't ready to climb.")
    
    another_route = input("Do you want to climb another route? y/n ")
    if another_route == 'y':
        choose_route()
    else:
        dead()
     
        
def eat_food(route_choice):
    """when energy levels get low, eat some food to bring them back up"""
    global energy_level
    food_choices = {'apple': 30, 'trail mix': 40, 'clif bar': 45, 'water': 10, 'red bull': 500}

    print(f"Your power bars are getting low. Eat a snack before continuing. Current energy level at {energy_level}. Below you'll see a snack and the energy you get from it. ")
    time.sleep(2)
    for food, food_energy in food_choices.items():
        print(f'{food} - {food_energy}')
    user_food_choice = input("What'll you have? : ")
    if user_food_choice in food_choices.keys():
        energy_level += food_choices[user_food_choice]
    print("Energy level", energy_level)
    climb_route(route_choice)
    


def dead(x="Your day is over."): #needs argument in dead(x).  Why? I think because dead() is called when finishing outcomes to end program. And this tells you why the outcome is so ex: "Too cold"
    """end of the program. Bounces back to main module"""
    print(x)
    seneca_gumbies_main.finish()
    


