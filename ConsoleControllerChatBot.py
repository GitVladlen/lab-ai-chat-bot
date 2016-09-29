from Utils import *


class ConsoleControllerChatBot(object):
    def __init__(self, model):
        self.model = model

        Notification.addObserver(self, "onStart")
        pass

    def update(self, event, *args, **kwargs):
        if event == "onStart":
            self.ask_name()
            pass
        pass

    def ask_name(self):
        question = "What is your name?"
        Notification.notify("onAskQuestion", question=question)

        answer = self.get_input()

        msg = "Hi {name}!".format(name=answer)
        Notification.notify("onPrint", msg=msg)
        pass

    def get_input(self):
        user_input = raw_input(">")

        return user_input
        pass

    pass
