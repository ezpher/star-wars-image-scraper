import requests

next = 'https://swapi.dev/api/people/?page=1'
people_list = []

while (next is not None):
    response = requests.get(next).json()
    
    people = response['results']
    people_list += people
    
    next = response['next']

####

people_total = len(people_list)
categories = {}

for (people_id, person) in enumerate(people_list):
    
    if 'people' not in categories:
        categories['people'] = []

    categories['people'].append({f'{people_id}': person['name']})

print(categories)
    