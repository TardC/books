glossary = {
    'print': 'write words.',
    'hello': 'greeting to other people.',
    'python': 'a programming language.',
    'list': 'a series of something like.',
    'dictionary': 'key-value pairs.',
    'set': 'a series of different elements.',
    'tuple': 'like list, but immutable.',
    'sort': 'a funtion for sorting.',
    'max': 'a funtion for geting maximum.',
    'min': 'a funtion for geting minimum.',
    }

print("print: " + glossary['print'] + "\n" +
    "hello: " + glossary['hello'] + "\n" +
    "python: " + glossary['python'] + "\n" +
    "list: " + glossary['list'] + "\n" +
    "dictionary: " + glossary['dictionary'])

print("print:\n\t" + glossary['print'] + "\n" +
    "hello:\n\t" + glossary['hello'] + "\n" +
    "python:\n\t" + glossary['python'] + "\n" +
    "list:\n\t" + glossary['list'] + "\n" +
    "dictionary:\n\t" + glossary['dictionary'])


for word, meaning in glossary.items():
    print(word + ": " + meaning)
