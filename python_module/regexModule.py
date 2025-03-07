# re is Python's built-in regular expression module that allows pattern matching in strings. It helps in validating, searching, and replacing patterns efficiently.

import re

def email_validator():
    email = input("Enter an email address: ")
    
    # Define a pattern using a raw string (r"...") with regex rules.
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# re.match(pattern, string) checks if the beginning of the string matches the pattern. It does not check the entire string.

# re.fullmatch(pattern, string) ensures that the ENTIRE string matches the pattern.

    if re.fullmatch(pattern, email):
        print(f"{email} is a valid email!")
    else:
        print(f"{email} is an invalid email. Please try again.")

email_validator()



# pattern = r'^\d{3} \d{4}-\d{6}$'

pattern = r'^880-\d{4}-\d{6}$'

# phone = "(123) 456-7890"
phone = "880-1785-XXXXXX"

if re.fullmatch(pattern, phone):
    print("Valid phone number")
else:
    print("Invalid phone number")


pattern = r'^(https?://)?(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+(/[a-zA-Z0-9-._~:/?#@!$&\'()*+,;=]*)?$'

url = "https://www.google.com/search?q=python"

if re.fullmatch(pattern, url):
    print("Valid URL")
else:
    print("Invalid URL")



pattern = r"\d+"  # Match one or more digits

text = "My age is 25 and my brother is 30."

# re.findall() → Find all matches
matches = re.findall(pattern, text)
print(matches)  # Output: ['25', '30']

# re.search() → Find first match
match = re.search(pattern, text)
print(match.group())  # Output: '25'

# re.sub() → Replace matches
new_text = re.sub(pattern, "XX", text)
print(new_text)  # Output: "My age is XX and my brother is XX."
