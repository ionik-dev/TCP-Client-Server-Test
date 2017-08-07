import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)

    c, addr = s.accept()
    print("Connection from: {}".format(str(addr)))

    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        data = str(data)
        print("got from connected user: {}".format(data))
        data = data.upper()
        print("sending {}".format(data))
        c.send(data.encode())

    c.close()

if __name__ == '__main__':
    Main()