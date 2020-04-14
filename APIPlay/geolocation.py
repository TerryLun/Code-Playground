# from APIPlay.geolocation import geolocation
import requests

assert requests.get('https://github.com/nvbn/import_from_github_com').status_code == 200


# lat, lon = geolocation.getLocation()
# print(lat, lon)
