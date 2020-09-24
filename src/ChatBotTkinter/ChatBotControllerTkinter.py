#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Common.Utils import *


class ChatBotControllerTkinter(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view     
        pass

    def run(self):
        Notification.addObserver(self._submit, Events.onViewSubmit)
        Notification.addObserver(self._startChatting, Events.onViewStartChatting)

        self.view.show()
        pass

    def _submit(self, msg):
        self.model.addToHistory(self.model.user_name, msg)
        answer = self.model.analyze(msg)
        self.model.addToHistory(self.model.bot_name, answer)
        pass

    def _startChatting(self):
        self.model.reset()
        self.view.clearDialog()

        self.model.addToHistory(self.model.bot_name, "Давайте общаться!")
        pass
    pass
