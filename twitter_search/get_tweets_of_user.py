import tweepy

auth = tweepy.OAuthHandler("NLZ39ilLBflHHt8myenHdH3Ao", "FJ5EAa7DMtnrUHPFNXMuG0heucpzZPatYJNjoixFniWMK8WM0o")

auth.set_access_token("1117700066255474688-5BSckADfdnZTX1WAgTBQib1tnEXBMO", "eiTGX94V9NRpXr9cI5j29oR59MzVp1NeVhHNKCrl4xEWl")



def get_tweets(username):

    api = tweepy.API(auth)

    number_of_tweets = 200
    tweets = api.user_timeline(screen_name=username)

    tmp = []

    tweets_for_csv = [tweet.text.encode("utf-8") for tweet in tweets]

    for j in tweets_for_csv:

        tmp.append(j)
        print("\n")
    print(tmp)




