# Use to store KEY VALUE PAIR e.g name:Yogi, email:y@scania.com, phone: 1234

customer = {
    "name": "Yogi Sri",
    "age": 40,
    "is_verified": True
}

print(customer["name"])  # Yogi Sri
#print(customer["DOB"])  # KeyError: 'DOB' - No key exists
#print(customer["Name"])  # KeyError: 'Name' - No key exists
print(customer.get("Name"))  # None - none is an object that represents the absence of a value - to avoid error use get
print(customer.get("DOB"))  # None - none is an object that represents the absence of a value - to avoid error use get
print(customer.get("DOB", "05-10-1982"))  # 05-10-1982

customer["name"] = "Yo Sri" # Can update the value as
print(customer["name"])  # Yo Sri

customer["phone"] = "1234" #Can ADD the new key value pairs as well
print(customer["phone"])  # 1234