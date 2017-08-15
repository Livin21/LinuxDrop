from receiver import download, get_active_ips as ips
try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import HTTPError


def download_from(ip):
    print("")
    print ("Connecting to planet " + ip + "...")
    try:
        download.frm(ip)
    except HTTPError:
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



