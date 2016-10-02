from ModelChatBot import ModelChatBot


PARAM_TKINTER = True

if PARAM_TKINTER is True:
    from Tkinter import *
    from ttk import *
    from TkinterViewChatBot import TkinterViewChatBot
    from TkinterControllerChatBot import TkinterControllerChatBot

    def main():
        model = ModelChatBot("dialogs.json")
        controller = TkinterControllerChatBot(model)

        root = Tk()

        view = TkinterViewChatBot(model, controller, root)

        view.pack(fill=BOTH, expand=True)
        root.mainloop()
        pass
    pass
else:
    from ConsoleControllerChatBot import ConsoleControllerChatBot
    from ConsoleViewChatBot import ConsoleViewChatBot

    def main():
        model = ModelChatBot("dialogs.json")
        controller = ConsoleControllerChatBot(model)
        view = ConsoleViewChatBot(model)
        pass
    pass

if __name__ == "__main__":
    main()
    pass
