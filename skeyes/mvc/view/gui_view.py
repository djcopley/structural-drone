from skeyes.mvc.view.view import View


class GuiView(View):

    def __init__(self, controller):
        super().__init__(controller)

    def start(self):
        self.start_controller()
