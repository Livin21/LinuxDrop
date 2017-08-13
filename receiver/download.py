from __future__ import print_function
import urllib2


def frm(ip):
    f_name = urllib2.urlopen("http://" + ip + ":1921/name").read()
    print ("Downloading " + f_name + " from " + ip + " ...")
    new_file = open(f_name, "wb")
    b_array = bytearray(urllib2.urlopen("http://" + ip + ":1921/").read())
    new_file.write(b_array)
    print ("Download Complete")
    print (urllib2.urlopen("http://" + ip + ":1921/end").read())

if __name__ == '__main__':
    frm("0.0.0.0")

