password = "1234@aAa"

if len(password) < 6:
    strength = "Weak"
elif len(password)<= 10:
    strength = "Medium"
else: 
    strength = "Strong"

print("Pawword strength is: ", strength)