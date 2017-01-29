#yelp_api.py in flask
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#def get_yelp(term, location):
def get_businesses(address, term):
	auth = Oauth1Authenticator(
    	consumer_key=os.environ['CONSUMER_KEY'],
    	consumer_secret=os.environ['CONSUMER_SECRET'],
    	token=os.environ['TOKEN'],   	
    	token_secret=os.environ['TOKEN_SECRET']
	)

	client = Client(auth)

	params = {
    'term': 'food',
    'lang': 'en',
    'limit': 3
	}

	response = client.search(address, **params)

	businesses = []

	for business in response.businesses:
		businesses.append({"name": business.name, "rating": business.rating, "phone": business.phone})
	return businesses

# businesses = get_businesses('New York City', 'food')
# print(businesses)
# get_businesses('New York City', 'food')	

