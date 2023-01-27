try:
    import usocket as _socket
except:
    import _socket
try:
    import ussl as ssl
except:
    import ssl

import lib.config as config
import socket

def http(url,port):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, port)[0][-1]
    s = socket.socket()
    s.settimeout(3.0)
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()


def post(url,port,path,headers,dat):
    addr = socket.getaddrinfo(url, port)[0][-1]
    print("Address Info: ",addr)
    s = socket.socket()
    s.settimeout(3.0)
    s.connect(addr)
    s.send(bytes('POST /%s HTTP/1.0\r\nHost: %s\n%s\nContent-length: %s\r\n\r\n%s' % (path, url, headers,len(dat),dat), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()

def https(url,port,method,dat,use_stream=True):
    s = _socket.socket()

    ai = _socket.getaddrinfo(url, port)
    print("Address infos:", ai)
    addr = ai[0][-1]

    print("Connect address:", addr)
    s.connect(addr)

    s = ssl.wrap_socket(s)

    if use_stream:
        # Both CPython and MicroPython SSLSocket objects support read() and
        # write() methods.
        s.write(b"GET / HTTP/1.0\nHost: "+url+"\r\n\r\n")
        print(s.read(4096))
    else:
        # MicroPython SSLSocket objects implement only stream interface, not
        # socket interface
        s.send(b"GET / HTTP/1.0\nHost: "+url+"\r\n\r\n")
        print(s.recv(4096))

    s.close()

def post_tls(url,port,path,method,headers,dat,use_stream=True):
    s = _socket.socket()

    ai = _socket.getaddrinfo(url, port)
    print("Address infos:", ai)
    addr = ai[0][-1]

    print("Connect address:", addr)
    s.connect(addr)

    s = ssl.wrap_socket(s)
    #print(s)

    if use_stream:
        # Both CPython and MicroPython SSLSocket objects support read() and
        # write() methods.
        s.write(bytes('%s /%s HTTP/1.0\r\nHost: %s\nContent-length: %s\n%s\r\n\r\n%s' % (method, path, url,len(dat),headers,dat), 'utf8'))

        print(s.read(4096))

    s.close()


def elastic_push(index,dat,use_stream=True):
    s = _socket.socket()

    ai = _socket.getaddrinfo(config.elasticserver, config.serverport)
    print("Address infos:", ai)
    addr = ai[0][-1]

    print("Connect address:", addr)
    s.connect(addr)

    s = ssl.wrap_socket(s)
    #print(s)

    if use_stream:
        s.write(bytes('PUT /%s HTTP/1.0\r\nHost: %s\nAuthorization: Basic %s\nContent-type: application/json\r\n\r\n%s' % (index, config.elasticserver, config.elastic,dat), 'utf8'))
        print(s.read(4096))

    s.close()

def elastic_get(index, query):

    s = _socket.socket()

    ai = _socket.getaddrinfo(url, port)
    print("Address infos:", ai)
    addr = ai[0][-1]

    print("Connect address:", addr)
    s.connect(addr)

    s = ssl.wrap_socket(s)
    print(s)


    use_stream = True

    if use_stream:
        # Both CPython and MicroPython SSLSocket objects support read() and
        # write() methods.
        s.write(b"GET / HTTP/1.0\nAuthorization: Basic "+config.elastic+"\r\n\r\n")
        s.write(bytes('%s /%s HTTP/1.0\r\nHost: %s\nAuthorization: Basic %s\nContent-length: %s\n%s\r\n\r\n%s' % ("GET", index, config.elasticserver, config.elastic,len(dat),"Content-type: application/json",dat), 'utf8'))

    print(s.read(4096))

    s.close()

#main()
