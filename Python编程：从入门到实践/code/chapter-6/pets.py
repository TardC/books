dabai = {
    'species': 'cat',
    'host': 'himself',
    }

dahua = {
    'species': 'cat',
    'host': 'herself',
    }

xiaobai = {
    'species': 'cat',
    'host': 'himself',
    }

pets = [dabai, dahua, xiaobai]

for pet in pets:
    species = pet['species']
    host = pet['host']
    print(host.title() + " have a/an " + species + ".")
