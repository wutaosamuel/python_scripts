# This is netStatus_ping.py
# check network status by ping
import os
#import asyncio # support multiple thread or io in the future 
import platform

from urllib.request import urlopen


class ping:
    def __init__(self, url=["https://www.baidu.com", "https://www.google.com"],
                 dns=["1.1.1.1", "8.8.8.8"]):
        self.url = url
        self.dns = dns

    def __call__(self, url=["www.baidu.com"], dns=["1.1.1.1"]):
        self.url = url
        self.dns = dns

    def check_url(self, url=None):
        if url == None:
            url = self.url
        for u in url:
            try:
                urlopen(u, timeout=2)
            except:
                return False
        return True

    def check_dns(self, dns=None):
        if dns == None:
            dns = self.dns
        for d in dns:
            if platform.system().lower() == "windows".lower():
                status = os.system("ping -n 2 "+d)
            elif platform.system().lower() == "linux".lower():
                status = os.system("ping -c 2 "+d)
            else:
                self.print_false()
            if status == 1:
                return False
        return True

    def check(self, url=None, dns=None):
        if self.check_url(url) == False:
            return False
        if self.check_dns(dns) == False:
            return False
        return True

    def print_false(self):
        print("Unknow false")


if __name__ == "__main__":
    net = ping()
    if platform.system().lower() == "linux".lower():
        if net.check() == False:
            os.system("systemctl restart systemd-networkd")
    else:
        print("Only support for linux")
