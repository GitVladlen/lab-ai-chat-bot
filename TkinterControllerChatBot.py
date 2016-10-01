class TkinterControllerChatBot(object):
    def __init__(self, model):
        self.model = model
        pass

    def setView(self, view):
        self.view = view
        pass

    def submit(self, msg):
        self.model.addToHistory(self.model.user_name, msg)

        question_block = self.model.currentQuestion()

        if question_block is None:
            return
            pass

        suggestion = self.model.doSuggestion(question_block, msg)

        if suggestion is not None:
            self.model.addToHistory(self.model.bot_name, suggestion)
            pass

        post_question = self.model.doPostQuestion(question_block)

        if post_question is not None:
            self.model.addToHistory(self.model.bot_name, post_question)
            pass

        self.model.nextQuestion()

        self.view.syncWithModel()

        question_block = self.model.currentQuestion()
        if question_block is None:
            return
            pass

        question = question_block.get("Question")

        if question is None:
            return
            pass

        self.model.addToHistory(self.model.bot_name, question)

        self.view.syncWithModel()
        pass

    def startChatting(self):
        self.model.reset()

        question_block = self.model.currentQuestion()
        if question_block is None:
            return
            pass

        msg = question_block.get("Question")

        if msg is None:
            return
            pass

        self.model.addToHistory(self.model.bot_name, msg)

        self.view.syncWithModel()
        pass

    pass
