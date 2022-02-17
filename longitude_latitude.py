from math import sin, cos, sqrt, atan2
Radius = 3956.0

latitude1=float(input("enter the 1st latitude value:"))
latitude2=float(input("enter the 2st latitude value:"))
longitude1=float(input("enter the 1st longitude value:"))
longitude2=float(input("enter the 1st longitude value:"))

distance_latitude=latitude2-latitude1
distance_longitude=longitude2-longitude1

area1 = sin(distance_latitude / 2)**2 + cos(latitude1) * cos(latitude2) * sin(distance_longitude / 2)**2
area2 = 2 * atan2(sqrt(area1), sqrt(1 - area1))

distance = Radius * area2

print("Distance is:",distance)
