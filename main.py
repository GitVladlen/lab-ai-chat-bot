#!/usr/bin/env python
# -*- coding: utf-8 -*-


PARAM_TKINTER = False

if PARAM_TKINTER == True:
    from src.ChatBotTkinter.ChatBotAppTkinter import ChatBotAppTkinter as ChatBot
    pass
else:
    from src.ChatBotConsole.ChatBotAppConsole import ChatBotAppConsole as ChatBot
    pass

def main():
    chatbot = ChatBot()

if __name__ == "__main__":
    main()
    pass
