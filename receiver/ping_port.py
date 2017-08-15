try:
    # For Python 3.0 and later
    from urllib.request import urlopen, URLError
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen, URLError


def ping(ip):
    try:
        urlopen("http://" + ip + ":1921/name").read()
        return True
    except URLError:
        return False
