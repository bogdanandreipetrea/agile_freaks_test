import sys
import urllib.request
import math


# Parse the input arguments
user_lat, user_long, shop_data_url = sys.argv[1], sys.argv[2], sys.argv[3]

# Download the coffee shop list
with urllib.request.urlopen(shop_data_url) as url:
    coffee_shops = url.read().decode('utf-8')

# Parse coffee shop list
shops = []
for line in coffee_shops.split('\n'):
    if not line:
        continue
    try:
        name, x, y = line.split(',')
        shops.append({'name': name, 'x': float(x), 'y': float(y)})
    except ValueError:
        print('Error parsing line:', line)

# Compute distance between the user and each coffee shop
distance = []
for shop in shops:
    x_lat = shop['x']
    x_long = shop['y']
    distance = math.sqrt((x_lat - float(user_lat))**2 + (x_long - float(user_long))**2)
    shop['distance'] = distance


# Sort shops by distance
shops.sort(key=lambda s: s['distance'])

# Print the three closest coffee shops and distance with maximum 4 decials
for shop in shops[:3]:
    print(f"{shop['name']},{shop['distance']:.4f}")
