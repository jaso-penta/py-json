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

print(person)

person_json = json.dumps(person)
print(person_json)

person_json = json.dumps(person, indent=4)
print(person_json)