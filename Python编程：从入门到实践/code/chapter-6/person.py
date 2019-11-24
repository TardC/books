person_0 = {
    'first_name': 'c',
    'last_name': 'tard',
    'age': 16,
    'city': 'beijing',
    }

person_1 = {
    'first_name': 'xx',
    'last_name': 'l',
    'age': 16,
    'city': 'beijing',
    }

person_2 = {
    'first_name': 'st',
    'last_name': 'l',
    'age': 16,
    'city': 'beijing',
    }

people = [person_0, person_1, person_2]

for person in people:
    full_name = person['first_name'] + " " + person['last_name']
    age = person['age']
    city = person['city']
    print("\nName: " + full_name.title())
    print("\tAge: " + str(age)) 
    print("\tCity: " + city.title())

    print("\nName: " + full_name.title() + "\n" +
        "\tAge: " + str(age) + "\n" +
        "\tCity: " + city.title())

print("His name is " +
    person_0['first_name'].title() + " " + person_0['last_name'].title() +
    ", his age is " + str(person_0['age']) +
    ", he live in " + person_0['city'].title() + ".")
