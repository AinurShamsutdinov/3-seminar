elemens_tuple = int(123), float(23.45), 'Hello World!'
dictionary = dict()
for item in elemens_tuple:
    type_of_element = type(item)
    dictionary[type_of_element] = item
print(f'{elemens_tuple = }')
print(f'{dictionary = }')
