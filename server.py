import socket

sock = socket.socket()

sock.bind(('', 9090))  # Назначаем хост и сокет
print('Запуск севера')
sock.listen(1)  # Слушаем сервер
print('Начало прослушивания порта')
conn, addr = sock.accept()  # принимаем новый сокет и адресс клиента
print('Подключение клиента')

while True:
    data = conn.recv(1024)
    if not data:
        print('Приём данных от клиента')
        break
    print('Отправка данных клиенту')
    conn.send(data)
    print('Отключение клиента')

print('Остановка сервера')
conn.close()
