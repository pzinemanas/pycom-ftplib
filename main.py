#!/usr/bin/env micropython
# -*- coding: utf-8 -*-

from network import WLAN
import ftplib
import time
import ujson 

# load config file
with open("config.json") as fp:
    config = ujson.load(fp)

# set wlan
wlan = WLAN()
wlan.init(mode=WLAN.STA, channel=7, antenna=WLAN.INT_ANT)
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

    #ftp.voidcmd('PBSZ 0')
    #resp = ftp.voidcmd('PROT P')
    #ftp.set_pasv(False)

    

    # change folder to LENOVO/HOME/
    ftp.cwd('LENOVO')
    ftp.cwd('HOME')

#    ftp.dir()

    # create /LENOVO/HOME/test folder
 #   ftp.mkd('test')

    # change folder to /LENOVO/HOME/test
    ftp.cwd('test')

    # create a file and send it to the server
#    with open('test.txt', 'w+') as fp:
#        fp.write("Hello FTP...")
    
#    with open('test.txt', 'rb') as fp:
#        ftp.storbinary('STOR test_server.txt', fp, blocksize=8192,
#                      callback=None, rest=None)

    # get the file from the server
    #with open('test_server.txt', 'w+') as fp:
#    ftp.retrbinary("RETR test_server.txt", print_screen, blocksize=8192, rest=None)

#    with open('test_server.txt', 'rb') as fp:
#        print(fp.read())

    ftp.quit()

    print("DONE")
