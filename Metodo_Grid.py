"""import tkinter as dx

ventana= dx.Tk()
ventana.geometry("640x480")
"ahora si yo quiero controlar las posiciones de estos objetos tkinder uso el metodo grid, aver digamos que tengo tres botones, boton 1, boton 2, boton3"
buton1= dx.Button(ventana, text="soy el boton1")
buton2= dx.Button(ventana, text="soy el boton2")
buton3= dx.Button(ventana, text="soy el boton3")
"entonces diriamos"
"row es fila y  column es columna xd"
buton2.grid(row=0, column=0)
"si un boton lo quiero en el centro"
buton1.grid(row = 1, column= 0)
buton3.grid(row=2,column=0)
ventana.mainloop()"""
from tkinter import *
import tkinter as dx
ventana=dx.Tk()
x=90
nashe=dx.IntVar(ventana, x)
label=dx.Label(ventana,textvariable=nashe)
label.pack()
ventana.mainloop()