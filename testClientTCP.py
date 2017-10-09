# Client?
import socket

def Main():
    host = '127.0.0.1'
    port = 15001
    # host es a quién me quiero conectar
    # port es a qué puerto quiero llegar


    s = socket.socket()
    s.connect((host, port))
    # Le digo al socket que se conecte a host, por
    # el puerto port

    prompt = input("-> ")
    while prompt != 'q':
        s.send(prompt.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print("Received from server: " + data)
        prompt = input("-> ")

    s.close()

if __name__ == '__main__':
    Main()
