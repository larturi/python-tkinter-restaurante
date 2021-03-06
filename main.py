import tkinter
from curses import panel
from tkinter import *
from tkinter.font import BOLD
from turtle import color

# ########################################################################
# ########################## Configuracion General #######################
# ########################################################################

aplicacion = Tk()

aplicacion.title("Mi Restaurante")

# Centrar la ventana
window_height = 630
window_width = 1100
screen_width = aplicacion.winfo_screenwidth()
screen_height = aplicacion.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
aplicacion.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# Evitar maximizar
aplicacion.resizable(0, 0)

# Color
aplicacion.config(bg="#353535")


# ########################################################################
# ################################# Layout ###############################
# ########################################################################

# Panel superior
panel_superior = Frame(aplicacion, bd=2, relief=FLAT, bg="#353535")
panel_superior.pack(side=TOP)

# Etiqueta titulo
etiqueta_titulo = Label(
                    panel_superior, 
                    text="Sistema de Facturación", 
                    fg="#f1f1f1", 
                    font=("Dosis", 58), 
                    bg="#353535",
                    width=27
                    )
etiqueta_titulo.grid(row=0, column=0)

# ############ Panel Izquierdo ############
panel_izquierdo = Frame(aplicacion, bd=2, relief=FLAT, bg="#353535", padx=0)
panel_izquierdo.pack(side=LEFT)

panel_costos = Frame(panel_izquierdo, bd=2, relief=FLAT, bg="#232323", padx=5, pady=10)
panel_costos.pack(side=BOTTOM)

panel_comidas = LabelFrame(panel_izquierdo, text="Comidas", font=("Dosis", 19, BOLD), 
                           bd=2, relief=FLAT, bg="#353535", fg="#f1f1f1", padx=10, pady=10)
panel_comidas.pack(side=LEFT)

panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Dosis", 19, BOLD), 
                           bd=2, relief=FLAT, bg="#353535", fg="#f1f1f1", padx=10, pady=10)
panel_bebidas.pack(side=LEFT)

panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Dosis", 19, BOLD), 
                           bd=2, relief=FLAT, bg="#353535", fg="#f1f1f1", padx=10, pady=10)
panel_postres.pack(side=LEFT)

# ############ Panel Derecho ############
panel_derecha = Frame(aplicacion, bd=2, relief=FLAT, bg="#353535")
panel_derecha.pack(side=RIGHT)

panel_calculadora = Frame(panel_derecha, bd=2, relief=FLAT, bg="#353535")
panel_calculadora.pack()

panel_recibo = Frame(panel_derecha, bd=2, relief=FLAT, bg="#353535")
panel_recibo.pack()

panel_botones = Frame(panel_derecha, bd=2, relief=FLAT, bg="#353535")
panel_botones.pack()


# ########################################################################
# ####################### Panel Izquierda (Alimentos) ####################
# ########################################################################
lista_comidas  = ['Pizza', 'Hamburguesa', 'Papas Fritas', 'Ensalada', 'Pollo', 'Carne', 'Pescado', 'Pasta']
lista_bebidas  = ['Coca-Cola', 'Pepsi', 'Fanta', 'Sprite', 'Cerveza', 'Vino', 'Whisky', 'Ron']
lista_postres  = ['Tarta', 'Crepa', 'Helado', 'Pastel', 'Flan', 'Pudin', 'Frutillas', 'Cafe']

# ############ Generar Items Comidas ############
variables_comida = []
cuadros_comida = []
texto_comida = []

contador = 0
for comida in lista_comidas:
    
    # Crear los checkbox
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(
                panel_comidas, 
                text=comida.title(), 
                font=("Dosis", 15), 
                bg="#353535", 
                fg="#f1f1f1",
                onvalue=1,
                offvalue=0,
                variable=variables_comida[contador]
            )
    comida.grid(row=contador, column=0, sticky=W)
    
    # Crear los cuadros de texto
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set("0")
    
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=("Dosis", 15, BOLD),
                                     bd=2,
                                     width=6,
                                     state=DISABLED,
                                     bg="#353535",
                                     textvariable=texto_comida[contador])
    
    cuadros_comida[contador].grid(row=contador, column=1)
    
    contador += 1

# ############ Generar Items Bebidas ############
variables_bebida = []
cuadros_bebida = []
texto_bebida = []

contador = 0
for bebida in lista_bebidas:
    
    # Crear los checkbox
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(
                panel_bebidas, 
                text=bebida.title(), 
                font=("Dosis", 15), 
                bg="#353535", 
                fg="#f1f1f1",
                onvalue=1,
                offvalue=0,
                variable=variables_bebida[contador]
            )
    bebida.grid(row=contador, column=0, sticky=W)
    
    # Crear los cuadros de texto
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set("0")
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=("Dosis", 15, BOLD),
                                     bd=2,
                                     width=6,
                                     state=DISABLED,
                                     bg="#353535",
                                     textvariable=texto_bebida[contador])
    
    cuadros_bebida[contador].grid(row=contador, column=1)
    
    contador += 1
    
