from curses import panel
from tkinter import *
from tkinter.font import BOLD
from turtle import color

aplicacion = Tk()

aplicacion.title("Mi Restaurante")

# Centrar la ventana
aplicacion.geometry("1020x630+200+120")

# Evitar maximizar
aplicacion.resizable(0, 0)

# Color
aplicacion.config(bg="burlywood1")

# Panel superior
panel_superior = Frame(aplicacion, bd=2, relief=FLAT, bg="white")
panel_superior.pack(side=TOP)

# Etiqueta titulo
etiqueta_titulo = Label(
                    panel_superior, 
                    text="Sistema de Facturación", 
                    fg="azure4", 
                    font=("Dosis", 58), 
                    bg="burlywood1",
                    width=27
                    )
etiqueta_titulo.grid(row=0, column=0)

panel_izquierdo = Frame(aplicacion, bd=2, relief=FLAT, bg="white")
panel_izquierdo.pack(side=LEFT)

panel_costos = Frame(panel_izquierdo, bd=2, relief=FLAT, bg="white")
panel_costos.pack(side=BOTTOM)

panel_comidas = LabelFrame(panel_izquierdo, text="Comidas", font=("Dosis", 19, BOLD), 
                           bd=2, relief=FLAT, bg="white", fg="azure4")
panel_comidas.pack(side=LEFT)

panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Dosis", 19, BOLD), 
                           bd=2, relief=FLAT, bg="white", fg="azure4")
panel_bebidas.pack(side=LEFT)

panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Dosis", 19, BOLD), 
                           bd=2, relief=FLAT, bg="white", fg="azure4")
panel_postres.pack(side=LEFT)

panel_derecha = Frame(aplicacion, bd=2, relief=FLAT, bg="white")
panel_derecha.pack(side=RIGHT)

panel_calculadora = Frame(panel_derecha, bd=2, relief=FLAT, bg="burlywood")
panel_calculadora.pack(side=BOTTOM)

panel_recibo = Frame(panel_derecha, bd=2, relief=FLAT, bg="burlywood")
panel_recibo.pack(side=BOTTOM)

panel_botones = Frame(panel_derecha, bd=2, relief=FLAT, bg="burlywood")
panel_botones.pack(side=BOTTOM)

# Lista de Productos
lista_comidas  = ['Pizza', 'Hamburguesa', 'Papas Fritas', 'Ensalada', 'Pollo', 'Carne', 'Pescado', 'Pasta']
lista_bebidas  = ['Coca-Cola', 'Pepsi', 'Fanta', 'Sprite', 'Cerveza', 'Vino', 'Whisky', 'Ron']
lista_postres  = ['Tarta', 'Crepa', 'Helado', 'Pastel', 'Flan', 'Pudin', 'Frutillas', 'Cafe']


# Generar Items Comidas
variables_comida = []
contador = 0
for comida in lista_comidas:
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(
                panel_comidas, 
                text=comida.title(), 
                font=("Dosis", 15), 
                bg="white", 
                fg="azure4",
                onvalue=1,
                offvalue=0,
                variable=variables_comida[contador]
            )
    comida.grid(row=contador, column=0, sticky=W)
    contador += 1


# Generar Items Bebidas
variables_bebida = []
contador = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(
                panel_bebidas, 
                text=bebida.title(), 
                font=("Dosis", 15), 
                bg="white", 
                fg="azure4",
                onvalue=1,
                offvalue=0,
                variable=variables_bebida[contador]
            )
    bebida.grid(row=contador, column=0, sticky=W)
    contador += 1
    
# Generar Items Postres
variables_postre = []
contador = 0
for postre in lista_postres:
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(
                panel_postres, 
                text=postre.title(), 
                font=("Dosis", 15), 
                bg="white", 
                fg="azure4",
                onvalue=1,
                offvalue=0,
                variable=variables_postre[contador]
            )
    postre.grid(row=contador, column=0, sticky=W)
    contador += 1
    
    
# Evita que la ventana se cierre
aplicacion.mainloop()