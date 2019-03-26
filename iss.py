#!/usr/bin/env python

__author__ = 'iam2angel' #Jen Browning

import requests
import turtle
import time

def get_astronauts():
    """Returns a list of people in space"""
    url = "http://api.open-notify.org/astros.json"
    request = request.get(url)
    req_data = request.json()
    print("Number of astronauts in space: {}.format(req_data[number])")


def get_coordinates():
    """Returns the current latitude and longitude with a time stamp"""
    #also need a time stamp for this function
    url = "http://api.open-notify.org/iss-now.json"
    res = requests.get(url)
    req_data = requests.json()
    longitude = req_data["iss_position"]["longitude"]
    latitude = req_data["iss_position"]["latitude"]
    timestamp = time.ctime(req_data["timestamp"])
    print("Longitude: {}.format(longitude)")
    print("Latitude: {}.format(latitude)")
    print("Timestamp: {}.format(timstamp)")
    return longitude, latitude, timestamp

def create_screen():
    screen = turtle.Screen()
    screen.setup(width=720, height=360, startx=None, starty=None)
    screen.bgpic('map.gif')
    screen.setworldcoordinates(-180, -90, 180, 90)
    return screen

def iss_map(screen, latitude, longitude):
    iss = turtle.Turle()
    screen.register_shape('iss.gif')
    iss.setheading(90)
    iss.penup()
    iss.goto(float(longitude), float(latitude))

def indy_pass(longitude, latitude):
    url = "http://api.open-notify.org/iss-pass.json"
    coord = {'lat: 39.7684', 'lon': -86.1581}
    res = requests.get(url, params=coord)
    pass_time = time.ctime(res.json()['response'[0]['risetime']])
    return pass_time

def iss_dot(longitude, latitude, timestamp):
    indy = turtle.Turtle()
    indy.penup()
    indy.color('green')
    indy.goto(longitude,latitude)
    indy.dot(5)
    indy.hideturtle()
    indy.write(indy_pass(longitude, latitude))

def indy_coordinates():
    indy_latitude = 39.7684
    indy_longitude = -86.1581
    indy_time = indy_pass(indy_latitude, indy_longitude)
    iss_dot(indy_longitude, indy_latitude, indy_time)




def main():
    print(get_astronauts)
    print(get_coordinates)


if __name__ == '__main__':
    main()
