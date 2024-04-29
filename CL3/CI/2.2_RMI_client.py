import Pyro4

uri = "PYRO:example.stringconcatenator@localhost:9090"
string_concatenator = Pyro4.Proxy(uri)

# Input strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Concatenate strings
result = string_concatenator.concatenate(str1, str2)
print(f"Concatenated string: {result}")
