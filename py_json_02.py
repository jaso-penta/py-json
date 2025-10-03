import json


person = {
    'first_name': 'Pero',
    'last_name': 'Peric',
    'phone': '+385 91 5887722',
    'email': 'pero@gmail.com',
    'address':{
        'street': 'Ulica 234',
        'postal_code': '23206',
        'city': 'Zadar',
        'country': 'Hrvatska'
    },
    'age': 35
}


try:
    with open('person.json', 'w') as file_writer:
        json.dump(person, file_writer, indent=4)
        

except Exception as ex:
    print(f'Dogodila se greska: {ex}! ')