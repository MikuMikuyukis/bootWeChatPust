import requests
import time
import socket
import random
import datetime
import os
import sys

def currentTime():
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    currenttime = "{}月{}日{}时{}分{}秒".format(month, day, hour, minute, second)
    return currenttime


def getIP():
    ipAPI = "http://ip.42.pl/raw"
    ip = requests.get(ipAPI)
    return ip.text


def getPcname():
    pcname = socket.gethostname()
    return pcname


def postServerChan(ip, pcname, times,requestsURL):
    ran = random.randint(1, 9999)
    dataout = str("主机名:{},时间：{}设备公网ip地址:{}随机数{},".format(pcname, times, ip, ran))
    data = {
        "text": "主人您的{}已经开机了喵".format(pcname),
        "desp": dataout
    }
    requests.post(requestsURL, data=data)


def networktest(requestsURL):
    times = currentTime()
    while True:
        pingtest = os.system("ping www.baidu.com -n 1")
        if pingtest == 0:
            print("网络正常")
            postServerChan(getIP(), getPcname(), times,requestsURL)
            break

        else:
            print("网络错误正在重试")
            time.sleep(1)
def import_par():
    try:
        parameter = sys.argv[1]
        return parameter
    except IndexError:
        print("请传入ServerChanURL")
        exit()


if __name__ == "__main__":
    requestsURL = import_par()
    networktest(requestsURL)
