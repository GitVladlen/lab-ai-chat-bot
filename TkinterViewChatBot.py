#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from ttk import *


class TkinterViewChatBot(Frame):
    def __init__(self, model, controller, root):
        Frame.__init__(self, root)

        # self.style = Style()
        # self.style.theme_use("clam")

        self.model = model
        self.controller = controller

        self.controller.setView(self)

        self.entry_str_var = None
        self.text = None

        self.setupOjects()

        self.setupRoot(root)  # hack for setup window title & menubar
        pass

    def setupRoot(self, root):
        root.title("Симулятор переписки")

        def onReturn(event):
            self.onSumbit()
            pass
        root.bind("<Return>", onReturn)
        pass

    def onSumbit(self):
        value = self.entry_str_var.get()

        if len(value) == 0:
            return
            pass

        self.controller.submit(value)

        self.entry_str_var.set("")
        pass

    def setupOjects(self):
        self.entry_str_var = StringVar()

        btn_start = Button(self, text=u"Найти собеседника")

        def onBtnStartClick(event):
            self.controller.startChatting()
            self.ent.config(state=NORMAL)
            pass
        btn_start.bind("<Button-1>", onBtnStartClick)
        btn_start.pack(side=TOP, fill=BOTH, padx=5, pady=5)

        group_chat = LabelFrame(self, text=u"Переписка:")
        group_chat.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

        scrollbar = Scrollbar(group_chat)
        self.text = Text(group_chat, width=40, height=15, wrap=WORD, yscrollcommand=scrollbar.set)

        group_msg = LabelFrame(self, text=u"Новое сообщение:")
        group_msg.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)

        btn = Button(group_msg, text=u"Отправить")

        self.ent = Entry(group_msg, textvariable=self.entry_str_var, state=DISABLED)
        self.ent.pack(side=TOP, fill=X, padx=5, pady=5)

        def onClick(event):
            self.onSumbit()
            pass
        btn.bind("<Button-1>", onClick)
        btn.pack(side=TOP, fill=X, padx=5, pady=5)

        self.text["state"] = DISABLED
        self.text.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.text.yview)
        pass

    def syncWithModel(self):
        self.text.config(state=NORMAL)

        self.text.delete('1.0', END)

        for user, msg in self.model.getHistory():
            line = u"{}: {}\n".format(user, msg)
            self.text.insert(END, line)
            pass

        self.text.config(state=DISABLED)

        self.text.see(END)
        pass

    pass
