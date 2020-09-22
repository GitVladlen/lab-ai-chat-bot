#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Common.Utils import *


class ChatBotViewConsole(object):
    def __init__(self, model):
        self.model = model
        pass

    def show(self):
        Notification.addObserver(self._syncWithModel, Events.onModelHistoryChanged)
        pass

    def _syncWithModel(self, user, msg):
        if user == self.model.user_name:
            return

        line = "{}: {}".format(user, msg)
        print(line)
        pass

    def inputUserMessage(self):
        user_input = ""
        while len(user_input) == 0:
            try:
                user_input = input("> ")
            except Exception as exception:
                Trace.log("View", "inputUserMessage {}: {}".format(type(exception), exception))
                pass
            pass

        return user_input
    pass
