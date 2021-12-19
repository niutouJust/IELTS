#!/usr/bin/python
# version python 2.7.16
# encoding:utf-8
# create date 2021-12-14 
# by NK
from src import xwg
from src import style
#
import os

class main():
    def __init__(self):
        pass
        # return self.BOOK_NAME
    def loop(self,words,type="default"):
        input_word =  raw_input("input: ")
        for i in range(1):
            self.say(words[0])
                # os.popen("say " + words[0])
            # say Chinese
            self.say(words[1])
            # os.popen("say " + words[1])
            # say synonym
            # os.popen("say " + words[2])
            while(input_word != words[0]):
                print("Error ! plaese input agin.")
                input_word =  raw_input("input: ")
                # say word
                for i in range(1):
                    self.say(words[0])
                    # os.popen("say " + words[0])
                # say Chinese
                if type == "default":
                    self.say(words[1])
                # os.popen("say " + words[1])
    def practise(self):
        arrWords = xwg.system()
        sty = style.system()
        
        for words in arrWords.bookWordsFirst():
            # print(words[0]) # english
            # print('\033[0;36m')
            print(sty.RED)
            print(sty.BOLD)
            print(words[0]) # english
            print(sty.END)
            print(words[1]) # chinese
            print(words[2]) # synonym
            self.say(words[0])
            self.loop(words) 
        for words in arrWords.bookWordsSecond():
            print(words[0])
            print(words[1])
            print(words[2])
            self.loop(words)

    def say(self,word):
        os.popen("say " + word)

process = main()
process.practise()
print("Good! Well Done.");