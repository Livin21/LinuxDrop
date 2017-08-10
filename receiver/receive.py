import urllib2

import download
import get_active_ips as ips


def download_from(ip):
    print("")
    print ("Connecting to " + ip + " ...")
    try:
        download.frm(ip)
    except urllib2.HTTPError:
        print ("Download Failed! File Not Found!")

if __name__ == '__main__':
    print ("Finding LinuxDrop instances in the network...")
    active_ips = ips.get()
    try:
        download_from(active_ips[0])
    except IndexError:
        print ("No LinuxDrop instances running in this network!")



