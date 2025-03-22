import math

def area(r):
  return (math.pi * (r**2))

def circum(r):
  return (2 * math.pi * r)

radius = int(input("Enter the radius: "))

print(area(radius))
print(circum(radius))