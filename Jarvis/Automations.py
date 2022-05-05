from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep


def WhatsappMsg(name,message):


    startfile("C:\\Users\\veda\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

    sleep(10)

    click(x=212, y=143)    

    sleep (2)

    write(name)

    sleep(2)

    click(x=203, y=302)

    sleep(2)

    click (x=830, y=995)

    sleep(2)

    write(message)

    press("Enter")

def WhatappChat(name):
     startfile("C:\\Users\\veda\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

     sleep(10)

     click(x=212, y=143)    

     sleep (2)

     write(name)

     sleep(2)
 
     click(x=203, y=302)

     sleep(2)

     click (x=830, y=995)

     sleep(2)
