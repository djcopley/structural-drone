import threading


class View:
    def __init__(self, controller):
        self.controller = controller
        self.controller_thread = None

    def start(self):
        """
        Method begins execution of the program.

        :return: None
        """
        raise NotImplemented

    def start_controller(self):
        """
        Method starts controller in a new thread.

        :return:
        """
        self.controller_thread = threading.Thread(self.controller.start_model)
        self.controller_thread.start()

    def stop_controller(self):
        """
        Method stops controller thread.

        :return:
        """
        self.controller.stop_model()
        self.controller_thread.join()