# ############ Generar Items Postres ############
variables_postre = []
cuadros_postre = []
texto_postre = []

contador = 0
for postre in lista_postres:
    
    # Crear los checkbox
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(
                panel_postres, 
                text=postre.title(), 
                font=("Dosis", 15), 
                bg="#353535", 
                fg="#f1f1f1",
                onvalue=1,
                offvalue=0,
                variable=variables_postre[contador]
            )
    postre.grid(row=contador, column=0, sticky=W)
    
    # Crear los cuadros de texto
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set("0")
    cuadros_postre[contador] = Entry(panel_postres,
                                     font=("Dosis", 15, BOLD),
                                     bd=2,
                                     width=6,
                                     state=DISABLED,
                                     bg="#353535",
                                     textvariable=texto_postre[contador])
    
    cuadros_postre[contador].grid(row=contador, column=1)

    contador += 1
    
# ########################################################################
# ############################# Panel Derecha ############################
# ########################################################################

var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

# Costo Comida
etiqueta_costo_comida = Label(panel_costos,
                              text="Costo Comida",
                              font=("Dosis", 15, BOLD),
                              bg="#232323",
                              fg="#f1f1f1")
etiqueta_costo_comida.grid(row=0, column=0, sticky=W)

texto_costo_comida = Entry(panel_costos,
                           font=("Dosis", 15, BOLD),
                           bd=2,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_comida)

texto_costo_comida.grid(row=0, column=1, padx=41)

# Costo Bebida
etiqueta_costo_bebida = Label(panel_costos,
                              text="Costo Bebida",
                              font=("Dosis", 15, BOLD),
                              bg="#232323",
                              fg="#f1f1f1")
etiqueta_costo_bebida.grid(row=1, column=0, sticky=W)

texto_costo_bebida = Entry(panel_costos,
                           font=("Dosis", 15, BOLD),
                           bd=2,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_bebida)

texto_costo_bebida.grid(row=1, column=1, padx=41)

# Costo Postres
etiqueta_costo_postre = Label(panel_costos,
                              text="Costo Postres",
                              font=("Dosis", 15, BOLD),
                              bg="#232323",
                              fg="#f1f1f1")
etiqueta_costo_postre.grid(row=2, column=0, sticky=W)

texto_costo_postre = Entry(panel_costos,
                           font=("Dosis", 15, BOLD),
                           bd=2,
                           width=10,
                           state="readonly",
                           textvariable=var_costo_postre)

texto_costo_postre.grid(row=2, column=1, padx=41)


# Subtotal
etiqueta_subtotal = Label(panel_costos,
                              text="Subtotal",
                              font=("Dosis", 15, BOLD),
                              bg="#232323",
                              fg="#f1f1f1")
etiqueta_subtotal.grid(row=0, column=2, sticky=W)

texto_subtotal = Entry(panel_costos,
                           font=("Dosis", 15, BOLD),
                           bd=2,
                           width=10,
                           state="readonly",
                           textvariable=var_subtotal)

texto_subtotal.grid(row=0, column=3, padx=41)


# Impuestos
etiqueta_impuestos = Label(panel_costos,
                              text="Impuestos",
                              font=("Dosis", 15, BOLD),
                              bg="#232323",
                              fg="#f1f1f1")
etiqueta_impuestos.grid(row=1, column=2, sticky=W)

texto_impuestos = Entry(panel_costos,
                           font=("Dosis", 15, BOLD),
                           bd=2,
                           width=10,
                           state="readonly",
                           textvariable=var_impuestos)

texto_impuestos.grid(row=1, column=3, padx=41)

# Total
etiqueta_total = Label(panel_costos,
                              text="Total",
                              font=("Dosis", 15, BOLD),
                              bg="#232323",
                              fg="#f1f1f1")
etiqueta_total.grid(row=2, column=2, sticky=W)

texto_total = Entry(panel_costos,
                           font=("Dosis", 15, BOLD),
                           bd=2,
                           width=10,
                           state="readonly",
                           textvariable=var_total)

texto_total.grid(row=2, column=3, padx=41)

# ########################################################################
# ############################ Panel Derecha #############################
# ########################################################################

# Botones

botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []
columnas = 0

for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=("Dosis", 15, 'bold'),
                   fg='#232323',
                   bg='#232323',
                   bd=1,
                   width=6,
                   height=2)
    
    botones_creados.append(boton)
    
    boton.grid(row=0, column=columnas, padx=2, pady=2)
    columnas += 1
    
# Recibo
texto_recibo = Text(panel_recibo,
                    font = ("Dosis", 15, 'bold'),
                    bd=1,
                    width=37,
                    height=10)

texto_recibo.grid(row=0, column=0)


# calculadora

visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 22, 'bold'),
                          width=27,
                          bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-',
                       '1', '2', '3', 'x', 'R', 'B', '0', '/']
botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='#232323',
                   bg='#232323',
                   bd=1,
                   width=5,
                   height=2)

    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna)

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

# Evita que la ventana se cierre
aplicacion.mainloop()