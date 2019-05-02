import tweepy

auth = tweepy.OAuthHandler("NLZ39ilLBflHHt8myenHdH3Ao", "FJ5EAa7DMtnrUHPFNXMuG0heucpzZPatYJNjoixFniWMK8WM0o")

auth.set_access_token("1117700066255474688-5BSckADfdnZTX1WAgTBQib1tnEXBMO", "eiTGX94V9NRpXr9cI5j29oR59MzVp1NeVhHNKCrl4xEWl")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
user = api.get_user('twitter')

for tweet in public_tweets:
    print("Contenu du tweet : " + tweet.text + "\n")

for status in tweepy.Cursor(api.user_timeline).items():
    # process status here
    process_status(status)
