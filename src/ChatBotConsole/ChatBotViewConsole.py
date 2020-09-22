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

        line = u"{}: {}".format(user, msg)
        print(line)
        pass

    def inputUserMessage(self):
        user_input = ""
        while len(user_input) == 0:
            try:
                user_input = raw_input("> ")
            except Exception as exception:
                Trace.log("View", "inputUserMessage {}: {}".format(type(exception), exception))
                pass
            pass
            
        if type(user_input) != str:
            return "exit"

        return user_input
    pass
