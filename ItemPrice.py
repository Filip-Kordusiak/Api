import requests
import sqlite3

def inter_cars():
    # Dane autoryzacyjne klienta
    client_id = 'u2qwrerewqewrqwrqerweqca'
    client_secret = 'xqrwet_Fvqwereqrwqrewqrweca'

    # Endpoint do uzyskania access_token
    token_url = 'https://is.webapi.qqwerreqwrqe.eu/oauth2/token?grant_type=client_credentials&scope=allinone'

    # Dane do wysłania w żądaniu uzyskania tokena
    token_data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    # Wysłanie żądania uzyskania tokena
    response = requests.post(token_url, data=token_data)

    # Sprawdzenie odpowiedzi
    if response.status_code == 200:
        token_info = response.json()
        access_token = token_info.get('access_token')
        print("Uzyskano access_token:", access_token)

        # Endpoint do pobrania danych o produkcie

        # Tworzenie nagłówków z autoryzacją
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }
        connection = sqlite3.connect('my_database.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        xd = 0
        for row in rows:
            if xd == 10:
                pass
            else:
                xd = xd + 1
            product_id = row[1]
            sku = row[2]
            data = {
                "lines": [
                    {
                        f"sku": sku,
                        "quantity": 1
                    }
                ]
            }
            url = 'https://api.webapi.eqwrerwq.eu/ic/pricing/quote'
            response = requests.post(url, json=data, headers=headers)

            if response.status_code == 200:
                ceny = response.json()
                print("Pomyślnie dodano SKU.", response.json())
                list_prices_net = [product["price"]["listPriceNet"] for product in ceny["lines"]]
                print(list_prices_net[0])
                print(ceny['lines'][0]['price']['listPriceNet'])
                xddd = ceny['lines'][0]['price']['listPriceNet']
                print(type(xddd))
                cursor.execute("UPDATE products SET Price = ? WHERE productID = ?",
                               (ceny['lines'][0]['price']['listPriceNet'], product_id))

            else:
                print("Wystąpił problem przy dodawaniu SKU. Kod odpowiedzi:", response.status_code)
        connection.commit()
        connection.close()

inter_cars()
