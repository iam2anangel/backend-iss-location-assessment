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
   
    coordinates = {'lat': 39.7684, 'lon': -86.1581}
    request = requests.get("http://api.open-notify.org/iss-pass.json", params=coordinates)
    #time stamp
    value = request.json()
    print value['response'][0]['risetime']
    pass_time = time.ctime(value['response'][0]['risetime'])
    return pass_time

def get_map():
    data = get_coordinates()
    pos = data['iss_position']
    longitude = pos['longitude']
    latitude = pos['latitude']
    screen = turtle.Screen()
    screen.bgpic('map.gif')
    screen.setup(width=720, height=360, startx=None, starty=None) #sets up size of the screen
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.register_shape('iss.gif')

    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.setheading(90)
    iss.penup()
    iss.goto(float(longitude), float(latitude))

    indy = turtle.Turtle()
    indy.penup()
    indy.color('yellow')
    indy.goto(-86.1581, 39.7684,)
    indy.dot(5)
    indy.write(indy_time())
    screen.exitonclick()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--astro', help='finds astronauts', action='store_true')
    parser.add_argument('-c', '--coords', help='finds coordinates', action='store_true')
    parser.add_argument('-m', '--map', help='displays map', action='store_true')
    return parser


def main(args):
    parser = create_parser()
    parsed_args = parser.parse_args(args)

    if parsed_args.astro:
        astronauts = get_astronauts()
        for astronaut in astronauts['people']:
            print("Astronaut {} is aboard the {}".format(astronaut['name'], astronaut['craft']))
            print("Number of astronauts in space: {}".format(astronauts['number']))
    
    elif parsed_args.coords:
        coordinates = get_coordinates()
        print("The ISS is located at latitude {} and longitude {} on {}"
              .format(coordinates['iss_position']['latitude'],
                      coordinates['iss_position']['longitude'],
                      time.ctime(coordinates['timestamp'])))
    
    elif parsed_args.map:
        date = indy_time()
        get_map()
        print("The ISS will pass over Indianapolis, IN on {}".format(date))

    


if __name__ == '__main__':
    
    main(sys.argv[1:])
