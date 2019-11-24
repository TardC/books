def get_formatted_cityname(city, country, population=''):
    """Return a neatly formatted cityname."""
    formatted_cityname = city + ', ' + country
    formatted_cityname = formatted_cityname.title()
    if population:
        formatted_cityname += ' - population ' + str(population)
    return formatted_cityname
