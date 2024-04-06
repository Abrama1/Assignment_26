import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

clients = []
history = []


def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received from {client_address}: {message}")
                history.append(message)
                with open('chat_history.txt', 'a') as file:
                    file.write(f"{message}\n")
                for c in clients:
                    if c != client_socket:
                        c.sendall(message.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            clients.remove(client_socket)
            client_socket.close()
            break


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print(f"Server is listening on {HOST}:{PORT}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connected to {client_address}")
            clients.append(client_socket)
            threading.Thread(target=handle_client, args=(client_socket, client_address)).start()


if __name__ == "__main__":
    main()
