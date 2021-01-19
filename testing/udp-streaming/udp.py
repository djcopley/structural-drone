import time
import socket
import skvideo.io
import skvideo.datasets

host = "0.0.0.0"
port = 5700
max_length = 65540

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

videogen = skvideo.io.vreader(skvideo.datasets.bigbuckbunny())

for frame in videogen:

    time.sleep(1)
