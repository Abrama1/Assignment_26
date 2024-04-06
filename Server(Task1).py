import socket


def server():
    host = socket.gethostname()
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server is listening...")

    while True:
        conn, addr = server_socket.accept()
        print("Connection established with: ", addr)
        conn.send("Connection successful!".encode())
        conn.close()

if __name__ == "__main__":
    server()
