import sys 
import json 
from tweepy import Cursor 
from twitter_client import get_twitter_client 
 
user = input('Enter the user name: ') 

client = get_twitter_client() 
 
fname = "user_timeline_{}.jsonl".format(user) 
 
with open(fname, 'w') as f: 
    for page in Cursor(client.user_timeline, screen_name=user, count=200).pages(16): 
        for status in page:
        	f.write(json.dumps(status._json)+"\n") 