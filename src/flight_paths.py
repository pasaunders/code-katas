"""Given two cities, return a path and the total distance traveled."""

import math
import json
import networkx as nx


def calculate_distance(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.
    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from: http://www.movable-type.co.uk/scripts/latlong.html
    """

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3  # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])
    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934 # convert km to miles


def read_airports():
    """Parse json file containing airport data into useable format."""
    with open('../cities_with_airports.json', 'r') as data:
        airport_file = json.load(data)
        airport_dictionary = {}
        for city in airport_file:
            airport_dictionary[city['city']] = {
            'lat_lon': city['lat_lon'],
            'connections': city['destination_cities']
            }
        return airport_dictionary


def flight_path(start_city, end_city):
    """Generate a flight path using a graph."""
    airport_dictionary = read_airports()
    airport_graph = nx.Graph()
    for city, data in airport_dictionary.items():
        airport_graph.add_node(city)
        for item in data['connections']:
            try:
                travel_dist = calculate_distance(data['lat_lon'], airport_dictionary[item]['lat_lon'])
            except KeyError:
                continue
            airport_graph.add_edge(city, item, weight=travel_dist)
    path = str(nx.dijkstra_path(airport_graph, start_city, end_city))
    length = nx.dijkstra_path_length(airport_graph, start_city, end_city)
    return "The path is: {}, covering {} miles".format(path, length)
