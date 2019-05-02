import tweepy

auth = tweepy.OAuthHandler("NLZ39ilLBflHHt8myenHdH3Ao", "FJ5EAa7DMtnrUHPFNXMuG0heucpzZPatYJNjoixFniWMK8WM0o")

auth.set_access_token("1117700066255474688-5BSckADfdnZTX1WAgTBQib1tnEXBMO", "eiTGX94V9NRpXr9cI5j29oR59MzVp1NeVhHNKCrl4xEWl")

api = tweepy.API(auth, wait_on_rate_limit = True)

api.update_status("encore toi sumo ? @AlihsanAln " + str(i))
