from __future__ import print_function

import re
import subprocess
import netifaces as ni

import ping_port


def find_correct_ips(ip_array):
    c_ips = []
    for j in ip_array:
        if ping_port.ping(j):
            c_ips.append(j)
    return c_ips


def get():
    print ("Fetching list of devices...")
    this_device_ip = ni.ifaddresses('wlo1')[ni.AF_INET][0]['addr']
    p2 = subprocess.Popen(["nmap", "-sP", this_device_ip + "/24"], stdout=subprocess.PIPE)
    res = p2.communicate()
    arr = ''.join(map(str, res)).replace("\n", " ").replace("(", "").replace(")", "").split(" ")
    ip_arr = []
    print ("Almost there")
    for i in arr:
        print (".", end="")
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", i):
            ip_arr.append(i)

    correct_ips = find_correct_ips(ip_arr)
    return correct_ips
