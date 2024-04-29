from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Create server listening on port 8000
with SimpleXMLRPCServer(('localhost', 8000)) as server:
    server.register_introspection_functions()
    server.register_function(factorial, 'factorial')

    # Run the server's main loop
    print("Serving XML-RPC on localhost port 8000...")
    server.serve_forever()
