import urllib2


def ping(ip):
    try:
        urllib2.urlopen("http://" + ip + ":1921/name").read()
        return True
    except urllib2.URLError:
        return False
