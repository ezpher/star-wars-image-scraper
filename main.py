import os
import requests
import json

def get_category_items(category, master_dict = {}):

    next = f'https://swapi.dev/api/{category}/?page=1'
    category_list = []
    item_identifier = ''

    while (next is not None):
        response = requests.get(next).json()
        
        items = response['results']
        category_list += items
        
        next = response['next']

        if not item_identifier: 
            item_identifier = 'title' if not items[0].get('name') else 'name'

    ####

    categories = master_dict

    for (item_id, item) in enumerate(category_list):
        
        if f'{category}' not in categories:
            categories[f'{category}'] = []

        categories[f'{category}'].append({f'{item_id}': item[item_identifier]})

    return categories

def data_to_textfile(data):

    curr_dir = os.path.dirname(__file__)
    rel_path = 'output\output.txt' # for windows os
    abs_path = os.path.join(curr_dir, rel_path)

    print('output file: ', abs_path)

    with open(abs_path, 'wt') as output_file:
        json.dump(data, output_file)


if __name__ == '__main__':

    categories = {}
    categories = get_category_items('people', categories)
    categories = get_category_items('films', categories)
    categories = get_category_items('starships', categories)
    categories = get_category_items('vehicles', categories)
    categories = get_category_items('species', categories)
    categories = get_category_items('planets', categories)

    data_to_textfile(categories)

    # print(json.dumps(categories))
    # print(categories)
        