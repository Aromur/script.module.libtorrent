#-*- coding: utf-8 -*-
'''
    Torrenter v2 plugin for XBMC/Kodi
    Copyright (C) 2015 srg70, RussakHH, DiMartino
'''

import sys
import os
try:
    import xbmc
except:
    pass

def get_libname(platform):
    libname=[]
    if platform['system'] in ['darwin', 'linux_x86', 'linux_x86_64']:
        libname=['libtorrent.so']
    elif platform['system'] == 'windows':
        libname=['libtorrent.pyd']
    elif platform['system'] == 'android_armv7':
        libname=['libtorrent.so', 'liblibtorrent.so']
    return libname

def get_platform():
    ret = {
        "arch": sys.maxsize > 2 ** 32 and "x64" or "x86",
    }
    if xbmc.getCondVisibility("system.platform.android"):
        ret["os"] = "android"
        if "arm" in os.uname()[4]:
            ret["arch"] = "arm"
    elif xbmc.getCondVisibility("system.platform.linux"):
        ret["os"] = "linux"
        if "arm" in os.uname()[4]:
            ret["arch"] = "arm"
    elif xbmc.getCondVisibility("system.platform.xbox"):
        system_platform = "xbox"
        ret["arch"] = ""
    elif xbmc.getCondVisibility("system.platform.windows"):
        ret["os"] = "windows"
    elif xbmc.getCondVisibility("system.platform.osx"):
        ret["os"] = "darwin"
    elif xbmc.getCondVisibility("system.platform.ios"):
        ret["os"] = "ios"
        ret["arch"] = "arm"

    ret["system"] = ''
    ret["message"] = ['', '']

    if ret["os"] == 'windows':
        ret["system"] = 'windows'
        ret["message"] = ['Windows has static compiled python-libtorrent included.',
                          'You should install "script.module.libtorrent" from "MyShows.me Kodi Repo"']
    elif ret["os"] == "linux" and ret["arch"] == "x64":
        ret["system"] = 'linux_x86_64'
        ret["message"] = ['Linux x64 has not static compiled python-libtorrent included.',
                          'You should install it by "sudo apt-get install python-libtorrent"']
    elif ret["os"] == "linux" and ret["arch"] == "x86":
        ret["system"] = 'linux_x86'
        ret["message"] = ['Linux has static compiled python-libtorrent included but it didn\'t work.',
                          'You should install it by "sudo apt-get install python-libtorrent"']
    elif ret["os"] == "linux" and ret["arch"] == "arm":
        ret["system"] = 'linux_arm'
        ret["message"] = ['As far as I know you can compile python-libtorrent for ARMv6-7.',
                          'You should search for "OneEvil\'s OpenELEC libtorrent" or use Ace Stream.']
    elif ret["os"] == "android":
        if ret["arch"]=='arm':
            ret["system"] = 'android_armv7'
        else:
            ret["system"] = 'android_x86'
        ret["message"] = ['Please contact DiMartino on kodi.tv forum. We compiled python-libtorrent for Android,',
                          'but we need your help with some tests on diffrient processeors.']
    elif ret["os"] == "darwin":
        ret["system"] = 'darwin'
        ret["message"] = ['It is possible to compile python-libtorrent for OS X.',
                          'But you would have to do it by yourself, there is some info on github.com.']
    elif ret["os"] == "ios":
        ret["system"] = 'ios'
        ret["message"] = ['It is probably NOT possible to compile python-libtorrent for iOS.',
                          'But you can use torrent-client control functions.']

    return ret