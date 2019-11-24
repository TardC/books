cities = {
    'beijing': {
        'country': 'china',
        'population': 100,
        'fact': 'politics, economy, culture center',
        },

    'shanghai': {
        'country': 'china',
        'population': 90,
        'fact': 'economy, culture center'
        },

    'hangzhou': {
        'country': 'china',
        'population': 80,
        'fact': 'economy center',
        },

    'shenzhen': {
        'country': 'china',
        'population': 70,
        'fact': 'economy center',
        },

    }

for city, city_info in cities.items():
    print("\nCity: " + city.title())
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print("\tCountry: " + country.title())
    print("\tPopulation: " + str(population) + " millions")
    print("\tFact: " + fact)
