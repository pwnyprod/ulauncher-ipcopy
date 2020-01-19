from requests import get
import socket


def get_external_ip():
    """
    :return String
    """
    ip = get('https://api.ipify.org').text
    if ip != "":
        return ip
    return 'No network connection'


def get_local_ip():
    """
    :return: String
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
