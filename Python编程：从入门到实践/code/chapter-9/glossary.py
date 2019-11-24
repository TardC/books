from collections import OrderedDict

glossary = OrderedDict()

glossary['print'] = 'write words.'
glossary['hello'] = 'greeting to other people.'
glossary['python'] = 'a programming language.'
glossary['list'] = 'a series of something like.'
glossary['dictionary'] = 'key-value pairs.'

for word, meaning in glossary.items():
    print(word + ": " + meaning)
