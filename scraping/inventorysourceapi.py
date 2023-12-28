import requests
import json
import pandas as pd

url = "https://app.inventorysource.com/api/supplier/directory-search"

final = []

page_no = 4
for x in range(1, page_no + 1):
    payload = {
        "search": None,
        "current_page": f'{x}',
        "sort_on": "popularity",
        "sort_descending": True,
        "supplier_type_integrated": 1,  
        "catalog_type": None,
        "location": None,
        "category": [],
        "ships_location": [],
        "allows_dropship": None,
        "minimum_order": None,
        "supplier_attribute": None,
        "allows_amazon": None,
        "allows_ebay": None,
        "verified": None
    }
    headers = {
        'authority': 'app.inventorysource.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.6',
        'app-id': '1698328794000',
        'content-type': 'application/json;charset=UTF-8',
        'cookie': 'intercom-device-id-yajnigow=dc5008db-42b1-419c-8d6d-fd5dcf81d100; JSESSIONID=E999EF9C6E2910DEC28D585CFD216370; XSRF-TOKEN=d6ba2672-fc61-44f3-b0b1-785fb31515ef; intercom-session-yajnigow=NGpRb1VLdFRFUXhZUzlxU2dwUXk5bmVOS0M2QWM2S1h0cDNHYzdGSjlRSkFpN2dqZkJaVEd1TExudkp5emZWaC0tbXp3ZkJ3dFlWUVlxVmJ2eDZTbDVwZz09--f2e3c582697f04c2c633d1c023846df8eeaae4dd; JSESSIONID=2F2FCE3C959006D9B474803F9BE7F70D',
        'origin': 'https://app.inventorysource.com',
        'referer': 'https://app.inventorysource.com/',
        'sec-ch-ua': '"Chromium";v="118", "Brave";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'uid': '2540177',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'x-xsrf-token': 'd6ba2672-fc61-44f3-b0b1-785fb31515ef'
        }

    response = requests.post(url, json=payload, headers=headers)
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse JSON response
        # Loop through the 'dropshippers' and access the 'categories' and 'catalog_category_name' fields
        for dropshipper in data['dropshippers']:
            dropshipper_name = dropshipper.get('dropshipper_name')
            print(dropshipper_name)

            dropshipper_location_name = dropshipper.get('dropshipper_location_name')
            print(dropshipper_location_name)

            ship_to_locations = dropshipper['ship_to_locations']
            dropshipper_locations = ', '.join([ship.get('dropshipper_location_name') for ship in ship_to_locations])
            print(dropshipper_locations)

            catalog_type = bool(dropshipper.get('allow_browse'))
            print(catalog_type)

            minimum_order = dropshipper.get('minimum_order')
            print(minimum_order)

            allows_dropship = dropshipper.get('allows_dropship')
            print(allows_dropship)

            allows_amazon = bool(dropshipper.get('allows_amazon'))
            print(allows_amazon)

            allows_ebay = bool(dropshipper.get('allows_ebay'))
            print(allows_ebay)

            categories = dropshipper['categories']
            catalog_category_name = ','.join([category.get('catalog_category_name') for category in categories])
            print(catalog_category_name)

            total_count = dropshipper.get('total_count')
            print(total_count)

            dropship_data = {
                'dropshipper name': dropshipper_name,
                'Ships from': dropshipper_location_name,
                'Ships to': dropshipper_locations,  # Store multiple values as a single string
                'Catalog type': catalog_type,
                'Minimum order': minimum_order,
                'Allows dropship': allows_dropship,
                'Allows Amazon': allows_amazon,
                'Allows_ebay': allows_ebay,
                'Supplier categories': catalog_category_name,
                'Number of Products': total_count
            }

            final.append(dropship_data)

    else:
        print(f"Request failed with status code {response.status_code}")

df = pd.DataFrame(final)
df.to_csv('inventorysource.csv', index=False)
