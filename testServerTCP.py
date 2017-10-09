# Server?
import socket

# utf-8: encode y decode hacen lo suyo para que el
# mensaje que se envie o se reciba este en el mismo
# idioma


def Main():
    host = '127.0.0.1'
    port = 15001
    # host es dónde voy a escuchar
    # port es el puerto en el que voy a escuchar


    s = socket.socket()
    # Creo el objeto socket
    s.bind((host, port))
    # bind asigna el host y el puerto al servidor 
    s.listen(1)
    # Escucha una sola conexion en el (host, port)

    c, addr = s.accept()
    # Cuando haya un syn, aceptalo
    # accept devuelve una conexion y una direccion
    # (la del cliente). La conexion es lo que voy a
    # usar para recibir y enviar mensajes
    print("Connection from: " + str(addr))

    while True:
        data = c.recv(1024).decode('utf-8')
        # Espera a recibir 1024 bytes
        if not data:
            break
        print("From user: " + data)
        data = data.upper()
        print("Sending: " + data)
        c.send(data.encode('utf-8'))
        # Envia el mensaje recibido en mayusculas

    c.close()





if __name__ == '__main__':
    Main()
