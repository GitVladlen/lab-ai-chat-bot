from Tkinter import *


class TkinterViewChatBot(Frame):
    def __init__(self, model, controller, root):
        Frame.__init__(self, root)

        self.model = model
        self.controller = controller

        self.controller.setView(self)

        self.setupOjects()

        self.setupRoot(root)
        pass

    def setupRoot(self, root):
        root.title("Chat")

        menubar = Menu(root)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Start chatting", command=self.controller.startChatting)

        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)
        pass

    def setupOjects(self):
        ent_str = StringVar()

        group_chat = LabelFrame(self, text="All chat log", padx=5, pady=5)
        group_chat.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

        scrollbar = Scrollbar(group_chat)
        text = Text(group_chat, width=40, height=15, wrap=WORD, yscrollcommand=scrollbar.set)

        group_msg = LabelFrame(self, text="Enter Message")
        group_msg.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)

        btn = Button(group_msg, text="Submit")
        ent = Entry(group_msg, textvariable=ent_str)

        ent.pack(side=TOP, fill=X, padx=5, pady=5)

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
        btn.pack(side=TOP, fill=X, padx=5, pady=5)

        text["state"] = DISABLED
        text.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=text.yview)
        pass

    def syncWithModel(self):

        pass

    pass
