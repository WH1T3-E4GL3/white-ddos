import socket as s
print('eg : python3 ipfinder.py')
print('And type url of any site without http or https eg:www.google.com')
try:
    host = input('Enter the url of the website : ')
    print(f'IP of {host} is {s.gethostbyname(host)}')
except Exception as e:
    print('Failed to resolve IP: ', e)

