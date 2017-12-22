import tweepy
import requests
import os

from PIL import Image
from PIL import ImageFile
from io import BytesIO

from credentials import *

# Oauth handler and API key verification
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweet_image(url, username, status_id):
	# hard coded pwd
	# input_path = '/Users/nwalsh/Dev/style-twitter-bot/'
	input_path = '/home/datmo-team/projects/style-twitter-bot/'
	input_filename = os.path.join(input_path, 'input_image.png')
	#send get request
	request = requests.get(url, stream=True)
	if request.status_code == 200:
		#read data from downloaded bytes
		i = Image.open(BytesIO(request.content))
		#save the input image under a particular filename
		i.save(input_filename)
		#hardcoded output directory
		#output_path = '/Users/nwalsh/Dev/style-twitter-bot/output_images/'
		output_path = '/home/datmo-team/projects/style-twitter-bot/output_images/'
		output_filename = os.path.join(output_path, 'starry_night.jpg')
		api.update_with_media(output_filename, status='@{0} Here\'s your painting!'.format(username), in_reply_to_status_id=status_id)

	else:
		print("Oh no, unable to download image!")


# BotStreamer class, inherit from Tweepy's StreamListener
class BotStreamer(tweepy.StreamListener):
	# Called when a new status arrives
	def on_status(self, status):
		username = status.user.screen_name
		status_id = status.id

		if 'media' in status.entities:
			for image in status.entities['media']:
				tweet_image(image['media_url'], username, status_id)

myStreamListener = BotStreamer()

stream = tweepy.Stream(auth, myStreamListener)
stream.filter(track=['@StarryNightBot'])

