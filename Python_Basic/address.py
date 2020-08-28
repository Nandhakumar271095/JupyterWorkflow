book = {}
book['tom'] = {
    'name': 'tom',
    'address': '2/173, pudhu nagar, TN-100',
    'Phone': 8754481591
}
book['Jim'] = {
    'name': 'Jim',
    'address': '4/74, NSK nagar, TN-115',
    'Phone': 9551739417
}

import _json
s=json.dumps(book)
print(s)
