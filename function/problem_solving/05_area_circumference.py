import math

def area(r):
  return (math.pi * (r**2))

def circum(r):
  return (2 * math.pi * r)

radius = int(input("Enter the radius: "))

print(area(radius))
print(circum(radius))

def multi_return(radius):
    area = (math.pi * (r**2))
    circumference = (2 * math.pi * r)
    return area, circumference

a, c = multi_return(3)
print("Area: ", a, "Circumference: ", c)

def multi_return(radius):
    area = math.pi * (radius**2)
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = multi_return(3)
print(f"Area: {a:.2f}, Circumference: {c:.2f}")
