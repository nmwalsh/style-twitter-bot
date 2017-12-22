import tweepy
import requests
from PIL import Image
from PIL import ImageFile

from credentials import *

# Oauth handler and API key verification
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweet_image(url, username, status_id):
	filename = 'input_image.png'
	#send get request
	request = requests.get(url, stream=True)
	if request.status_code == 200:
		#read data from downloaded bytes
		i = Image.open(BytesIO(request.content))
		#save the image under a particular filename
		i.save(filename)
		#scramble(filename)
		api.update_with_media('starry_night.png', status='@{0}, here\'s your painting!'.format(username), in_reply_to_status_id=status_id)

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

