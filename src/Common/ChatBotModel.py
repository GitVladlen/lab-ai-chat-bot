#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import random

from src.Common.Utils import *


class ChatBotModel(object):
    def __init__(self, data_file_name):
        self.reflections = None
        self.psychobabble = None

        self.history = []

        self.user_name = u"You"
        self.bot_name = u"Bot"

        self.loadData(data_file_name)
        pass

    def loadData(self, file_name):
        try:
            with open(file_name, encoding="utf-8") as json_data:
                data = json.load(json_data)
                self.reflections = data["reflections"]
                self.psychobabble = data["psychobabble"]
                pass
        except Exception as exception:
            Trace.log("Model", "loadDialogs {}: {}".format(type(exception), exception))
            return False
            pass

        return True
        pass

    def reflect(self, fragment):
        tokens = fragment.lower().split()
        for i, token in enumerate(tokens):
            if token in self.reflections:
                tokens[i] = self.reflections[token]
        return ' '.join(tokens)

    def analyze(self, statement):
        for pattern, responses in self.psychobabble:
            match = re.match(pattern, statement.rstrip(".!"))
            if match:
                response = random.choice(responses)
                return response.format(*[self.reflect(g) for g in match.groups()])

    def reset(self):
        self.history = []
        self.current_dialog = 0
        pass

    def addToHistory(self, user, msg):
        block = (user, msg)
        self.history.append(block)
        Notification.notify(Events.onModelHistoryChanged, user, msg)
        pass

    def getHistory(self):
        return self.history
        pass

    def getMessageCount(self):
        return len(self.history)
        pass

    pass

