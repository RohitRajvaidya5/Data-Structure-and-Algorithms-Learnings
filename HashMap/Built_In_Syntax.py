
# What is hashmaps ?

# A HashMap is a data structure that stores key–value pairs and allows fast lookup, 
# insertion, and deletion using a hashing function.

# In Python, you can use a dictionary to implement a HashMap.
# Example of using a HashMap (dictionary) in Python:

# Create a HashMap (dictionary) with built-in syntax
hashmap = {}

# Insert key-value pairs into the HashMap
hashmap["name"] = "Alice"
hashmap["age"] = 30
hashmap["city"] = "New York"

# Retrieve values using keys
print(hashmap["name"])
print(hashmap["age"])
print(hashmap["city"])


# with collection module in python
from collections import defaultdict

# Create a HashMap using defaultdict
hashmap_with_collection_int = defaultdict(int)
hashmap_with_collection_int["rohit"] = 100
hashmap_with_collection_int["roshan"] = 98
hashmap_with_collection_int["pritam"] = 95

# Retrieve values using keys
print(hashmap_with_collection_int["rohit"])
print(hashmap_with_collection_int["roshan"])
print(hashmap_with_collection_int["pritam"])


hashmap_with_collection_any_datatype = defaultdict(list)
hashmap_with_collection_any_datatype["fruits"].append("apple")
hashmap_with_collection_any_datatype["fruits"].append("banana")
hashmap_with_collection_any_datatype["fruits"].append("orange")
hashmap_with_collection_any_datatype["vegetables"] = ["carrot", "broccoli", "spinach"]


# Retrieve values using keys
print(hashmap_with_collection_any_datatype)




