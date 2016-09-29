from Tkinter import *


class TkinterViewChatBot(Frame):
    def __init__(self, model, controller, parent = None):
        Frame.__init__(self, parent)

        self.model = model
        self.controller = controller

        self.controller.setView(self)

        self.setupOjects()
        pass

    def setupOjects(self):
        ent_str = StringVar()

        group_chat = LabelFrame(self, text="All chat log", padx=5, pady=5)
        group_chat.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        scrollbar = Scrollbar(group_chat)
        text = Text(group_chat, wrap=WORD, yscrollcommand=scrollbar.set)

        group_msg = LabelFrame(self, text="Enter Message", padx=5, pady=5)
        group_msg.pack(side=TOP, fill=BOTH, padx=10, pady=10)

        btn = Button(group_msg, text="Submit")
        ent = Entry(group_msg, textvariable=ent_str)

        def onClick(event):
            if len(ent_str.get()) == 0:
                return
                pass

            text.config(state=NORMAL)
            msg = "- " + ent_str.get() + "\n"
            ent_str.set("")
            text.insert(END, msg)
            text.config(state=DISABLED)
            pass
        btn.bind("<Button-1>", onClick)
        btn.pack(side=BOTTOM, fill=BOTH)

        ent.pack(side=BOTTOM, fill=BOTH)

        text["state"] = DISABLED
        text.pack(side=LEFT, fill=BOTH)

        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=text.yview)
        pass

    pass
