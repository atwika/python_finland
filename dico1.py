def mort():
    print("tu dois mourir")

def vie():
    print("tu dois vivre")


choix = {}

choix["mort"] = mort
choix["vie"] = vie

choix["vie"]()

#///////////


fruits = {"pommes" : 21, "oranges" : 15, "poires" : 12}

for cle, val in fruits.items():
    print("vous disposez de {} {}.".format(val, cle))


