import requests
import sqlite3



def inter_cars():
# Dane autoryzacyjne klienta
    client_id = 'u2YcXtBfsdagfasdgasgrtfva'
    client_secret = 'xVBt_FasdffasdsfaffggaE7ca'

    # Endpoint do uzyskania access_token
    token_url = 'https://is.webapi.fwefrewfre.eu/oauth2/token?grant_type=client_credentials&scope=allinone'

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
        data = {
            "sku": "ADDFFA"
        }
        # Wysłanie żądania pobrania danych o produkcie
        connection = sqlite3.connect('my_database.db')
        cursor = connection.cursor()

        # Wykonaj zapytanie SELECT, aby pobrać wszystkie rekordy z tabeli products
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        xd = 0
        for row in rows:
            if xd == 10:
                break
            else:
                xd = xd +1
            product_url = f'https://api.webapi.fqfrqfqrfr.eu/ic/inventory/stock?sku={row[2]}'
            product_response = requests.get(product_url, headers=headers)

            if product_response.status_code == 200:
                product_data = product_response.json()
                print("Dane o produkcie:", product_data)
                total_availability = sum(item['availability'] for item in product_data)
                print("Sum of Availability:",  total_availability)
                product_id = row[1]

                cursor.execute("UPDATE products SET Quantity = ? WHERE productID = ?",
                               (total_availability, product_id))
                try:
                    print(product_data[0]["sku"],)
                except:
                    pass
            else:
                print("Błąd podczas uzyskiwania access_token. Kod statusu:", response.status_code)
        connection.commit()
        connection.close()
    ##

inter_cars()