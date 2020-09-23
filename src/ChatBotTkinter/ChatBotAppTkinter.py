#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Common.ChatBotModel import ChatBotModel
from src.ChatBotTkinter.ChatBotControllerTkinter import ChatBotControllerTkinter
from src.ChatBotTkinter.ChatBotViewTkinter import ChatBotViewTkinter

from src.Common.Utils import *


class ChatBotAppTkinter(object):
    def __init__(self):
        Events.addEvent("onViewSubmit")
        Events.addEvent("onViewStartChatting")
        Events.addEvent("onModelHistoryChanged")

        self.model = ChatBotModel("dialogs.json")
        self.view = ChatBotViewTkinter(self.model)

        self.controller = ChatBotControllerTkinter(self.model, self.view)
        pass

    def run(self):
        self.controller.run()
        pass
    pass