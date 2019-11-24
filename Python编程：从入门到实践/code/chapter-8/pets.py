def describe_pet(pet_name, animal_type='dog'):
    """Show pet's information."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# a dog named Willie
describe_pet('willie')
describe_pet(pet_name='willie')

# a hamster named Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
