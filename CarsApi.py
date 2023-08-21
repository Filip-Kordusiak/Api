import requests
def inter_cars():
# Dane autoryzacyjne klienta
    client_id = 'u2YqweffewqqwfqfweqfweqfewJECfqwqfwK0Jca'
    client_secret = 'xVBt_Fvfewqfweqqfwfqweqfweqfwe3utZE7ca'

    # Endpoint do uzyskania access_token
    token_url = 'https://is.webapi.qfwfqwefew.eu/oauth2/token?grant_type=client_credentials&scope=allinone'

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
        skus = ["D92F9B", "D99807", "DA367A", "B0C805", "B0E3A9", "DCAE3C", "DCAE66", "DCAF46", "DCB02A", "DCB189",
                "DD1207", "DDFA48", "DE228C", "B536CD", "DEB2DD", "BAE3B9", "BAEA29", "BAEF32", "E255FE", "BBD5CE",
                "BBD801", "E2DD19", "E2EBF8", "E3CD3B", "C0C12B", "E51F6A", "C33D64", "C3C36F", "C49FB8", "C4A2A5",
                "E7692E", "C4DD0E", "C5CDEA", "C72F72", "CAEF81"]
        for i in skus:
            product_url = f'https://api.webapi.qffqwefweq.eu/ic/inventory/stock?sku={i}'
            product_response = requests.get(product_url, headers=headers)

            if product_response.status_code == 200:
                product_data = product_response.json()
                print("Dane o produkcie:", product_data)
                total_availability = sum(item['availability'] for item in product_data)
                print("Sum of Availability:", total_availability)
            else:
                print("Błąd podczas uzyskiwania access_token. Kod statusu:", response.status_code)
    ##


    data = {
        "lines": [
            {
                "sku": "DCAE66",
                "quantity": 100
            },
            {
                "sku": "ABC123",
                "quantity": 50
            },
            {
                "sku": "XYZ789",
                "quantity": 80
            }
        ]
    }
    url = 'https://api.webapi.fqwefewqs.eu/ic/pricing/quote'
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        ceny = response.json()
        print("Pomyślnie dodano SKU.", response.json())
        list_prices_net = [product["price"]["listPriceNet"] for product in ceny["lines"]]
        print(list_prices_net)
    else:
        print("Wystąpił problem przy dodawaniu SKU. Kod odpowiedzi:", response.status_code)
inter_cars()