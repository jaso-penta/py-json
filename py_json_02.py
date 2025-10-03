import json


contacts = [
    {
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
},
    {
    'first_name': 'Jure',
    'last_name': 'Juro',
    'phone': '+385 91 4567722',
    'email': 'pero@gmail.com',
    'address':{
        'street': 'Ulica 111',
        'postal_code': '23336',
        'city': 'Zagreb',
        'country': 'Hrvatska'
    },
    'age': 25
}
]

try:
    with open('contacts.json', 'w') as file_writer:
        json.dump(contacts, file_writer, indent=4)

except Exception as ex:
    print(f'Dogodila se greska: {ex}! ')