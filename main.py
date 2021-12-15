#!/usr/bin/python
# version python 2.7.16
# encoding:utf-8
# create date 2021-12-14 
# by NK
from src import xwg
#
import os

class main():
    def __init__(self):
        pass
        # return self.BOOK_NAME
        
    def practise(self):
        arrWords = xwg.system()

        for words in arrWords.bookWordsFirst():
            print(words[0])
            print(words[1])
            print(words[2])
            input_word =  raw_input("input: ")
            # say word
            for i in range(1):
                os.popen("say " + words[0])
            # say Chinese
            os.popen("say " + words[1])
            # say synonym
            os.popen("say " + words[2])
            while(input_word != words[0]):
                print("Error ! plaese input agin.")
                input_word =  raw_input("input: ")
                # say word
                for i in range(1):
                    os.popen("say " + words[0])
                # say Chinese
                os.popen("say " + words[1])
        for words in arrWords.bookWordsSecond():
            print(words[0])
            print(words[1])
            print(words[2])
            input_word =  raw_input("input: ")
            # say word
            for i in range(1):
                os.popen("say " + words[0])
            # say Chinese
            os.popen("say " + words[1])
            # say synonym
            os.popen("say " + words[2])
            while(input_word != words[0]):
                print("Error ! plaese input agin.")
                input_word =  raw_input("input: ")
                # say word
                for i in range(1):
                    os.popen("say " + words[0])
                # say Chinese
                os.popen("say " + words[1])

process = main()
process.practise()