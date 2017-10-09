# UDP server?
import socket



def Main():
    host = '127.0.0.1'
    port = 15000
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    # Asigno el host y el puerto al server
    
    print("Server started")

    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Message from " + str(addr) + ": ")
        print(data)

        data = data.upper()
        print("Sending: " + data)
        s.sendto(data.encode('utf-8'), addr)

    c.close()


if __name__ == '__main__':
    Main()
