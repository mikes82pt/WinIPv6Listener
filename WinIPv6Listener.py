import socket

def start_listener(port):
    # Create an IPv6 socket
    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as server_socket:
        # Allow the socket to be reused
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Bind the socket to all interfaces on the specified port
        server_socket.bind(('', port))
        
        # Start listening for incoming connections
        server_socket.listen()
        print(f"Listening for connections on port {port}...")

        while True:
            # Accept a connection
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connection from {client_address}")
                # Optionally, you can send or receive data here
                data = client_socket.recv(1024)
                if data:
                    print(f"Received data: {data.decode()}")
                    client_socket.sendall(b"Data received")

if __name__ == "__main__":
    try:
        port = int(input("Enter the port number to listen on (1-65535): "))
        if 1 <= port <= 65535:
            start_listener(port)
        else:
            print("Port number must be between 1 and 65535.")
    except ValueError:
        print("Invalid input. Please enter a valid port number.")
