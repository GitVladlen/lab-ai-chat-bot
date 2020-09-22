#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.ttk import *

from src.Common.Utils import *

# view interface
# - show
# - hide

class ChatBotViewTkinter(object):
    def __init__(self, model):
        self.model = model

        self.entry_str_var = None
        self.text = None

        self.root = Tk()
        
        self._setupOjects()
        self._setupRoot()
        pass

    def show(self):
        Notification.addObserver(self._syncWithModel, Events.onModelHistoryChanged)

        self.root.mainloop()
        pass

    def _syncWithModel(self, user, msg):
        self.text.config(state=NORMAL)

        line = u"{}: {}\n".format(user, msg)
        self.text.insert(END, line)

        self.text.config(state=DISABLED)

        self.text.see(END)
        pass

    def _setupRoot(self):
        self.root.title("Симулятор переписки")

        def onReturn(event):
            self._onSumbit()
            pass

        self.root.bind("<Return>", onReturn)
        pass

    def _onSumbit(self):
        value = self.entry_str_var.get()

        if len(value) == 0:
            return
            pass

        # self.controller.submit(value)

        Notification.notify(Events.onViewSubmit, value);

        self.entry_str_var.set("")
        pass

    def _setupOjects(self):
        frame = Frame(self.root)

        self.entry_str_var = StringVar()

        btn_start = Button(self.root, text=u"Найти собеседника")

        def onBtnStartClick(event):
            # self.controller.startChatting()

            Notification.notify(Events.onViewStartChatting);
            
            self.ent.config(state=NORMAL)
            pass

        btn_start.bind("<Button-1>", onBtnStartClick)
        btn_start.pack(side=TOP, fill=BOTH, padx=5, pady=5)

        group_chat = LabelFrame(self.root, text=u"Переписка:")
        group_chat.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

        scrollbar = Scrollbar(group_chat)
        self.text = Text(group_chat, width=40, height=15, wrap=WORD, yscrollcommand=scrollbar.set)

        group_msg = LabelFrame(self.root, text=u"Новое сообщение:")
        group_msg.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)

        btn = Button(group_msg, text=u"Отправить")

        self.ent = Entry(group_msg, textvariable=self.entry_str_var, state=DISABLED)
        self.ent.pack(side=TOP, fill=X, padx=5, pady=5)

        def onClick(event):
            self._onSumbit()
            pass

        btn.bind("<Button-1>", onClick)
        btn.pack(side=TOP, fill=X, padx=5, pady=5)

        self.text["state"] = DISABLED
        self.text.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.text.yview)        

        frame.pack(fill=BOTH, expand=True)
        
        pass
    pass