import tkinter as tk


'''Basi bottone e label'''

def clickBottone():
   
    text = "hello"
    
    #----------------------------- widget etichetta-------------------
    #setto il colore , la tipologia di scritta e la gandezza
    testo = tk.Label(windows,text=text, fg="red", font = ("helvetical",16))
    testo.grid(row=0,column=1 )
    #testo.grid(row=0,column=1, padx=100, pady=50) # e possibile mettere i paddig
    #-------------------------------------------------------------
   
    
def clickBottone2():
   
    text = "nuovo messaggio funzione 2"
    
    #----------------------------- widget etichetta-------------------
    #setto il colore , la tipologia di scritta e la gandezza
    testo = tk.Label(windows,text=text, fg="red", font = ("helvetical",16))
    testo.grid(row=1,column=1 , padx= 50)
    #testo.grid(row=0,column=1, padx=100, pady=50) # e possibile mettere i paddig
    #-------------------------------------------------------------
    
 
    
#--------------------Finestra Principale
#creo una finestra
windows = tk.Tk()

#setto larghezza e altezza
windows.geometry("600x600")

#setto il titolo
windows.title("interfaccia grafica")
windows.resizable(False,False)  # per impedire di aumentare o diminuire la finestra si puo omettere tranquillamente

#per modificare il colore di sfondo
#windows.configure(background='blue')
#--------------------------------

#------------------------ Bottone

#aggiungo bottone, command devo mettere il metodo che gestisce il bottone
firstButton = tk.Button(text = "Saluta", command = clickBottone)
#specifichiamo la posizione di dove mettere il bottone, tramite righe e colonne
# con sticky indichiamo dove devono stare fermi i widget cioè, usando Nord,sud ,est e ovest in inglese
firstButton.grid(row = 0, column = 0, sticky = "W") ########################################### Fare prove con stickky
 
#firstButton.configure(background = 'blue')  #per modificare il colore di sfondo

#-------------------------------------------

#-------------- Bottone 2 
firstButton = tk.Button(text = "Saluta antonioo", command = clickBottone2)
#specifichiamo la posizione di dove mettere il bottone, tramite righe e colonne
firstButton.grid(row = 1, column = 0, pady=20) 



#----------------------------------------------------
windows.mainloop()  #per avviare la finestra
