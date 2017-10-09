# UDP client?
import socket

def Main():
    host = '127.0.0.1'
    port = 15001 # Debe ser diferente del port del server

    server = ('127.0.0.1', 15000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Creo el socket para UDP
    s.bind((host, port))
    # Asigno host y puerto al cliente

    message = input("-> ")
    while message != 'q':
        s.sendto(message.encode('utf-8'), server)
        # Como no hay conexion establecida, tengo
        # que decirle que se lo envie al server
        data, addr = s.recvfrom(1024)
        # El socket solo espera a recibi

        data = data.decode('utf-8')
        print("Received from server: " + data)

        message = input("-> ")

    s.close()

if __name__ == '__main__':
    Main()
