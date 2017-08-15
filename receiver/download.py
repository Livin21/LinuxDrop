from __future__ import print_function
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


def frm(ip):
    f_name = urlopen("http://" + ip + ":1921/name").read()
    print ("Loading " + f_name + " from planet " + ip + " ...")
    new_file = open(f_name, "wb")
    b_array = bytearray(urlopen("http://" + ip + ":1921/").read())
    new_file.write(b_array)
    print ("Mission Accomplished!")
    print (urlopen("http://" + ip + ":1921/end").read())

if __name__ == '__main__':
    frm("0.0.0.0")

