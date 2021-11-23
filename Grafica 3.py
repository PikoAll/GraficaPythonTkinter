#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 19:37:59 2021

@author: ubuntu
"""

'''Grafica menu in alto tipo file modifica....'''
'''Bottone con la spunta, bottoni radio'''
'''Menu a tendina'''


import tkinter as tk
from tkinter import ttk


def opeN():
    
    label = tk.Label(windows,text = 'hai cliccato open')
    label.grid(row=0,column=0)
    

def uscita():
    
    label = tk.Label(windows,text = 'hai cliccato exit')
    label.grid(row=0,column=0)


def callback():
    label = tk.Label(windows,text = ckValue.get())
    label.grid(row = 1, column=1)
   # chkExample.toggle()  # per lasciareselezionato o deselezionato sempre la spunta



def provaradio():
    etichettaRadio = tk.Label(windows,textvariable = radioValore)
    etichettaRadio.grid(row = 2, column =1)

def callbackFunc(event):
     print("New Element Selected")
     print(combo.current(), combo.get())

windows = tk.Tk()

windows.geometry("600x600")
windows.title('menu in alto')

menuBar = tk.Menu(windows)  #passo la finestra principale come parametro

fileMenu = tk.Menu(menuBar) # gli dico che deve stare dentro il menu bar
fileMenu.add_command(label = 'open', command = opeN)
fileMenu.add_command(label = 'exit', command = uscita)

menuBar.add_cascade(label="file", menu = fileMenu)

menu2 = tk.Menu()

menuBar.add_cascade(label="help",menu=menu2)

windows.config(menu=menuBar)


#------------ Bottone con la spunta

ckValue = tk.BooleanVar()
ckValue.set(True)

chkExample = tk.Checkbutton(windows,text = 'clicca',var=ckValue, command = callback)

chkExample.grid(row=1,column=0)


#-------------

#------------Bottoni radio

radioValore = tk.IntVar()

radio1 = tk.Radiobutton(windows,text="gennaio",variable = radioValore, value=0,command = provaradio)
radio2 = tk.Radiobutton(windows,text="febr",variable = radioValore, value=1,command = provaradio)

radio1.grid(row=2,column=0)
radio2.grid(row=3,column=0)



#---------------------

#---------------- menu a tendina ------

combo = ttk.Combobox(windows,values =[1,2,3])

combo.current(0) #per settare il valore che deve essere visto


combo.grid(row=4,column=0)
combo.bind("<<ComboboxSelected>>", callbackFunc)


#---------------













windows.mainloop()






