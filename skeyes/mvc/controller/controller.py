class Controller:
    def __init__(self, model):
        self.model = model

    def run_model(self):
        self.model.run()
