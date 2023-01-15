from tkinter import *
import tkinter as dx

ventana= dx.Tk()
ventana.geometry("640x480")
etiqueta = dx.Label(ventana,text="Calculadore de Ecuaciones Cuadraticas", bg= "green")
"fill puede estirar a lo ancho de la pantalla con dx.X, y en lo largo de la pantalla uso dx.Y pero usando si o si expand(true o false), para ocupar toda la pantalla uso dx.BOTH"
etiqueta.pack(fill = dx.X)
def saludo():
    print("hola bb")
"para que esta funcion haga algo cuando yo apreto el boton se escribe lo sig. command = (nombre de mi funcion sin parentesis )"
boton1 = dx.Button(ventana,text="Click aqui",command= saludo)
"side puede tener valores de RIGHT, LEFT O BUTTOM QUE ES ABAJO "
"el metodo pack por ahora tiene dos funciones, que son side y fill ya explicadas anteriormente "
"la caja texto es un objeto tkinter y por eso lleva dx, al igual que todos los que llevan dx"

"ahora digamos que queremos pegar el texto pero ahora en una etiqueta, primero definiriamos nuestra etiqueta "
etiqueta2= dx.Label(ventana)
etiqueta2.pack()
"ahora para poner este texto en la etiqueta yo diria `nombre de la etiqueta` [""text""]= texto1"
cajatexto= dx.Entry(ventana, font="Helvetica")
"ahora si quiero obtener el texto de esta cajatexto harmos lo siguente "
"defino una funcion"
def textodelacaja():
    "aqui uso el metodo get, y lo que hace es traer todo lo de la caja de texto y meterlo en una variable cualquiera"
    texto1= cajatexto.get()
    "y si quiero imprimirlo?"
    print(texto1)
    etiqueta2["text"]=texto1
boton2= dx.Button(ventana, text= "click 2", command= textodelacaja)
cajatexto.pack()
boton2.pack()

boton1.pack(side= dx.BOTTOM)
"para que suceda algo con este boton se hace lo siguiente, declaramos una funcion"



ventana.mainloop()