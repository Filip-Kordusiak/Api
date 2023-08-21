import json

# Tworzenie struktury początkowej JSON
data = {
    "products": []
}

# Symulacja dodawania produktów w pętli
for i in range(10):  # Możesz zmienić liczbę produktów według potrzeb
    product_id = i

    price = i * 10  # Cena dla przykładu

    product = {
        "product_id": product_id,

        "price": price
    }

    data["products"].append(product)

# Zapisywanie danych do pliku JSON
print(data)
with open("output.json", "w") as outfile:
    json.dump(data, outfile, indent=2)

print("Plik JSON został utworzony i wypełniony danymi.")
