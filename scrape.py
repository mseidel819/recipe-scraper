import json
from get_urls import get_urls
from create_json import create_json


categories = ['bread', "breakfast-treats", "desserts/cakes", "desserts/cookies", "desserts/pies"]

total = 0
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

for category in categories:
    url = f'https://sallysbakingaddiction.com/category/{category}/'
    href_list = get_urls(url, HEADERS)
    json_data = create_json(href_list, HEADERS)
    total += len(json_data)
    cleaned_filename = category.replace("/", "-")
    with open(f'sallys-baking-addiction/{cleaned_filename}.json', "w") as json_file:
        json.dump(json_data, json_file, indent=2)

    print(f'{category}.json successfully written!')

print(f'Success! {total} recipes were downloaded')
