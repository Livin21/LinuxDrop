import sys

from sender import send
from receiver import receive

def run():
    try:
        option = sys.argv[1]
        if option == "-send":
            f_name = sys.argv[2]
            send.start_server(f_name)
        elif option == "-receive":
            receive.receive()
        else:
            print ("Usage:\n\n\t\tlidrop -send file\n\t\tlidrop -receive")
    except IndexError:
        print ("Usage:\n\n\t\tlidrop -send file\n\t\tlidrop -receive")


if __name__ == "__main__":
    run()
