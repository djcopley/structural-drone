from skeyes.view.view import View


class CliView(View):
    def __init__(self, controller):
        super().__init__(controller)

    def run(self):
        self.start_controller()
