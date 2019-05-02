import tweepy

auth = tweepy.OAuthHandler("NLZ39ilLBflHHt8myenHdH3Ao", "FJ5EAa7DMtnrUHPFNXMuG0heucpzZPatYJNjoixFniWMK8WM0o")

auth.set_access_token("1117700066255474688-5BSckADfdnZTX1WAgTBQib1tnEXBMO", "eiTGX94V9NRpXr9cI5j29oR59MzVp1NeVhHNKCrl4xEWl")

api = tweepy.API(auth, wait_on_rate_limit = True)


search_word = input("entrer le mot que vous chercher : ")

date_since = "2019-04-01"


tweets = tweepy.Cursor(api.search, q = search_word, lang = "en", since = date_since).items(5)

user_location = [[tweet.text] for tweet in tweets]


for tweet in tweets:
    print(user_location)
