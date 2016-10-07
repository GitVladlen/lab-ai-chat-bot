#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TkinterControllerChatBot(object):
    def __init__(self, model):
        self.model = model
        self.view = None
        pass

    def setView(self, view):
        self.view = view
        pass

    def submit(self, msg):
        self.model.addToHistory(self.model.user_name, msg)

        self.view.syncWithModel()

        suggestion = self.model.doSuggestion(msg)
        if suggestion is not None:
            self.model.addToHistory(self.model.bot_name, suggestion)
            pass

        post_question = self.model.doPostQuestion()
        if post_question is not None:
            self.model.addToHistory(self.model.bot_name, post_question)
            pass

        self.model.nextQuestion()

        self.view.syncWithModel()

        question = self.model.doQuestion()
        if question is None:
            return
            pass

        self.model.addToHistory(self.model.bot_name, question)

        self.view.syncWithModel()
        pass

    def startChatting(self):
        self.model.reset()

        question = self.model.doQuestion()
        if question is None:
            return
            pass

        self.model.addToHistory(self.model.bot_name, question)

        self.view.syncWithModel()
        pass

    pass
