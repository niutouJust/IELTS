#!/usr/bin/python3
# version Python 3.8.1rc1
# encoding:utf-8
# create date 2021-12-14 
# by NK
from src import xwg
from src import style
from src import voice
#
import os
import time

class main():
    def __init__(self):
        self.style = style.system()
        self.voice = voice.system()
        self.Words = xwg.system()
        self.log_file_xwg = "./tmp/xwg-1.log"
        self.fopen_xwg = os.open(self.log_file_xwg,os.O_RDWR|os.O_CREAT)
        # lock_file = "./tmp/keywords.lock"
        # if os.path.isfile(lock_file) is False:
        #     self.downVice()
            # os.open(lock_file,os.O_CREAT)
        # else:
        #     print("if you want to download new keywords files , you can remove './tmp/keywords.lock' file")
        # return self.BOOK_NAME
    def downVice(self):
        # pass
        # for words in self.Words.bookWordsFirst():
        #     self.voice.downFileAndSayByMacos(words[0])
        #     time.sleep(0.1)
        # for words in self.Words.bookWordsSecond():
        #     self.voice.downFile(words[0])
        #     time.sleep(0.1)
        print("Downloads is Finish")
    def loop(self,words,type="default"):
        input_word =  input("input: ")
        for i in range(1):
            # self.say(words[0])
                # os.popen("say " + words[0])
            # say Chinese
            # self.say(words[1])
            # os.popen("say " + words[1])
            # say synonym
            # os.popen("say " + words[2])
            # time.sleep(1)
            while(input_word != words[0]):
                print("Error ! plaese input agin.")
                input_word =  input("input: ")
                # say word
                for i in range(1):
                    self.say(words[0],2)
                    # os.popen("say " + words[0])
                # say Chinese
                if type == "default":
                    self.say(words[1],2)
                # os.popen("say " + words[1])
            print(self.style.GREEN)
            print('OK!')
            print(self.style.END)
    def practice(self):
        
        for words in self.Words.bookWordsFirst():
            self.practiceProcess(words)
            self.practiceLog(self.fopen_xwg,words[0])
            #pass
            # print(words[0]) # english
            # print('\033[0;36m')
            # print(self.style.RED)
            # print(self.style.BOLD)
            # print(words[0]) # english
            # print(self.style.END)
            # print(words[1]) # chinese
            # print(self.style.YELLOW)
            # print(words[2]) # synonym
            # print(self.style.END)
            # self.say(words[0],2)
            # time.sleep(0.2)
            # self.sayChinese(words[1],1)
            # self.loop(words) 
        for words in self.Words.bookWordsSecond():
            self.practiceProcess(words)

    def practiceProcess(self,words):
            print(self.style.RED)
            print(self.style.BOLD)
            print(words[0]) # english
            print(self.style.END)
            print(words[1]) # chinese
            print(self.style.YELLOW)
            print(words[2]) # synonym
            print(self.style.END)
            self.say(words[0],2)
            time.sleep(0.2)
            self.sayChinese(words[1],1)
            self.loop(words) 

    def say(self,word,count):
        for i in range(count):
            #in Macos
            self.voice.downFileAndSayByMacos(word)
            time.sleep(1)
    def sayChinese(self,word,count):
        os.popen("say " + str(word))

    def practiceLog(self,fopen,key):
        
        os.write(fopen,str.encode(key))

process = main()
process.practice()
print("Good! Well Done.");