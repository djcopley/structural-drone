import time
import socket
import skvideo.io
import skvideo.datasets

host = "0.0.0.0"
port = 5600
max_length = 65540

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))

sock.listen(10)
conn, addr = sock.accept()

while True:
    with open("outputfile.mp4", "rb") as ifile:
        sock.send(ifile.read(4096))

# writer = skvideo.io.FFmpegWriter("outputfile.mp4", outputdict={'-vcodec': 'libx264'})
#
# videogen = skvideo.io.vreader(skvideo.datasets.bigbuckbunny())
#
# for frame in videogen:
#     writer.writeFrame(frame)
