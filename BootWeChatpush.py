import requests
import time
import socket
import random


def getIP():
    ipAPI = "http://ip.42.pl/raw"
    ip = requests.get(ipAPI)
    return ip.text


def getPcname():
    pcname = socket.gethostname()
    return pcname


def postServerChan(ip, pcname,URL):
    ran = random.randint(10, 99)
    dataout = str("主机名:{}设备公网ip地址:{}随机数{}".format(pcname, ip, ran))
    data = {
        "text": "主人您的{}已经开机了喵".format(pcname),
        "desp": dataout
    }
    requests.post("URL", data=data)

URL = ""#填你ServerChanURL
time.sleep(5)
postServerChan(getIP(), getPcname(),URL)
