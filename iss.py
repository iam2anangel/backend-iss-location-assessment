#!/usr/bin/env python

__author__ = 'iam2angel' #Jen Browning

import requests
import turtle
import time
import argparse
import sys

def get_astronauts():
    """Returns the full names, number, and spacecraft of astronauts in ISS."""
    astro_data = requests.get("http://api.open-notify.org/astros.json")
    return astro_data.json()
   
   
def get_coordinates():
    coordinate_data = requests.get("http://api.open-notify.org/iss-now.json")
    return coordinate_data.json()

def indy_time():
    coordinates = {'lat: 39.7684', 'lon: -861581'}
    request = requests.get("http://api.open-notify.org/iss-pass.json", params=coordinates)
    #time stamp
    pass_time = time.ctime(request.json(['response'][0]['risetime']))
    return pass_time

def get_map()
    data = get_coordinates()
    pos = data['iss_position']
    longitude = data['longitude']
    latitude = data['latitude']
    screen = turtle.Screen()
    screen.bgpic('map.gif')
    screen.setup(width=720, height=360, startx=None, starty=None)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.register_shape('iss.gif')

    iss = turtle.Turtle()
    iss.setheading(90)
    iss.penup()
    iss.goto(float(longitude), float(latitude))

    indy = turtle.Turtle()
    indy.penup()
    indy.color('green')
    indy.goto(39.7684, -86.1581)
    indy.dot(5)
    indy.write(indy_time)
    screen.exitonclick()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--astro', help='finds astronauts', action='store_true')
    parser.add_argument('-c', '--coords', help='finds coordinates', action='store_true')
    parser.add_argument('-m', '--map', help='displays map', action='store_true')
    return parser


def main():
    


if __name__ == '__main__':
    main()
