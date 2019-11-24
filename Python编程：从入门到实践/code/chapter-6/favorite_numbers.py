favorite_numbers = {
    'lily': 0,
    'andrew': 1,
    'tom': 2,
    'jen': 3,
    'phil': 4,
    }

print("Lily's favorite number: " + str(favorite_numbers['lily']) + "\n" +
    "Andrew's favorite number: " + str(favorite_numbers['andrew']) + "\n" +
    "Tom's favorite number: " + str(favorite_numbers['tom']) + "\n" +
    "Jen's favorite number: " + str(favorite_numbers['jen']) + "\n" +
    "Phil's favorite number: " + str(favorite_numbers['phil']) + "\n")

print("Lily's favorite number: " + str(favorite_numbers['lily']))
print("Andrew's favorite number: " + str(favorite_numbers['andrew']))
print("Tom's favorite number: " + str(favorite_numbers['tom']))
print("Jen's favorite number: " + str(favorite_numbers['jen']))
print("Phil's favorite number: " + str(favorite_numbers['phil']))


favorite_numbers = {
    'lily': [0],
    'andrew': [1, 6],
    'tom': [2, 8],
    'jen': [3, 7, 8],
    'phil': [4, 9],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favorite number(s) is/are:")
    for number in numbers:
        print("\t" + str(number))

for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print("\n" + name.title() + "'s favorite numbers are:")
        for number in numbers:
            print("\t" + str(number))
    elif len(numbers) == 1:
        print("\n" + name.title() + "'s favorite number is " +
            str(number) + ".")
