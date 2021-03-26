# import gstreamer


class Streamer:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port


if __name__ == '__main__':
    streamer = Streamer("localhost", 5600)
