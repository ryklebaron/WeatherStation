import requests
from bs4 import BeautifulSoup
import csv
import json

BUIEN_RADAR_URL = 'https://data.buienradar.nl/2.0/feed/json'
response = requests.get(BUIEN_RADAR_URL)
soup = BeautifulSoup(response.text, 'lxml')

def parse_json(response):
    if response.status_code >= 400:
        raise ValueError('request failed', response.status_code, response)
    return response.json()


def retrieve_buienradar():
    return parse_json(requests.get(BUIEN_RADAR_URL))

measurements = retrieve_buienradar()['actual']['stationmeasurements']
for m in measurements:
    print(f"{m['stationname']:<40},{m['regio']}")

# print(retrieve_buienradar())