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

with ftplib.FTP() as ftp:
    ftp.connect(config['ftp']['host'],port=config['ftp']['port'])
    ftp.set_debuglevel(1)
    ftp.login(config['ftp']['user'], config['ftp']['pass'])

    # change folder to LENOVO/HOME/
    ftp.cwd('LENOVO')
    ftp.cwd('HOME')

    # create /LENOVO/HOME/test folder
    ftp.cwd('test')
    #ftp.dir()
    print("FTP CONNECTED")
    #upload(ftp, sys.argv[2], sys.argv[3] if len(sys.argv) >= 4 else None)
    with open('boot.py', 'rb') as fp:
        ftp.storbinary('STOR boot.py', fp, blocksize=8192,
                      callback=None, rest=None)
    ftp.quit()

    print("FTP SEND")
