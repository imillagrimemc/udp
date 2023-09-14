import socket

# Задайте адрес сервера и порт
server_address = ('0.0.0.0', 12345)  # 0.0.0.0 означает, что сервер будет слушать на всех доступных интерфейсах

# Создайте сокет для UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Привяжите сокет к заданному адресу и порту
udp_socket.bind(server_address)

print(f"Сервер слушает на {server_address}")

while True:
    try:
        # Принимайте данные от клиентов
        data, client_address = udp_socket.recvfrom(1024)  # 1024 - максимальный размер буфера

        # Обработайте полученные данные (здесь просто выводим их на экран)
        print(f"Получено от {client_address}: {data.decode('utf-8')}")

        # Ответ на запрос (если нужно)
        # udp_socket.sendto(b"Сообщение от сервера", client_address)
    except KeyboardInterrupt:
        # Обработка остановки сервера по нажатию Ctrl+C
        print("Сервер остановлен.")
        break
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Закройте сокет после завершения работы
udp_socket.close()
