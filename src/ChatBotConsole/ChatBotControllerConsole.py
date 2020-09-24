#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ChatBotControllerConsole(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        pass

    def run(self):
        self.view.show()
        self._startChatting()
        pass

    def _startChatting(self):
        self.model.reset()

        self.model.addToHistory(self.model.bot_name, "Hello. How are you feeling today?")

        while True:
            user_input = self.view.inputUserMessage()
            self._submit(user_input)
            if user_input == "exit":
                break
            pass
        pass

    def _submit(self, msg):
        self.model.addToHistory(self.model.user_name, msg)
        answer = self.model.analyze(msg)
        self.model.addToHistory(self.model.bot_name, answer)
        pass
    pass
