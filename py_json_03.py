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



def save_to_json_file(data_to_save, file_name = 'contacts.json', writing_mode = 'w'):
    try:
        with open(file_name, writing_mode) as file_writer:
            json.dump(data_to_save, file_writer, indent=4)

    except Exception as ex:
        print(f'Dogodila se greska: {ex}! ')


save_to_json_file(contacts)


new_contact = {
    'first_name': 'Marko',
    'last_name': 'Maric',
    'phone': [
        '+385 91 4523111',
        '+385 91 4321855'
    ],
    'email': 'marko@gmail.com',
    'address':{
        'street': 'Ulica 314',
        'postal_code': '10000',
        'city': 'Rjeka',
        'country': 'Hrvatska'
    },
    'age': 44
}

contacts.append(new_contact)

save_to_json_file(contacts)



