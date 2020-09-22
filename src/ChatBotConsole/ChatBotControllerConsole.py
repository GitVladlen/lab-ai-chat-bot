#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Common.Utils import *


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

        question = self.model.doQuestion()
        if question is None:
            return
            pass

        self.model.addToHistory(self.model.bot_name, question)

        user_input = self.view.inputUserMessage()

        while user_input != "exit":
            self._submit(user_input)

            user_input = self.view.inputUserMessage()
            pass
        pass

    def _submit(self, msg):
        self.model.addToHistory(self.model.user_name, msg)

        suggestion = self.model.doSuggestion(msg)
        if suggestion is not None:
            self.model.addToHistory(self.model.bot_name, suggestion)
            pass

        post_question = self.model.doPostQuestion()
        if post_question is not None:
            self.model.addToHistory(self.model.bot_name, post_question)
            pass

        self.model.nextQuestion()

        question = self.model.doQuestion()
        if question is None:
            return
            pass

        self.model.addToHistory(self.model.bot_name, question)
        pass
    pass
