#!/usr/bin/python3
# version Python 3.8.1rc1
# encoding:utf-8
# create date 2021-12-14 
# by NK
# practice listen words
from src import ysw
from src import style
from src import voice

#
import os
import time
import sqlite3

class main():
    def __init__(self):
        self.style = style.system()
        self.voice = voice.system()
        self.Words = ysw.system()
        self.log_file_xwg_a = "./tmp/ysw-a.log"
        self.log_file_xwg_b = "./tmp/ysw-b.log"
        self.log_file_xwg_c = "./tmp/ysw-c.log"
        fopen_xwg_a = os.open(self.log_file_xwg_a,os.O_RDWR|os.O_CREAT)
        fopen_xwg_b = os.open(self.log_file_xwg_b,os.O_RDWR|os.O_CREAT)
        fopen_xwg_c = os.open(self.log_file_xwg_c,os.O_RDWR|os.O_CREAT)
        read_content_xwg_a = os.read(fopen_xwg_a,100)
        read_content_xwg_b = os.read(fopen_xwg_b,100)
        read_content_xwg_c = os.read(fopen_xwg_c,100)
        self.log_word_xwg_a = read_content_xwg_a.decode()
        self.log_word_xwg_b = read_content_xwg_b.decode()
        self.log_word_xwg_c = read_content_xwg_c.decode()
        self.option = 'Y' # default is N
        conn = sqlite3.connect('test.db')
        print(conn)
    # input continue
    def loop(self,words,type="default"):
        print(self.style.BLUE)
        input_word =  input("【input the word】: ")
        print(self.style.END)
        for i in range(1):
            while(input_word != words[0]):
                print(self.style.BLUE)
                print("Error ! plaese input agin.")
                input_word =  input("【input the word】: ")
                print(self.style.END)
                # say word
                for i in range(1):
                    self.say(words[0],2)
            print(self.style.GREEN)
            print('OK!')
            print(self.style.END)

    # proctice main process
    def practice(self):
        self.option = 'Y'
        self.checkLog(self.log_word_xwg_a)
        for words in self.Words.bookWordsFirst():
            if (self.option == 'N'):
                if words[0].strip() == self.log_word_xwg_a.strip():
                   self.option = 'Y'
                else:
                    continue
            self.practiceProcess(words)
            self.practiceLogLinux(self.log_file_xwg_a,words[0])
        self.option = 'Y'
        self.checkLog(self.log_word_xwg_b)
        for words in self.Words.bookWordsSecond():
            if (self.option == 'N'):
                if words[0].strip() == self.log_word_xwg_b.strip():
                   self.option = 'Y'
                else:
                    continue
            self.practiceProcess(words)
            self.practiceLogLinux(self.log_file_xwg_b,words[0])
        # self.option = 'Y'
        # self.checkLog(self.log_word_xwg_c)
        # for words in self.Words.bookWordsThird():
        #     if (self.option == 'N'):
        #         if words[0].strip() == self.log_word_xwg_c.strip():
        #            self.option = 'Y'
        #         else:
        #             continue
        #     self.practiceProcess(words)
        #     self.practiceLogLinux(self.log_file_xwg_c,words[0])

    # check log word
    def checkLog(self,log_word):
        if log_word != '':
            print("Found the a log file, do you want to restart ?\n")
            print("Last Word:" + log_word)
            self.option = input("Option: Y or N(default) \n")
        if self.option == '':
            self.option = 'N'
    
    # practice print and saying
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
            # self.sayChinese(words[1],1) # do not say Chinese
            self.loop(words) 

    # saying
    def say(self,word,count):
        for i in range(count):
            #in Macos
            self.voice.downFileAndSayByMacos(word)
            time.sleep(0.5)
    # say Chinese 
    def sayChinese(self,word,count):
        os.popen("say " + str(word))

    # waiting dev
    def practiceLog(self,fopen,key):
        os.write(fopen,str.encode(key))

    # save word to log
    def practiceLogLinux(self,file_name,key):
        os.popen("echo "+ key + " >" + file_name)
        

process = main()
process.practice()
print("Good! Well Done.");