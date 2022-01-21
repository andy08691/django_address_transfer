from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from time import sleep
from random import randint

def geoProcessing(address):
  print('geoProcessing', address)
  try:
    user_agent = 'user_me_{}'.format(randint(10000,99999))
    geolocator = Nominatim(user_agent=user_agent)
    location = geolocator.geocode(address)
    print('location', location)
    print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
    return {'latitude':  location.latitude, "longitude": location.longitude}
  except Exception as e:
    return None
    
    
  
  # try:
  #   return geolocator.reverse(latlon)
  # except GeocoderTimedOut:
  #     logging.info('TIMED OUT: GeocoderTimedOut: Retrying...')
  #     sleep(randint(1*100,sleep_sec*100)/100)
  #     return reverse_geocode(geolocator, latlon, sleep_sec)
  # except GeocoderServiceError as e:
  #     logging.info('CONNECTION REFUSED: GeocoderServiceError encountered.')
  #     logging.error(e)
  #     return None
  # except Exception as e:
  #     logging.info('ERROR: Terminating due to exception {}'.format(e))
  #     return None
  