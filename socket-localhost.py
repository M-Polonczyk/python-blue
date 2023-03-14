import ipaddress
import socket
from random import randrange
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




    dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(5):
        dice[randrange(1, 7)] += 1
    print(dice)
    classroom = []
    for i in range(7):
        classroom.append([])
        for students in range(1,11):
            classroom[i].append(students)
    for students in classroom:
        print(students)


if __name__ == '__main__':
    main()
