import ipaddress
import socket


def main():
    try:
        mysocket = socket.socket()
        mysocket.connect(('127.0.0.1', 50000))
        print(" connection estabilish..")
        while True:
            serverData = mysocket.recv(2048).decode()
            print(f"message from server: {serverData}")

            if serverData == "exit":
                print("connection as closed by server".encode())
                mysocket.close()
                break

            sendData = input("message to server : ")
            mysocket.send(sendData.encode())
            if sendData == "exit":
                print("connection as closed by client".encode())
                mysocket.close()
                break
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
