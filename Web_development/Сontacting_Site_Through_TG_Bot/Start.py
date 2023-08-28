from http.server import HTTPServer, CGIHTTPRequestHandler
import os
server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
#os.startfile("Start_bot.py")
httpd.serve_forever()