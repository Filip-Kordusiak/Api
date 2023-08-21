import requests
import sqlite3

# Dane autoryzacyjne klienta
client_id = 'sklep-qwerrewqqwrerqwrweq'
client_secret = 'sklep-fdsfadfqwerfevftgtbvtrvrrwsgvregewfew'

# Endpoint do uzyskania access_token
token_url = 'https://qfwqfwefqew.pl/api/auth/access_token'

# Dane do wysłania w żądaniu uzyskania tokena
token_data = {
    'grant_type': 'client_credentials',
    "scope": "READWRITE",
    'client_id': client_id,
    'client_secret': client_secret
}

# Wysłanie żądania uzyskania tokena
response = requests.post(token_url, data=token_data)

if response.status_code == 200:
    token_info = response.json()
    access_token = token_info.get('access_token')
    print("Uzyskano access_token:", access_token)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    xd = 0
    datasel = {
        "products": []
    }
    for row in rows:
        print(row)
        product_id = row[1]
        price = row[4]
        products = {
            "product_id": product_id,
            "price": price
        }

        datasel["products"].append(product)
        url = 'fqwefewqfewqwfqeqw.pl/api/products/helper/price_update'
        response = requests.post(url, json=product, headers=headers)



        if xd == 10:

            break
        else:
            xd = xd + 1