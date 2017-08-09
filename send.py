import SimpleHTTPServer
import SocketServer

PORT = 1921

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("0.0.0.0", PORT), Handler)

print "serving at localhost:", PORT
httpd.serve_forever()
