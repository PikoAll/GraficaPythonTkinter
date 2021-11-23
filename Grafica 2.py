#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 19:14:50 2021

@author: ubuntu
"""

'''Basi bottone label etidtext e textArea'''

import tkinter as tk



def funzioneMia():
    
    #controllo se e stato scritto qualcosa nella edit text
    
    if textinput.get()=="" :
        
        testo = "aggiungi una parola coglione"
    
    else:
        testo = textinput.get()
        
    #----------------------- AREA testo
    areatesto = tk.Text()
    areatesto.insert(tk.END, testo) #inserisco il contenuto testuale da codice
    areatesto.grid(row=3, column = 0)

windows = tk.Tk()
windows.geometry("600x600")
windows.title("ciao")

#ora setto dicento che ci sara solo una colonna
windows.grid_columnconfigure(0, weight = 1)


etichetta = tk.Label(windows, text="aggiungi la parola", pady=10, font=("helvetica",15))

etichetta.grid(row = 0, column = 0, sticky= "N")



#------------ text edit -------------------------------
textinput = tk.Entry()# possiamo passare il parametro width per dare una dimensione fissa di larghezza e anche di altezza
textinput.grid(row = 1, column = 0 , sticky="WE",pady=10,padx=10)

#------------

#----------- Bottone

bottone = tk.Button(text='stampa', command = funzioneMia)
bottone.grid(row=2, column = 0, pady=10, padx=10, sticky="WE")


#---------------------------
windows.mainloop()

