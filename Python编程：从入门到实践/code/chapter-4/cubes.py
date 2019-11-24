cubes = []
for value in range(1, 11):
	cubes.append(value**3)
for cube in cubes:
	print(cube)

cubes = [value**3 for value in range(1, 11)]
for cube in cubes:
	print(cube)
