""" item = {
    'name': 'iPhone Pro Max 17',
    'price': '$1099',
    'department': 'Phones'
}

print(item['name']) """




best_buy_items = [
{
    'name': 'iPhone Pro Max 17',
    'price': '$1099',
    'department': 'Phones'
},

{
    'name': 'Samsung Galaxy s27',
    'price': '$799',
    'department': 'Phone'
},

{
    'name': 'Samsung OLED 4K S9OF Smart TV',
    'price': '1099.99',
    'department': 'TV'
},

{
    'name': 'Samsung Galaxy Buds3 Pro',
    'price': '$249.99',
    'department': 'Airpod'
}
]
for index, item in enumerate(best_buy_items):
    print(index, ':', item['name'])
    