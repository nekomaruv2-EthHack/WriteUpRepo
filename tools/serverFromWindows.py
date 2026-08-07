# This python code is useful to start python server.
# often time I struggle to send some files my parrot from windows server.
# change "loot.zip" to arbitary file name.
# 
import http.server

class UploadHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers["Content-Length"])
        file_data = self.rfile.read(length)
        with open("loot.zip", "wb") as f:
            f.write(file_data)
        self.send_response(200)
        self.end_headers()

http.server.HTTPServer(("0.0.0.0", 8001), UploadHandler).serve_forever()
