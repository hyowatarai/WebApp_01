import time
import subprocess
from unicodedata import name
import pyautogui as pg
from flask import request
import os
import pywinauto as pwa
import PySimpleGUI as sg
import schedule
import sched
import time
import datetime
import random
import glob
import threading
import sys
from pathlib import Path

def task0(Nyu, Pass):

    path1=r"C:\Users\gutar\zooming\pics\home.png"
    path2=r"C:\Users\gutar\zooming\pics\sanka.png" 

    subprocess.Popen(r'C:\Users\gutar\AppData\Roaming\Zoom\bin\Zoom.exe')
    time.sleep(3)

    #ホームページに遷移
    try:
        p1=pg.locateOnScreen(path1,confidence=0.8)
        x1, y1 = pg.center(p1)
        pg.doubleClick(x1, y1)
    except TypeError:
        pass

    #参加をクリック
    time.sleep(2)
    p2 = pg.locateOnScreen(path2,confidence=0.8)
    x2,y2 = pg.center(p2)
    pg.doubleClick(x2,y2)
    #ミーティングIDを入力
    time.sleep(2)
    pg.typewrite("{}".format(Nyu))
    pg.press("Enter")

    #パスワードを入力
    time.sleep(2)
    pg.typewrite("{}".format(Pass))
    pg.press("Enter")

# zoom_path=r""#Zoom.exeのパスを定義
# path1=r""#ホームページの画像のパスを定義
# path2=r""#参加ボタンの画像のパスを定義
# path3=r""#退出ボタンの画像のパスを定義