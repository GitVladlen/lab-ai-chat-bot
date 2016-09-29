from Utils import *


class ConsoleViewChatBot(object):
    def __init__(self, model):
        self.model = model

        Notification.addObserver(self, "onAskQuestion")
        Notification.addObserver(self, "onPrint")
        pass

    def update(self, event, *args, **kwargs):
        if event == "onAskQuestion":
            self.ask(kwargs["question"])
            pass
        if event == "onPrint":
            self.print_msg(kwargs["msg"])
            pass
        pass

    def ask(self, question):
        print "[Question]:", question
        pass

    def print_msg(self, msg):
        print "[Message]:", msg
        pass

    pass
