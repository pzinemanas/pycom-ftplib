#!/usr/bin/env micropython
# -*- coding: utf-8 -*-

from network import WLAN
import ftplib
import time
import ujson 
import os

# load config file
with open("config.json") as fp:
    config = ujson.load(fp)

# set wlan
wlan = WLAN()
wlan.init(mode=WLAN.STA_AP, channel=7, antenna=WLAN.INT_ANT, ssid="wipy-wlan")
wlan.connect(config['wifi']['ssid'], auth=(WLAN.WPA2, config['wifi']['pass']))

while not wlan.isconnected():
    time.sleep_ms(50)

print("WIFI CONNECTED")

def print_screen(x):
    print(x)

with ftplib.FTP() as ftp:
    ftp.connect(config['ftp']['host'],port=config['ftp']['port'],timeout=0.1)
    ftp.set_debuglevel(1)
    ftp.login(config['ftp']['user'], config['ftp']['pass'])

    # create folder test
    ftp.mkd('test')

    # cd to test
    ftp.cwd('test')
    

    # create a file and send it to the server
    with open('test.txt', 'w+') as fp:
        fp.write("Hello FTP...")
    
    with open('test.txt', 'rb') as fp:
        ftp.storbinary('STOR test_server.txt', fp, blocksize=8192,
                      callback=None, rest=None)

    # dir
    ftp.dir()

    # get the file from the server
    with open('test_server.txt', 'w+') as fp:
        ftp.retrbinary("RETR test_server.txt", fp.write, blocksize=8192, rest=None)

    with open('test_server.txt', 'r') as fp:
        print(fp.read())


    # remove files
    ftp.delete('test_server.txt')
    ftp.cwd('..')
    ftp.rmd('test')

    ftp.quit()

    os.remove('test.txt')
    os.remove('test_server.txt')

    print("DONE")
