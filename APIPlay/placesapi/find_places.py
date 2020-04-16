import requests
import json


def find_closest():
    """
    Find closest store using latitude and longitude
    """

    payload = {'location': '49.282441,-123.118667',
               'rankby': 'distance',
               'type': 'grocery_or_supermarket',
               'key': 'AIzaSyC3seDxrJph4nMK3IPMSTvmvhdryXKFpUc'}

    responses = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?', params=payload)
    responses.raise_for_status()
    data = json.loads(responses.text)
    result_list = data['results']

    for place in result_list:
        if 'opening_hours' in place:
            print('Name:', place['name'],
                  'Coordinates', place['geometry']['location']['lat'], place['geometry']['location']['lng'],
                  'Open now:', place['opening_hours']['open_now'],
                  'Address:', place['vicinity'],
                  'Place id:', place['place_id'])
        else:
            print(place['name'], 'has no operating hours info.')

    return result_list


def main():
    print('Loaded: find_places.py')
    find_closest()


if __name__ == "__main__":
    main()
