#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 08:07:51 2018

@author: ep9k
"""
import seneca_actions as sa
import time

def current_season():
    seasons = 'winter spring summer fall'.split()
    print("Seasons are: ")
    for season in seasons:
        print(season)
    current_season = input('What season is it now? ')
    seasonDict[current_season]()     #I put season functions into a dictionary (seasonDict). this takes current_season and grabs that function from the dictionary, then executes
    
    
def winter_season():
    winter_temps = input("Good days are hard to come by in the Winter. Is it warmer than 40 degrees? y/n : ")
    if winter_temps == 'y':
        sunny_day = input("It is warm enough if there is sun. Is there sun? y/n : ")
        if sunny_day == "yes":
            time.sleep(2)
            sa.choose_route()   #jumps to choose_route.
        else:
            sa.dead("Too cold")
    else:
        sa.dead("Too cold") #jumps to dead(x). x is message printed in dead()


def summer_season():
    cool_day = input("Summer can be hot at Seneca. Is it cooler than 85 degrees? y/n : ")
    if cool_day == 'y':
        time.sleep(2)
        sa.choose_route()
    else:
        sa.dead("Too hot, go swim in the river instead")
       

def spring_season():
    rainy_day = input("Spring can be rainy at Seneca. Is it raining today? y/n :")
    if rainy_day == 'y':
        sa.dead("Too wet to climb today.")
    else:
        time.sleep(2)
        sa.choose_route()
     
        
def fall_season():
    print("Ahh, perfect fall weather today. You lucky dog!")
    time.sleep(2)
    sa.choose_route()


seasonDict = {
#I put season functions into a dictionary (seasonDict).
        "winter": winter_season,
        "summer": summer_season,
        "spring": spring_season,
        "fall": fall_season        
        }

