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
            dict(
                Question="How are you?",
                Suggestion=("Fine", "Normal"),
                SuggestionTrue="That great :)",
                SuggestionFalse="Oh o_0",
            ),
            dict(
                Question="What is your favourite color?",
                PostQuestion="Oh, I really dont care)"
            ),
            dict(
                Question="Good bye!",
            ),
        ]

        self.history = []

        self.user_name = "User"
        self.bot_name = "Bob"

        self.current_question = 0
        pass

    def reset(self):
        self.history = []
        self.current_question = 0
        pass

    def doSuggestion(self, question_dict, msg):
        suggestion = question_dict.get("Suggestion")

        if suggestion is None:
            return None
            pass

        suggestion_true = question_dict.get("SuggestionTrue")

        if msg in suggestion:
            return suggestion_true
            pass

        suggestion_false = question_dict.get("SuggestionFalse")
        return suggestion_false
        pass

    def doPostQuestion(self, question_dict):
        post_question = question_dict.get("PostQuestion")

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
        if self.current_question < len(self.db):
            return True
            pass

        return False
        pass

    def currentQuestion(self):
        if self.hasQuestion() is False:
            return None
            pass

        question = self.db[self.current_question]

        return question
        pass

    def nextQuestion(self):
        if self.hasQuestion() is False:
            return None
            pass

        
        self.current_question += 1
        pass

    pass
