def make_album(singer, name, songs_number=''):
    album = {'singer': singer, 'name': name}
    if songs_number:
        album['songs_number'] = songs_number
    return album

while True:
    print("\nPlease enter the name of the singer and album:")
    print("(enter 'q' at any time to quit)")

    singer = input("Singer name: ")
    if singer == 'q':
        break

    name = input("Album name: ")
    if name == 'q':
        break

    album = make_album(singer, name)
    print(album)
