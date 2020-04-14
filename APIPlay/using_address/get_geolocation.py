import requests
import json


def get_coordinates():
    """
    Query user input address then return latitude and longitude
    """
    address = input('Where ya at boi? ')
    key = 'AIzaSyARtxtrUYeHG4cfM7O5TRpDy62FG7lkszg'
    responses = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={key}')
    responses.raise_for_status()
    data = json.loads(responses.text)
    return data['results'][0]['geometry']['location']['lat'], data['results'][0]['geometry']['location']['lng']


def main():
    print('Loaded: geo_location.py')


if __name__ == "__main__":
    main()
