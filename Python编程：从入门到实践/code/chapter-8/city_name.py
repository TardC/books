def city_country(city_name, country):
    full_name = city_name + ', ' + country
    return full_name.title()

full_name = city_country('santiago', 'chile')
print(full_name)
full_name = city_country('beijing', 'china')
print(full_name)
full_name = city_country('Shanghai', 'China')
print(full_name)
