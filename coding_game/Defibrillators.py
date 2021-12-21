import sys
import math

def distance(lonA, latA, lonB, latB):
    x = (lonB - lonA)*math.cos((latA + latB)/2)
    y = latB - latA
    return (x**2 + y**2)**0.5 * 6371
city = ''
dis = 0
lon = float(input().replace(',', '.'))
lat = float(input().replace(',', '.'))
n = int(input())
x = [input().replace(',', '.').split(';')  for _ in range(n)]
for i in x:
    d = distance(lon, lat, float(i[-2]), float(i[-1]))
    if d < dis or i == x[0]:
        dis = d
        city = i[1]

print(city)
