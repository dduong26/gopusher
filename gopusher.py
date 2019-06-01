#! /usr/bin/env python
import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('http://gotracker.ca/GOTracker/mobile/StationStatus/Service/01/Station/3')

soup = BeautifulSoup(page.text, 'html.parser')
#item = soup.find_all(True, {'class':['colTripDestination', 'colTripScheduled', 'colTripTrack', 'colTripExpected']})
station = [station.get_text() for station in soup.find_all(class_='colTripDestination')]
tripscheduled = [tripscheduled.get_text() for tripscheduled in soup.find_all(class_='colTripScheduled')]
triptrack = [triptrack.get_text() for triptrack in soup.find_all(class_='colTripTrack')]
tripexpected = [tripexpected.get_text() for tripexpected in soup.find_all(class_='colTripExpected')]

gotrain = pd.DataFrame({
    "Station": station,
    "Trip Scheduled": tripscheduled,
    "Trip Track": triptrack,
    "Trip Expected": tripexpected
})

if __name__ == '__main__':
    print(gotrain)
