import requests
import json
import csv
import time
from random import randint

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Accept': '*/*'
}

def get_data():

    all_data = []

    with open('all_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
            'Название', 'Бренд', 'Рейтинг', 'Цена', 'Цена со скидкой'
            )
        )

    count = 1

    while True:
        try:
            url = f'https://catalog.wb.ru/catalog/electronic15/catalog?appType=1&curr=rub&dest=-1257786&page={count}&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,22,1,31,66,110,48,71,114&sort=popular&spp=0&subject=2290&uclusters=0'
            response = requests.get(url=url, headers=headers)
            data = response.json()

            for item in data['data']['products']:
                name = item['name']
                brand = item['brand']
                price = item['priceU']/100
                sale_price = item['salePriceU']/100
                rating = item['reviewRating']
                all_data.append(
                    {
                        'name': name,
                        'brand': brand,
                        'rating': rating,
                        'price': price,
                        'sale price': sale_price
                    }
                )

                with open('all_data.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        (
                        name, brand, rating, price, sale_price
                        )
                    )
                
                time.sleep(2)

            count += 1
        except:

            with open('all_data.json', 'w', encoding='utf-8') as file:
                json.dump(all_data, file, indent=4, ensure_ascii=False)

            return 'Страницы закончились. Парсинг завершён!'


def main():
    get_data()

if __name__=='__main__':
    main()


