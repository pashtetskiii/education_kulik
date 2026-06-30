import collections

with open('shop', encoding='utf-8') as shop_file:
    shops = list(map(lambda x: x.replace('\n', ''), shop_file.readlines()))

city_shops = collections.defaultdict(list)
for line in shops:
    shop, city = line.split(':')
    city_shops[city].append(shop)

print(city_shops)