## Overview

You have been hired by a company that builds a app for coffee addicts.  You are 
responsible for taking the user’s location and returning a list of the three closest coffee shops.

## Input

The coffee shop list is a comma separated file with rows of the following form:
`Name,Y Coordinate,X Coordinate`

The quality of data in this list of coffee shops may vary.  Malformed entries should cause the 
program to exit appropriately. 

Your program will be executed directly from the command line and will be provided three 
arguments in the following order:
`<user x coordinate> <user y coordinate> <shop data url>`

Notice that the data file will be read from an network location (ex: https://raw.githubusercontent.com/Agilefreaks/test_oop/master/coffee_shops.csv)

## Output

Write a program that takes the user’s coordinates encoded as listed above and prints out a 
newline­separated list of the three closest coffee shops (including distance from the user) in 
order of closest to farthest.  These distances should be rounded to four decimal places. 

Assume all coordinates lie on a plane.

The output should be very simple no UI is required.

## Example

Using the [coffee_shops.csv](coffee_shops.csv)

__Input__

`47.6 -122.4 coffee_shops.csv`

__Expected output__

```
Starbucks Seattle2,0.0645
Starbucks Seattle,0.0861
Starbucks SF,10.0793
```


## Parse the input arguments
user_lat, user_long, shop_data_url = sys.argv[1], sys.argv[2], sys.argv[3]

## Download the coffee shop list
with urllib.request.urlopen(shop_data_url) as url:
    coffee_shops = url.read().decode('utf-8')

## Parse coffee shop list
shops = []
for line in coffee_shops.split('\n'):
    if not line:
        continue
    try:
        name, x, y = line.split(',')
        shops.append({'name': name, 'x': float(x), 'y': float(y)})
    except ValueError:
        print('Error parsing line:', line)

## Compute distance between the user and each coffee shop
distance = []
for shop in shops:
    x_lat = shop['x']
    x_long = shop['y']
    distance = math.sqrt((x_lat - float(user_lat))**2 + (x_long - float(user_long))**2)
    shop['distance'] = distance


## Sort shops by distance
shops.sort(key=lambda s: s['distance'])

## Print the three closest coffee shops and distance with maximum 4 decials
for shop in shops[:3]:
    print(f"{shop['name']} , {shop['distance']:.4f}")
