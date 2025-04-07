# format specifiers = {value:flags} format a value based on what flags are inserted.


# .(number)f = round to that many decimal places (fixed point)
# :(number)  = allocate that many spaces
# :03        = allocate and zero pad that many spaces
# :<  = left justify
# :>  = right justify
# :^  = center align
# :+  = use a plus sign to indicate positive value
# :=  = place sign to left most position
# :   = insert a space before positive numbers
# :,  = comma separator


# format specifiers

price1 = 3.14159
price2 = -889.65
price3 = 12.45
price4 = 856.99
price5 = 34829
price6 = 38827.327
price7 = 29487.8999

# print(f"Price 1 is ${price1}")
# print(f"Price 2 is ${price2}")
# print(f"Price 3 is ${price3}")


print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:>10}")
print(f"Price 4 is ${price4:+}")


# thousand separator

print(f"Price 5 is ${price5:,}")

# thousand separator and decimal specifier

print(f"Price 6 is ${price6:,.2f}")

# thousand separator and decimal specifier and precede with plus sign

print(f"Price 7 is ${price7:+,.2f}")
