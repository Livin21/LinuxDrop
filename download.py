import urllib2


def frm(ip, port):
    f_name = urllib2.urlopen("http://" + ip + ":" + port + "/name").read()
    new_file = open(f_name, "wb")
    b_array = bytearray(urllib2.urlopen("http://" + ip + ":" + port + "/").read())
    new_file.write(b_array)

if __name__ == '__main__':
    frm("0.0.0.0", "1921")

