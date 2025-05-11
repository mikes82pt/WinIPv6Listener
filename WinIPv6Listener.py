import socket
def start_tcp_listener(port):
    # Create an IPv6 TCP socket
    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as server_socket:
        # Allow the socket to be reused
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Bind the socket to all interfaces on the specified port
        server_socket.bind(('', port))
        
        # Start listening for incoming connections
        server_socket.listen()
        print(f"Listening for TCP connections on port {port}...")
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
def start_udp_listener(port):
    # Create an IPv6 UDP socket
    with socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) as server_socket:
        # Bind the socket to all interfaces on the specified port
        server_socket.bind(('', port))
        print(f"Listening for UDP connections on port {port}...")
        while True:
            # Receive data from any client
            data, client_address = server_socket.recvfrom(1024)
            print(f"Connection from {client_address}")
            print(f"Received data: {data.decode()}")
            server_socket.sendto(b"Data received", client_address)
if __name__ == "__main__":
    print("WinIPv6Listener v1.1")
    try:
        port = int(input("Enter the port number to listen on (1-65535): "))
        if 1 <= port <= 65535:
            protocol = input("Choose protocol (tcp/udp): ").strip().lower()
            if protocol == 'tcp':
                start_tcp_listener(port)
            elif protocol == 'udp':
                start_udp_listener(port)
            else:
                print("Invalid protocol. Please choose 'tcp' or 'udp'.")
        else:
            print("Port number must be between 1 and 65535.")
    except ValueError:
        print("Invalid input. Please enter a valid port number.")
