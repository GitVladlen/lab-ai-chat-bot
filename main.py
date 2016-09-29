PARAM_TKINTER = True

from ModelChatBot import ModelChatBot

if PARAM_TKINTER is True:
    from TkinterViewChatBot import TkinterViewChatBot
    from TkinterControllerChatBot import TkinterControllerChatBot
    pass
else:
    from ConsoleControllerChatBot import ConsoleControllerChatBot
    from ConsolerViewChatBot import ConsolerViewChatBot
    pass

def main_console():
    model = ModelChatBot()
    controller = ConsoleControllerChatBot(model)
    view = ConsolerViewChatBot(model)

    model.run()
    pass

def main_tkinter():
    model = ModelChatBot()
    controller = TkinterControllerChatBot(model)
    view = TkinterViewChatBot(model, controller)

    view.pack()

    view.mainloop()
    pass


if __name__ == "__main__":
    if PARAM_TKINTER is True:
        main_tkinter()
        pass
    else:
        main_console()
        pass
    pass
