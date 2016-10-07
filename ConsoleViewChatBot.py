#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Utils import *


class ConsoleViewChatBot(object):
    def __init__(self, model, controller):
        self.model = model
        self.controller = controller

        self.controller.setView(self)
        pass

    def syncWithModel(self):
        print "============================"
        for user, msg in self.model.getHistory():
            line = "{}: {}".format(user, msg)
            print line
            pass

        input = ""
        while len(input) == 0:
            try:
                input = raw_input(">")
            except Exception as exception:
                Trace.log("View", "syncWithModel {}: {}".format(type(exception), exception))
                pass
            pass

        self.controller.submit(input)
        pass

    pass
