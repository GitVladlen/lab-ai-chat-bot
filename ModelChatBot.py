from Utils import *


class ModelChatBot(object):
    def __init__(self):
        self.db = [
            dict(
                Question="What is your name?",
                Suggestion=("Vladlen", "Bogdan", "Max"),
                SuggestionTrue="I know this name :)",
                SuggestionFalse="I dont know this name o_0",
                PostQuestion="Hi!"
            ),
        ]

        self.history = []
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

    pass
