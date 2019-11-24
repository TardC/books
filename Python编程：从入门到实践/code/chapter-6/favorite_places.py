favorite_places = {
    'tardc': ['beijing', 'shanghai', 'hangzhou'],
    'xx': ['beijing', 'hangzhou'],
    'lily':['shenzhen']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite place(s) is/are:")
    for place in places:
        print("\t" + place.title())
