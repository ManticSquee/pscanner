import socket

target = input('Enter IP address: ')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Scanning for open ports...')

def pscan(port):
    try:
        s.connect((target,port))
        return True
    except:
        return False

for x in range(20,30):
    if pscan(x):
        print('Port', x, 'is open')
