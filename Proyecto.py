from distutils.cmd import Command
from tkinter import *
from math import *
import math as calculos
import tkinter as dx
from PIL import Image,ImageTk
ventana= dx.Tk()
ventana.title("Calculadora de Ecuaciones Cuadraticas")
ventana.geometry("1280x720")
ventana.iconbitmap("favicon.ico")
fonditouwu=Image.open("fondito3.jpg")
fonditouwu=fonditouwu.resize((1920,1080),Image.LANCZOS)
img=ImageTk.PhotoImage(fonditouwu)
mostrandoimagen=Label(ventana,image=img).place(x=0,y=0)
"Mensajes, defino los mensajes que se van a asignar para cada instancia"
msj1=dx.Label(ventana, text="Ingrese el termino cuadratico --> ",font="Ubuntu")
msj2=dx.Label(ventana, text= "Ingrese el termino lineal --> ",font="Ubuntu")
msj3=dx.Label(ventana,text= "Ingrese el termino independiente --> ",font="Ubuntu")
msj4=dx.Label(ventana,text="Analizando el dsicriminante obtenemos que ",font="Ubuntu")
"Valores"
A=dx.Entry(ventana)
B=dx.Entry(ventana)
C=dx.Entry(ventana)
"Funciones: defino mis funciones para poder sacar primero los datos del entry y luego hago otra funcion para sacar ya las soluciones utilizando las formulas"
i=0
def numeroA():
    global i
    a=A.get()
    if A== None:
        a=0
    i=i+1
def numeroB():
    global i
    b=B.get()
    i=i+1
def numeroC():
    global i
    c=C.get()
    i=i+1
def formula():
    "analizo el discriminante"
    discr= (int(B.get())**2)-4*int(A.get())*int(C.get())
    "pregunto si el dsicriminante es mayor a cero, el i este quiza no sirva de mucho para la condicion"
    if discr>=0 and i==3:
        msj5=dx.Label(ventana,text="Si tiene solucion",font="Ubuntu")
        "ubico al mensaje 6 con el metodo place"
        msj5.place(relx=0.31,rely=0.5)
        "calculo la primera solucion llamandola x_pos"
        x_pos=(-int(B.get())+calculos.sqrt((int(B.get()))**2-4*int(A.get())*int(C.get())))/(2*int(A.get()))
        "calculo la segunda solucion llamandola x_neg"
        x_neg=(-int(B.get())-calculos.sqrt((int(B.get()))**2-4*int(A.get())*int(C.get())))/(2*int(A.get()))
        "utilizo intvar para poder usar mis soluciones en una variable"
        solpos=dx.IntVar(ventana,x_pos)
        "y luego usarla en esta nueva variable y asi poder mostrar las soluciones"
        mostrarsolpos=dx.Label(ventana, textvariable=solpos)
        mostrarsolpos.place(relx=0.35,rely=0.6)
        solneg=dx.IntVar(ventana,x_neg)
        mostrarsolneg=dx.Label(ventana, textvariable=solneg)
        mostrarsolneg.place(relx=0.31,rely=0.6)
    else:
        msj5=dx.Label(ventana,text="No tiene solucion en el conjunto de los numeros reales", font="Ubuntu")
        msj5.place(relx=0.31,rely=0.4)
        ventana_nueva=Toplevel()
        ventana_nueva.title("Mensaje")
        ventana_nueva.iconbitmap("favicon.ico")
        ventana_nueva.geometry("380x420")
        ventana_nueva.configure(bg="black")
        msjerror=dx.Label(ventana_nueva,text="ERROR :(",font=("Bahnschrift Light", 50),fg="#FFFFFF",bg='#000').place(relx=0.2,rely=0.3)
"Botones"
Ingresar_a=dx.Button(ventana,text="Click aqui para ingresar a",command= numeroA,font="Ubuntu")
Ingresar_b=dx.Button(ventana,text="Click aqui para ingresar b",command= numeroB,font="Ubuntu")
Ingresar_c=dx.Button(ventana,text="Click aqui para ingresar c",command= numeroC,font="Ubuntu")
calcularsolucion=dx.Button(ventana,text="Haga click aqui para obtener la solucion", command= formula,font="Ubuntu")
"Posiciones"
msj1.place(relx=0.01,rely=0.1)
msj2.place(relx=0.31,rely=0.1)
msj3.place(relx=0.60,rely=0.1)
A.place(relx=0.20,rely=0.1,relwidth=0.05)
B.place(relx=0.50,rely=0.1,relwidth=0.05)
C.place(relx=0.80,rely=0.1,relwidth=0.05)
Ingresar_a.place(relx=0.20,rely=0.2)
Ingresar_b.place(relx=0.50,rely=0.2)
Ingresar_c.place(relx=0.80,rely=0.2)
msj4.place(relx=0.31,rely=0.4)
calcularsolucion.place(relx=0.31,rely=0.3)
ventana.mainloop()