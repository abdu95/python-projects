# We use dictionaries in situations where we want to store information that comes as key value pairs
# Name: John Smith
# Email: john@gmail.com
# Phone: 1234
customer = {
    "name": "John Smith",
    "age": 23,
    "is_verified": True
}
# keys should be unique: Dictionary contains duplicate keys 'age'
# just like the dictionaries we have in the real world, in a real dictionary we have a bunch of words and there are definition of each word
# each word is only listed once in a dictionary
# keys only can be strings and numbers??
# value can be anything: a string, a number, a boolean, a list

# we can access each item in this dictionary using [ ]. this will return the value associated with the "name" key
print(customer["name"])
# if we pass a key that doesn't exist
# print(customer["birthdate"])  # KeyError: 'birthdate'
# case sensitive
# print(customer["Name"])  # KeyError: 'Name'
# to get around this we can use the get() method. if you use a key that doesn't exist here, it doesn't yell at us. it simply returns None
# None - is an object in python that represents the absence of a value.
print(customer.get("birthdate"))
# we can also optionally supply a default value, if this dictionary doesn't have this key
print(customer.get("birthdate", "Jan 1 1980"))

# We can also update the values
customer["name"] = "Jack Smith"
# add a new key
customer["birthdate"] = "Jan 1 2000"