def add(n1,n2):
    return n1 + n2

def multiple(n1,n2):
    return n1 * n2

n1 = int(input("Enter first number n1: "))
n2 = int(input("Enter second number n2: "))

add_result = add(n1,n2)
mul_result = multiple(n1,n2)

print(add_result)
print(mul_result)