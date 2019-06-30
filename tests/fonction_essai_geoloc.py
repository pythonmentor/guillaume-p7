
import googlemaps
from pprint import pprint
gmaps = googlemaps.Client(key=name)
geocode_result = gmaps.geocode('tour eiffel')
pprint(geocode_result)
