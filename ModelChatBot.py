from Utils import *


class ModelChatBot(object):
    def __init__(self):
        self.is_running = False
        self.db = [
            dict(
                Question="What is your name?",
                Suggestion=("Vladlen", "Bogdan", "Max"),
                SuggestionTrue="I know this name :)",
                SuggestionFalse="I dont know this name o_0",
                PostQuestion="Hi!"
            ),
        ]

        Notification.addObserver(self, "onStop")
        pass

    def hasQuestion(self):
        if len(self.db) > 0:
            return True
            pass

        return False
        pass

    def nextQuestion(self):
        if self.hasQuestion() is False:
            return None
            pass

        question = self.db.pop(self.db[0])

        return question
        pass

    def isRunning(self):
        return self.is_running
        pass

    def run(self):
        self.is_running = True

        Notification.notify("onStart")
        # Notification.notify("onStop")
        pass

    def update(self, event, *args, **kwargs):
        if event == "onStop":
            self.stop()
            pass
        pass

    def stop(self):
        self.is_running = False
        pass

    pass