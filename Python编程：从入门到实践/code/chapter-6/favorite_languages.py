favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")


for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")


for name in favorite_languages.keys():
    print(name.title())


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")


if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")


print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


surveyed_persons = ['jen', 'phil', 'tom', 'lily']

for surveyed_person in surveyed_persons:
    if surveyed_person in favorite_languages.keys():
        print("Thank you taking the poll, " + surveyed_person.title())
    else:
        print("Hi " + surveyed_person.title() +
            ", please take the poll.")


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
    elif len(languages) == 1:
        print("\n" + name.title() + "'s favirite language is " +
            languages[0].title() + ".")
