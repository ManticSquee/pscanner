import socket

target = input('Enter IP address: ')

try:
    for x in range(900,915):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((target,x))

        if result == 0:
            print('Port', x , 'is open')

except:
    print('Invalid IP')