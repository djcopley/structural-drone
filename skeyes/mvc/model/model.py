from skeyes.mvc.model.action import Action
from skeyes.mvc.model.video import Video


class Model:
    def __init__(self, video_device_handle, gst_ip_address, gst_port):
        self.running = True

        # TODO make getters and setters for the following parameters that way the controller can update objects easily
        # Configuration options
        # ----------------------
        # Webcam opencv device handle - ie: 0, 1, 2, 3
        self.video_device_handle = video_device_handle
        # Gstreamer udp stream ip (this is the destination ip)
        self.gst_ip_address = gst_ip_address
        # Gstreamer port
        self.gst_port = gst_port

    def start(self):
        while self.running:
            # Get video frame
            pass
