import xmlrpc.client

# Connect to the server
s = xmlrpc.client.ServerProxy('http://localhost:8000')

# Call the server's factorial function
num = int(input("Enter a number to compute the factorial: "))
print(f"The factorial of {num} is {s.factorial(num)}")
