# This is netStatus_ping.py
# check network status by ping
import os
import argparse
import platform

from urllib.request import urlopen


class ping:
    def __init__(self, url=["https://www.baidu.com",
                            "https://www.google.com",
                            "https://www.bilibili.com",
                            "https://www.kickstarter.com",
                            "https://github.com"],
                 dns=["1.1.1.1", "8.8.8.8", "1.0.0.1", "119.29.29.29", "223.5.5.5"]):
        self.url = url
        self.dns = dns
        self.command = None
        self.flag = False

    def exec_arg(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-u", "--url",
                            help="url for checking network status",
                            type=str, nargs="+", required=False)
        parser.add_argument("-d", "--dns",
                            help="dns for checking network status",
                            type=str, nargs="+", required=False)
        parser.add_argument("-c", "--command",
                            help="execute command after this action",
                            type=str, nargs="?", required=False)
        parser.add_argument("-f", "--flag",
                            help="execute command under certain circumstances(net False or True)",
                            type=bool, nargs="?", required=False)

        args = parser.parse_args()
        if args.url != None:
            self.url = args.url
        if args.dns != None:
            self.dns = args.dns
        if args.command != None:
            self.command = args.command
        if args.flag != None:
            self.flag = args.flag

    def __call__(self, url=["www.baidu.com"], dns=["1.1.1.1"]):
        self.url = url
        self.dns = dns

    def check_url(self, url=None):
        if url == None:
            url = self.url
        count = 0
        size = len(url)
        for u in url:
            try:
                urlopen(u, timeout=5)
                count += 1
            except:
                count += 0
        # connection larger than 60%
        if count/size >= 0.6:
            return True

        return False

    def check_dns(self, dns=None):
        if dns == None:
            dns = self.dns
        count = 0
        size = len(dns)
        for d in dns:
            if platform.system().lower() == "windows".lower():
                status = os.system("ping -n 3 "+d)
            else:
                status = os.system("ping -c 3 "+d)

            if status == 0:
                count += 1
        # connection larger than 60%
        if count/size >= 0.6:
            return True
        return False

    def check(self, url=None, dns=None):
        if self.check_url(url) == False:
            return False
        if self.check_dns(dns) == False:
            return False
        return True

    def exec_main(self):
        self.exec_arg()
        if self.check() == self.flag:
            os.system(self.command)

    ################## HELP ###################

    def print_false(self):
        print("Unknown false")

    def print_more_help(self):
        print("net_status.py \'-h\' | \'--help\' for more helps")

    def usage(self):
        print("net_status.py [-i <inputfolder>] [option]")
        print("or")
        self.print_more_help()
        sys.exit(0)


if __name__ == "__main__":
    net = ping()
    net.exec_main()
