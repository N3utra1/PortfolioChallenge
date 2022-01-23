#!/usr/bin/env
import pyfiglet
import socket

def banner():
    banner = pyfiglet.figlet_format("port scanner")
    print(banner)

def scan(maxPort):
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

    targetIP = socket.gethostbyname(socket.gethostname())

    try:
        for port in range(1,maxPort):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((targetIP,port))
            if result == 0:
                print("Port", port, "is open")
            s.close()
    except socket.error as e:
        print(e)
    except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            sys.exit()
    except socket.error:
            print("\ Server not responding !!!!")
            sys.exit()
banner()
scan(65535)
