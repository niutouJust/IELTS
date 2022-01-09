#!/usr/bin/python3
# encoding:utf-8
# create date: 2021-12-14 
# by NK
# issues: https://github.com/niutouJust/IELTS/issues/9
# requirement:
# curl
# 
import os
import time
import shlex, subprocess
# pip3 install mp3play in windows https://pypi.org/project/mp3play/
# import mp3play 

# pip3 install download https://pypi.org/project/download/
from download import download

# Error: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)>
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class system:
        #FILE_URL = r"https://sp1.baidu.com/-rM1hT4a2gU2pMbgoY3K/gettts?lan=en&spd=2&source=alading&text="
        FILE_URL = r"https://dict.youdao.com/dictvoice?type=2&audio="

        def __init__(self):
                pass
        
        def downFileAndSayByMacos(self,keyword):
                filename = str(keyword.replace(' ','_')) + '.mp3'
                url = self.FILE_URL + str(keyword.replace(" ",'%20'))
                file_path = './tmp/' + filename
                play_cmd = "afplay " + file_path
                # if file is exists, then skip.
                if os.path.isfile(file_path) is False:
                        command_line = "curl  -s  -o" + file_path + " " + str(url) 
                        # change command to list
                        args = shlex.split(command_line)
                        # exec command
                        p = subprocess.Popen(args)
                        if (p is True):
                                time.sleep(0.5)
                                os.popen(play_cmd)
                        # play command
                        # os.popen(play_cmd)
                else:
                        # play mp3
                        while(os.path.isfile(file_path) is True):
                                os.popen(play_cmd)
                                time.sleep(0.5)
                                break
                return True

        def sayWindows(self,keyword):
                # waiting for dev
                # path = self.downFile(keyword)
                # clip = mp3play.load(filename)
                # clip.play()
                pass

        # def sayMacos(self,keyword):
        #         self.downFile(keyword)
        #         path = './tmp/' + str(keyword) + ".mp3"
        #         while(os.path.isfile(path) is False):
        #                 os.popen("afplay " + str(path))
        #                 time.sleep(0.1)
