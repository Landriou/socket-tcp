import socket

socket_sv=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('192.168.1.51',3000)
socket_sv.bind(address)

#Asignamos la cantidad de clientes que el socket puede atender
socket_sv.listen(1)

print("Esperando conexiones")
#Llamada bloqueante

(socket_cliente,address_client) = socket_sv.accept()
print("Connected: ")
print(address_client)

#Mantenemos al socket aceptando conexiones
while True:
    message = socket_cliente.recv(100).decode("utf-8")
    print("client:")
    print(message)
    if(message == 'exit'):
        break

socket_sv.close()