import requests
import json


def get_travel_time():
    """
    Return distance and travel time of two location
    """
    origins = '49.282441,-123.118667'
    destinations = '3700 Number 3 Rd, Richmond, BC V6X 3X2, Canada'
    mode = 'driving'
    key = 'AIzaSyARtxtrUYeHG4cfM7O5TRpDy62FG7lkszg'
    responses = requests.get(f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={origins}&destinations={destinations}&mode={mode}&language=en-CA&key={key}')
    responses.raise_for_status()
    data = json.loads(responses.text)
    distance = data['rows'][0]['elements'][0]['distance']['text']
    travel_duration = data['rows'][0]['elements'][0]['duration']['text']
    return distance, travel_duration


def main():
    print('Loaded: travel_time.py')


if __name__ == "__main__":
    main()
