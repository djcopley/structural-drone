class Controller:
    def __init__(self, model):
        self.model = model

    def start_model(self):
        self.model.start()

    def stop_model(self):
        self.model.running = False
