#DEPENDENCIAS
#pip install tweepy

from multiprocessing.connection import Client
from textwrap import indent
# import config
import tweepy 
# import random
import json



#Cadenas para la autentificación
ACCESS_TOKEN = '972601443130757120-YDpvwikNyQmExICTBEZ0e7UnaXJWQc3'
ACCESS_TOKEN_SECRET = 'vCVPrNEk4PxqfJhqhIypDxJyq75oc2sSem1GDxE6xjAg8'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAN%2BiZAEAAAAA%'
API_KEY = 'pCkN7QGEPtR2GNukq2s9UTmiE'
API_KEY_SECRET = 'Vj9fFrf2d5rGBwAHCWU6x4SxYQo1Tpglf861cHRGKuqYh4fNok'


def obtenerCliente():
    client = tweepy.Client(bearer_token=BEARER_TOKEN,
                            consumer_key=API_KEY,
                            consumer_secret= API_KEY_SECRET,
                            access_token=ACCESS_TOKEN,
                            access_token_secret=ACCESS_TOKEN_SECRET)
    return client


auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# for user in tweepy.Cursor(api.get_friends, screen_name="Tnch").items():
#     print('friend: ' + user.screen_name)

for user in tweepy.Cursor(api.get_followers, screen_name="ChrisPaz2001").items():
    print('follower: ' + user.screen_name)


# client = obtenerCliente()

# data = client.get_followed_lists('ChrisPaz2001',user_auth=False)
# print(data)

# data = api.m
# data = api.get_user()
# print(json.dumps(data._jason, indent = 2))
