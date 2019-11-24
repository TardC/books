guests = ['a', 'b', 'c']
print(guests)

print(guests[2] + ' is not free.')
guests[2] = 'C'
print(guests)

print('I found a bigger table.')
guests.insert(0, 'A')
guests.insert(2, 'B')
guests.append('d')
print(guests)

print('I can just invite two persons, because the bigger table will not arrive timely.')
popped_guest = guests.pop()
print(popped_guest + ', I am sorry.')
popped_guest = guests.pop()
print(popped_guest + ', I am sorry.')
popped_guest = guests.pop()
print(popped_guest + ', I am sorry.')
popped_guest = guests.pop()
print(popped_guest + ', I am sorry.')
print(guests[1] + ', you are in list.')
print(guests[0] + ', you are in list.')
print('I totally invite ' + str(len(guests)) + ' guests.')
del guests[1]
del guests[0]
print(guests)
