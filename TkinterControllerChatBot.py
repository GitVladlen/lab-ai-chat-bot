class TkinterControllerChatBot(object):
    def __init__(self, model):
        self.model = model
        pass

    def setView(self, view):
        self.view = view
        pass

    def startChatting(self):
        question = self.mode.nextQuestion()
        if question is None:
            return
            pass

        self.history.append(question["Question"])

        self.view.syncWithModel()
        pass

    pass
