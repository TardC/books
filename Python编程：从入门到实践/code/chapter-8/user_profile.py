def build_profile(first, last, **user_info):
    """
    Create a dictionary that contains everything we know about the user.
    """
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

my_profile = build_profile('c', 'tard',
                           age=18,
                           city='Beijing',
                           country='China')
print(my_profile)
