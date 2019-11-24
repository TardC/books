rivers = {
    'nile': 'egypt',
    'huanghe': 'china',
    'changjiang': 'china',
    }

through_countries = {
    'nile': 'egypt',
    'huanghe': 'china',
    'changjiang': 'china',
    }

for river, country in rivers.items():
    print("The " + river.title() + " runs throuth " + country.title() + ".")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

for river, coutry in through_countries.items():
    print("The " + river.title() + " runs through " + country.title() + ".")

for river in through_countries.keys():
    print(river.title())

for country in through_countries.values():
    print(country.title())
