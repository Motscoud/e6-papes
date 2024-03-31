#importing API
from e621 import E621
import requests
import random

#spawn API
api = E621()

#Get posts with tags!
posts = api.posts.search("16:9 -rating:e -gore -animated -blood -imminent_death -snuff -cruelty -vore -hard_vore")

#Grabs the first post.
post = random.choice(posts)

#And grabs the URL!
image_url = post.file.url

#Grab the image
response = requests.get(image_url)

#saves the image to temp to feed into feh
with open('img.jpg', 'wb') as f:
    f.write(response.content)