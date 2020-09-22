#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.Common.ChatBotModel import ChatBotModel
from src.ChatBotConsole.ChatBotControllerConsole import ChatBotControllerConsole
from src.ChatBotConsole.ChatBotViewConsole import ChatBotViewConsole

from src.Common.Utils import *

class ChatBotAppConsole(object):
    def __init__(self):
        Events.addEvent("onModelHistoryChanged");

        self.model = ChatBotModel("dialogs.json")
        self.view = ChatBotViewConsole(self.model)

        self.controller = ChatBotControllerConsole(self.model, self.view)

        self.controller.run()
        
        pass
    pass