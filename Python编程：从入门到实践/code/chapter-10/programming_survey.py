filename = 'programming_survey.txt'

with open(filename, 'a') as file_object:
    while True:
        answer = input("Why do you like programming? ")
        file_object.write(answer + "\n")
