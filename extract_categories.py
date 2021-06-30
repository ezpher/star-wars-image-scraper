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

        categories[f'{category}'].append(
            {
                'category': f'{category}', 
                'id': int(item_id + 1),
                f'{item_identifier}': item[item_identifier], 
                'search_terms': 'Star Wars: Episode ' + item[item_identifier] if category == 'films' else item[item_identifier]    
            })

    return categories

def get_output_filepath():
    
    curr_dir = os.path.dirname(__file__)
    rel_path = 'output\output.txt' # for windows os
    abs_path = os.path.join(curr_dir, rel_path)

    return abs_path

def data_to_textfile(data):

    abs_path = get_output_filepath()

    with open(abs_path, 'wt') as output_file:
        json.dump(data, output_file)

    print('output file: ', abs_path)


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
        