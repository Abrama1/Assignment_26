import socket


def client():
    host = socket.gethostname()
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = client_socket.recv(1024)
    print(message.decode())

    client_socket.close()


if __name__ == "__main__":
    client()
