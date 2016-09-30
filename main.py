PARAM_TKINTER = True
from ModelChatBot import ModelChatBot

if PARAM_TKINTER is True:
    from Tkinter import *
    from TkinterViewChatBot import TkinterViewChatBot
    from TkinterControllerChatBot import TkinterControllerChatBot
    pass
else:
    from ConsoleControllerChatBot import ConsoleControllerChatBot
    from ConsoleViewChatBot import ConsoleViewChatBot
    pass

def main_console():
    model = ModelChatBot()
    controller = ConsoleControllerChatBot(model)
    view = ConsoleViewChatBot(model)

    model.run()
    pass

def main_tkinter():
    model = ModelChatBot()
    controller = TkinterControllerChatBot(model)

    root = Tk()

    view = TkinterViewChatBot(model, controller, root)

    view.pack(fill=BOTH, expand=True)
    root.mainloop()
    pass


if __name__ == "__main__":
    if PARAM_TKINTER is True:
        main_tkinter()
        pass
    else:
        main_console()
        pass
    pass
