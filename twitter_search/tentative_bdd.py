import pymysql
import tweepy
import time
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

con = pymysql.connect(host='localhost', user='root', port=3306, password='', database='db')

WORDS = ['fortnite', 'Trump', 'the']

def store_data(created_at, text, screen_name, tweet_id):
    cursor = con.cursor()
    insert_query = "INSERT INTO twitter (tweet_id, screen_name, created_at, text) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (tweet_id, screen_name, created_at, text))
    db.commit()
    cursor.close()
    db.close()
    return


class listener(tweepy.StreamListener):

    def on_data(self,data):

            datajson = json.loads(data)
            
            text = datajson['text']
            screen_name = datajson['user']['screen_name']
            tweet_id = datajson['id']
            created_at = parser.parse(datajson['created_at']) 
 
            print("Tweet collected at " + str(created_at))
            
            store_data(created_at, text, screen_name, tweet_id)
        


    def on_error(self, status):
        print(status)

auth = tweepy.OAuthHandler("NLZ39ilLBflHHt8myenHdH3Ao", "FJ5EAa7DMtnrUHPFNXMuG0heucpzZPatYJNjoixFniWMK8WM0o")

auth.set_access_token("1117700066255474688-5BSckADfdnZTX1WAgTBQib1tnEXBMO", "eiTGX94V9NRpXr9cI5j29oR59MzVp1NeVhHNKCrl4xEWl")

listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True)) 
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS)

