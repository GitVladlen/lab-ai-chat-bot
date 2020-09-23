#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse


def main():
    ap = argparse.ArgumentParser()

    ap.add_argument("-c", "--console", required=False,
                    help="first operand")
    args = vars(ap.parse_args())

    if not args["console"]:
        from src.ChatBotTkinter.ChatBotAppTkinter import ChatBotAppTkinter as ChatBot
        pass
    else:
        from src.ChatBotConsole.ChatBotAppConsole import ChatBotAppConsole as ChatBot
        pass

    chatbot = ChatBot()

    chatbot.run()


if __name__ == "__main__":
    main()
    pass
