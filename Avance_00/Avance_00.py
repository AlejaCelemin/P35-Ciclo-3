###.   MÓDULO DE LOGIN DEL SISTEMA
#EL EQUIPO deberá desarrollar el módulo que permita el ingreso al sistema, una vez se haya realizado la validación por nombre de usuario y contraseña.
### Deberá tenerse un usuario por defecto con el nombre de admininicial, y contraseña admin123456 para su ingreso la primera vez.

############  AVANCE_00 ################

##### Login ######

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Login")
root.geometry("300x150")
root.resizable(width=False, height=False)
root.config(bg="pink")

usuario=Label(root, text="Ingrese nombre de usuario:")
usuario.pack()

usuario1 =StringVar()
usu=Entry(root, width=30, textvariable=usuario1)
usu.pack()

contraseña=Label(root, text="contraseña:")
contraseña.pack()

contra=StringVar()
contra1=Entry(root, width=30, textvariable=contra, show="*")
contra1.pack()

def ingresar():
    if usuario1.get()=="admininicial" and contra.get()=="admi123456":
        root.title("Si puede Ingresar")
    else:
        root.title("Incorrecto")

bt=Button(root, text="Entrar", command=ingresar)
bt.pack(side=BOTTOM)


root.mainloop()

