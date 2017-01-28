import forecastio 
from geopy.geocoders import Nominatim


def get_weather(address):
	api_key = "b99b91ca4bc9dba39449b7783fc83cf5"
	geolocator = Nominatim()
	location = geolocator.geocode(address)

	forecast = forecastio.load_forecast(api_key, location.latitude, location.longitude).currently()
	return("{} and {} degrees".format(forecast.summary, forecast.temperature))


