from Utils import *
import json


class ModelChatBot(object):
    def __init__(self, dialogs_file_name):
        self.dialogs = []

        self.history = []

        self.user_name = "User"
        self.bot_name = "Bob"

        self.current_dialog = 0

        self.loadDialogs(dialogs_file_name)
        pass

    def loadDialogs(self, file_name):
        try:
            with open(file_name) as json_data:
                data = json.load(json_data)
                self.dialogs = data["dialogs"]
                pass
        except Exception as exception:
            Trace.log("Model", "loadDialogs {}: {}".format(type(exception), exception))
            return False
            pass

        return True
        pass

    def reset(self):
        self.history = []
        self.current_dialog = 0
        pass

    def doQuestion(self):
        dialog = self.currentDialog()
        if dialog is None:
            return None
            pass

        question = dialog.get("question")

        return question
        pass

    def doSuggestion(self, msg):
        dialog = self.currentDialog()
        if dialog is None:
            return None
            pass

        suggestion = dialog.get("suggestion")
        if suggestion is None:
            return None
            pass

        suggestion_true = dialog.get("suggestion_true")
        if msg in suggestion:
            return suggestion_true
            pass

        suggestion_false = dialog.get("suggestion_false")
        return suggestion_false
        pass

    def doPostQuestion(self):
        dialog = self.currentDialog()
        if dialog is None:
            return None
            pass

        post_question = dialog.get("post_question")

        return post_question
        pass

    def addToHistory(self, user, msg):
        block = (user, msg)
        self.history.append(block)
        pass

    def getHistory(self):
        return self.history
        pass

    def hasQuestion(self):
        if self.current_dialog < len(self.dialogs):
            return True
            pass

        return False
        pass

    def currentDialog(self):
        if self.hasQuestion() is False:
            return None
            pass

        question = self.dialogs[self.current_dialog]

        return question
        pass

    def nextQuestion(self):
        if self.hasQuestion() is False:
            return None
            pass

        self.current_dialog += 1
        pass

    pass
