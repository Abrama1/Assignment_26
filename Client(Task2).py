import socket
import threading

HOST = '127.0.0.1'
PORT = 65432


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except Exception as e:
            print(f"Error: {e}")
            break


def main():
    name = input("Enter your name: ")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print("Connected to server")

        threading.Thread(target=receive_messages, args=(client_socket,)).start()

        while True:
            message = input()
            if message.lower() == 'exit':
                break
            message = f"{name}: {message}"
            client_socket.sendall(message.encode('utf-8'))


if __name__ == "__main__":
    main()
