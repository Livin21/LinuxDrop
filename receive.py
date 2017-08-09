from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
import logging
import multiprocessing

from scapy.layers.inet import IP, TCP, ICMP

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

ip = "192.168.43.255"
closed = 0


def scan(port):
    closed = 0
    global openp
    src_port = RandShort()
    p = IP(dst=ip) / TCP(sport=src_port, dport=port, flags='S')
    resp = sr1(p, timeout=2)
    if str(type(resp)) == "<type 'NoneType'>":
        closed += 1
    elif resp.haslayer(TCP):
        if resp.getlayer(TCP).flags == 0x12:
            send_rst = sr(IP(dst=ip) / TCP(sport=src_port, dport=port, flags='AR'), timeout=1)
            print("[*] %d open" % port)
        elif resp.getlayer(TCP).flags == 0x14:
            closed += 1
    return closed


def is_up(ip):
    p = IP(dst=ip) / ICMP()
    resp = sr1(p, timeout=10)
    if resp is None:
        return False
    elif resp.haslayer(ICMP):
        return True


if __name__ == '__main__':
    conf.verb = 0
    start_time = time.time()
    ports = range(1, 1024)
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count() * 10)
    if is_up(ip):
        print("Host %s is up, start scanning" % ip)
        results = [pool.apply_async(scan, (port,)) for port in ports]
        for result in filter(lambda i: i.get() != None, results):
            closed += result.get()[0]
        duration = time.time() - start_time
        print("%s Scan Completed in %fs" % (ip, duration))
        print("%d closed ports in %d total port scanned" % (closed, len(ports)))
    else:
        print("Host %s is Down" % ip)
