#!bin/env python3
# Coded by Ahadu Eyasu, Ethiopia

import configparser
import os, sys
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

cpass = configparser.RawConfigParser()
cpass.add_section('cred')

def banner():
    print(gr+"  ___  ___| |_ _   _ _ __     ")
    print(gr+"/ __|/ _ \ __| | | | '_ \               ")
    print(re+"\__ \  __/ |_| |_| | |_) |          ")
    print(cy+"|___/\___|\__|\__,_| .__/       ")
    print(gr+"                   |_|           ")

    print(gr+" Version: 2.0")
    
    print(cy+" Made by Ahadu, Ethiopia ")

    
                                                                          
    
    
banner()
print(gr+"Installing useful data...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()
os.system("touch config.data")
xid = input(gr+"[-] Enter api_id: "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[-] Enter hash_id: "+re)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[-] Enter phone number: "+re)
cpass.set('cred', 'phone', xphone)
setup = open('config.data', 'w')
cpass.write(setup)
setup.close() 
print(gr+"You successfuly activate the hack.")
print(gr+"You can run the tools know.")
print(gr+"And please don't forget to join my channel https://t.me/all_in_one_ethio_channel.")   