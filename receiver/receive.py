import urllib2

import download
import get_active_ips as ips


def download_from(ip):
    print("")
    print ("Connecting to planet " + ip + " ...")
    try:
        download.frm(ip)
    except urllib2.HTTPError:
        print ("Mission Failed! File Not Found! Teleport to a different planet and try again")


def receive():
    print ("Launching scanner...")
    print ("Scanning nearby planets...")
    active_ips = ips.get()
    try:
        download_from(active_ips[0])
    except IndexError:
        print ("")
        print ("No planets have launched the file")
    except Exception:
        print ("")
        print ("Install nmap, Sloth!\n\n\'sudo apt install nmap\' will do it for ya!")



