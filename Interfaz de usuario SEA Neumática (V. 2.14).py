# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 23:21:33 2021

@author: José Fernando Aquino Ruilova
"""

#*****************************************************************************
#* Universidad Nacional Abierta                                              *
#* Centro Local Aragua (04)                                                  *
#* Ingenieria de Sistemas (236)                                              *
#* Prácticas Profesionales II (341)                                          * 
#*                                                                           *
#*                                                                           *
#*                                                                           *
#*                    SISTEMA DE INTELIGENCIA ARTIFICIAL                     * 
#*                        PARA AUTOMATIZAR ASESORÍAS (V.2.14)                *
#*                                                                           *
#*                                                                           *
#*                                                                           *                        
#*                                                                           *
#*                                                                           *
#*                                                                           *
#*                                           Jose Fernando Aquino Ruilova    *    
#*                                                C.I. 7.253.181             *  
#*                                                                           *                      
#*                                                                           *
#***************************************************************************** 

#***************************** Bibliotecas ***********************************


from tkinter import Tk, Menu, Label, Button, PhotoImage, LEFT,ttk,\
                                              Canvas, filedialog as FileDialog                     
from tkinter.tix import *





# *************************** Variables globales *****************************

#  marco_configuración
#  marco_estados

#  modo
#  tarea
#  concepto 

#  modo_combo 
#  tarea_combo 
#  concepto_combo 

#  lienzo_respuesta_configuración
#  lienzo_diálogo_configuración

nro_diálogo = 0
contador_linea = 0
              
#**************************** FUNCIONES **************************************

def diálogo():
        
# Marco de diálogo

    global nro_diálogo
    global contador_linea
    contador_linea = 0
    nro_diálogo = nro_diálogo + 1 
    número = str(nro_diálogo)
    diálogo = 'DIÁLOGO ' + número
    global marco_diálogo    
    marco_diálogo = Canvas (ventana_base) 
    marco_diálogo.config(bg = 'darkgray' ,width = 630,height = 605)     
    marco_diálogo.place(x = 2, y = 36)
    Label(marco_diálogo, text = diálogo,bg ='darkgray',fg = 'black')\
                                                        .place(x = 20, y = 10)
    global botón_configurar_t    
    botón_configurar_t  = Button(marco_diálogo,  
                                      text = 'Configurar',command = configurar)
    botón_configurar_t.place(x = 555, y = 10)     
    global botón_destruir
    botón_destruir = Button(marco_diálogo,text = "X",
                                               command = cerrar_diálogo)
    global etiqueta_dialogar 
    etiqueta_dialogar = Label(marco_estados,image = imagen_dialogar)                                                          
    etiqueta_dialogar.place(x = 4 , y = 4 )
    global etiqueta_configurar_t 
    etiqueta_configurar_t = Label(marco_estados, text = 'Diálogo sin configuración')                                                          
    etiqueta_configurar_t.place(x = 35 , y = 8 )
    

# Lienzo del diálogo

    global lienzo_diálogo
                                                                                                                                                   
    lienzo_diálogo = Canvas (marco_diálogo)
    lienzo_diálogo.config(bg='black',width= 600,height= 545,bd = 5)     
    lienzo_diálogo.place(x= 10, y= 40)
    Label(lienzo_diálogo, text = 'VENTANA DE DIÁLOGO',bg = 'black',
                                      fg = 'green').place(x = 230, y = 10)
    neumabot('Hola! por favor configura el diálogo')
    
def cerrar_diálogo():
    global marco_diálogo, etiqueta_configurar_t
    marco_diálogo.destroy()
    etiqueta_configurar_t.destroy()
    etiqueta_dialogar.destroy()
     

def configurar():
    
    global botón_configurar_t
    botón_configurar_t.destroy()
    global etiqueta_dialogar
    etiqueta_dialogar.destroy()
    global etiqueta_configurar
    etiqueta_configurar = Label(marco_estados,image = imagen_configurar)
    etiqueta_configurar.place(x = 4 , y = 4 )
    global etiqueta_configurar_t 
    etiqueta_configurar_t.destroy()
    etiqueta_configurar_t = Label(marco_estados, text = 'Configurando...')                                                          
    etiqueta_configurar_t.place(x = 35 , y = 8 )
    global lienzo_configuración
    lienzo_configuración = Canvas (marco_diálogo)
    lienzo_configuración.config(bg='lightgray',width =610,height=110)  
    lienzo_configuración.place(x= 10, y= 40)     
    Label(lienzo_configuración,
    text='Seleccionar el modo, la tarea y el concepto sobre el cual se desea dialogar', 
                            bg = 'lightgray',fg = 'black').place(x = 10, y = 5)                                                                                        
    labelTop = Label(lienzo_configuración, 
                   text = "Seleccionar Modo", bg = 'lightgray',fg = 'black')                                                                
    labelTop.place(x = 10, y = 30)
    global modo_combo
    modo_combo = ttk.Combobox(lienzo_configuración,
                                          values=['asesoría', 'entrenamiento'])                                          
    modo_combo.place(x = 10, y = 50)    
    modo_combo.bind("<<ComboboxSelected>>",selección_modo)      
    
    labelTop = Label(lienzo_configuración, 
                   text = "Seleccionar tarea",bg = 'lightgray',fg = 'black')                                                                 
    labelTop.place(x = 160, y = 30)
    global tarea_combo
    tarea_combo = ttk.Combobox(lienzo_configuración,
                                       values=['configuración', 'diagnóstico'])                                        
    tarea_combo.place(x = 160, y = 50)   
    tarea_combo.bind("<<ComboboxSelected>>",selección_tarea)            
    
    labelTop = Label(lienzo_configuración,
                text ="Seleccionar concepto", bg = 'lightgray',fg = 'black')                                                                 
    labelTop.place(x = 310, y = 30)    
    global concepto_combo
    concepto_combo = ttk.Combobox(lienzo_configuración,
                                              values=['componente', 'sistema'])                                               
    concepto_combo.place(x = 310, y = 50)   
    concepto_combo.bind("<<ComboboxSelected>>",selección_concepto)
    global botón_aplicar
    botón_aplicar = Button(marco_diálogo, text = 'Aplicar',command = aplicar)                                     
                                                
def neumabot(palabras):
    
    global contador_linea     
    Label(lienzo_diálogo, text = 'Neumabot>>>', bg = 'black',
               fg = 'green').place(x = 10, y = 50 + 20*contador_linea)    
    Label(lienzo_diálogo, text = palabras,bg = 'black',
         fg = 'lightgreen').place(x = 100, y = 50 + 20*contador_linea)                         
    contador_linea = contador_linea + 1    

def usuario():
    
    global contador_linea
    Label(lienzo_diálogo, text = 'Usuario>>>', bg = 'black',
               fg = 'white').place(x = 10, y = 50 + 20*contador_linea)
    contador_linea = contador_linea + 1
    pass

def aplicar():
    
    global etiqueta_configurar
    etiqueta_configurar.destroy()
    global etiqueta_dialogar
    etiqueta_dialogar = Label(marco_estados,image = imagen_dialogar) 
    etiqueta_dialogar.place(x = 4 , y = 4 ) 
    selección = ['ok','ok','ok']
    if   modo_combo.get() == 'entrenamiento':
           modo = 'Se entrenará al bot'
    elif modo_combo.get() == 'asesoría':
           modo = 'Se asesorará al usuario'
    else:  
           selección[0] = 'nok'           
    if   tarea_combo.get() == 'diagnóstico':
           tarea = ' sobre el diagnóstico'
    elif tarea_combo.get() == 'configuración':
           tarea = ' sobre la configuración'
    else:
           selección[1] = 'nok'           
    if   concepto_combo.get() == 'sistema':
           concepto = ' de un sistema.'
    elif concepto_combo.get() == 'componente':           
           concepto = ' de un(a) '+ componente_combo.get()
    else: 
           selección[2] = 'nok'           
    print (selección)               
    if selección == ['ok','ok','ok']:           
     texto = modo+tarea+concepto
     Label(marco_diálogo, text = texto, 
                            bg = 'darkgray',fg = 'black').place(x = 90, y = 10)
     if modo_combo.get() == 'entrenamiento':       
        neumabot('Recibiré entrenamiento'+tarea+concepto)
        texto = 'Recibiendo entrenamiento'+tarea+concepto
        usuario()                                                  
        print('Función:',modo_combo.get())           
     if modo_combo.get() == 'asesoría':
        neumabot('Daré asesoría'+tarea+concepto)
        texto = 'Brindando asesoría'+tarea+concepto
        usuario()                
        print('Función:',modo_combo.get()) 
     global botón_aplicar
     botón_aplicar.destroy()  
     global botón_destruir
     botón_destruir.place(x = 600, y = 10)  
     print ('A dialogar en modo de', modo_combo.get() ) 
     lienzo_configuración.destroy()    
    else:
     Label(lienzo_configuración,
     text = 'Debe seleccionar todas las opciones antes de aplicar al diálogo', 
                           bg = 'lightgray',fg = 'black').place(x = 10, y = 80)
    global etiqueta_configurar_t 
    etiqueta_configurar_t.destroy()
    etiqueta_configurar_t = Label(marco_estados, text = texto)                                                          
    etiqueta_configurar_t.place(x = 35 , y = 8 ) 

def selección_concepto(event):

    print('selección de concepto',concepto_combo.get()) 
    if concepto_combo.get() == 'componente':       
       labelTop = Label(lienzo_configuración,
              text ="Seleccionar componente", bg = 'lightgray',fg = 'black')                                                                 
       labelTop.place(x = 460, y = 30)    
       global componente_combo
       componente_combo = ttk.Combobox(lienzo_configuración,
                   values=['accesorio', 'unidad de mtto','válvula','cilindro'])                                               
       componente_combo.place(x = 460, y = 50)   
       componente_combo.bind("<<ComboboxSelected>>",selección_componente)        
    if concepto_combo.get()== 'sistema':  
       selección_sistema()
           
def selección_componente(event):

    print('selección de componente',componente_combo.get())
    global botón_aplicar    
    botón_aplicar.place(x = 575, y = 10)

def selección_modo(event):

    print('selección del modo de',modo_combo.get())
        
def selección_sistema():
    print('selección de sistema')
    global botón_aplicar    
    botón_aplicar.place(x = 575, y = 10)

def selección_tarea(event):    
    print('selección de la tarea de',tarea_combo.get())
    
def salir_configuración():
    print('salir')

def abrir_diálogo():
    archivo = FileDialog.askopenfilename(title = 'Abrir diálogo')           
    print(archivo)
    
def guardar_diálogo():
     archivo = FileDialog.asksaveasfilename(title = 'Guardar diálogo como')
#    inputpath1 = FileDialog.inputpath.set(input_path)
     print(archivo)
     
def salir():
    ventana_base.destroy()
    pass
    
def acerca():
                                                                                                                                         
    marco_acerca = Canvas (ventana_base)
    marco_acerca.config(bg= 'lightgray',width=630 ,height=605)     
    marco_acerca.place(x = 637, y = 36)
    Label(marco_acerca, text= 'ACERCA DEL SISTEMA SEA NEUMÁTICA',bg = 'lightgray',
                                           fg = 'black').place(x = 20, y = 10)                                         
    Button(marco_acerca, text="X", command = marco_acerca.destroy).place(x = 605, y = 10)         
    lienzo = Canvas (marco_acerca)
    lienzo.config(bg='gray',width= 600,height= 545,bd = 5)     
    lienzo.place(x = 10, y= 40)
    Label(lienzo, text = 'XXXXXXXXXX',bg = 'gray',
                                        fg = 'black').place(x = 230, y = 10)

def documentación():
       
    marco_documentación = Canvas (ventana_base)
    marco_documentación.config(bg= 'lightgray',width =630 ,height =605)     
    marco_documentación.place(x = 637, y = 36)
    Label(marco_documentación, text= 'DOCUMENTACIÓN DEL SISTEMA SEA NEUMÁTICA',
          bg = 'lightgray',fg = 'black').place(x = 20, y = 10)                                                                                    
    Button(marco_documentación, text="X", command = marco_documentación.destroy).place(x = 605, y = 10) 
    
    lienzo = Canvas (marco_documentación)
    lienzo.config(bg='gray',width= 600,height = 545,bd = 5)     
    lienzo.place(x = 10, y = 40)
    Label(lienzo, text = 'XXXXXXXXXX',bg = 'gray',
                                        fg = 'black').place(x = 210, y = 10)

def configuración():
#   Por construir 
    pass

def diagnóstico():
#   Por construir 
    pass

def sistema():
#   Por construir 
    pass  

#***************************** Menú Principal ********************************

# Ventana base

ventana_base = Tk()
tip = Balloon(ventana_base) 
ventana_base.state('zoomed')
#ventana_base.resizable(0, 0)
ventana_base.iconbitmap('loto.ico')


ventana_base.title \
 ('SISTEMA EXPERTO EN ASESORÍA DE TECNOLOGÍA NEUMÁTICA (SEA Neumática V.2.14)')
 

menu_pricipal = Menu(ventana_base)
ventana_base.config(menu = menu_pricipal, bg = 'gray')

# Menu de diálogo

menu_de_diálogo = Menu(menu_pricipal, tearoff = 0)
menu_pricipal.add_cascade(label= 'Diálogo', men = menu_de_diálogo)
menu_de_diálogo.config(bg='lightgray')

imagen_nuevo = PhotoImage('Nuevo', file = 'nuevo.png')
menu_de_diálogo.add_command(label = 'Nuevo diálogo...',image = imagen_nuevo,
   compound = LEFT,command = diálogo, accelerator='Ctrl+N')
                                                                                                          
menu_de_diálogo.add_separator()
imagen_abrir = PhotoImage('Abrir', file = 'abrir.png')
menu_de_diálogo.add_command(label = 'Abrir...',image = imagen_abrir ,
                 compound = LEFT, command = abrir_diálogo,accelerator='Ctrl+A')                                                                                                                

menu_de_diálogo.add_separator()
imagen_guardar = PhotoImage('Guardar', file = 'guardar.png')
menu_de_diálogo.add_command(label = 'Guardar...', image = imagen_guardar,
                compound = LEFT,command = guardar_diálogo,accelerator='Ctrl+G')
                                                                                                                
menu_de_diálogo.add_separator()
imagen_salir = PhotoImage('Salir',file = 'salir.png')                                  
menu_de_diálogo.add_command(label = 'Salir...',image = imagen_salir,
                          compound = LEFT,command = salir,accelerator='Ctrl+S')

# Menu de ayuda

menu_de_ayuda = Menu(menu_pricipal, tearoff = 0)
menu_pricipal.add_cascade(label = "Ayuda", menu = menu_de_ayuda)
menu_de_ayuda.config(bg='lightgray')

imagen_acerca = PhotoImage('Acerca',file = 'acerca.png')
menu_de_ayuda.add_command(label = "Acerca de SEA Neumatica",
                        image = imagen_acerca,compound = LEFT,command = acerca)
menu_de_ayuda.add_separator()  
imagen_documento = PhotoImage('Documento',file = 'documento.png')                                                                                               
menu_de_ayuda.add_command(label = "Documentación SEA...",
              image = imagen_documento,compound = LEFT,command = documentación)

# Barra de herramientas

marco_herramientas = Canvas(ventana_base)
marco_herramientas.config(bg ='LightSteelBlue4',width=1361 ,height=30)     
marco_herramientas.place(x= 1, y = 1)
boton_salir = Button(marco_herramientas,image = imagen_salir, command = salir)                                          
boton_salir.place(x = 4, y = 4)
tip.bind_widget( boton_salir,balloonmsg = 'Salir del sistema')
boton_acerca = Button(marco_herramientas,image = imagen_acerca, 
                                                              command = acerca) 
boton_acerca.place(x = 32, y = 4)
tip.bind_widget(boton_acerca ,balloonmsg = 'Acerca del sistema SEA')

boton_documentación = Button(marco_herramientas,image = imagen_documento,
                                                       command = documentación) 
boton_documentación.place(x = 60, y = 4)
tip.bind_widget(boton_documentación ,balloonmsg = 'Documentación del sistema SEA')
boton_diálogo = Button(marco_herramientas,image = imagen_nuevo, 
                                                             command = diálogo) 
boton_diálogo.place(x = 88, y = 4)
tip.bind_widget(boton_diálogo,balloonmsg = 'Abre nuevo diálogo')
boton_abrir = Button(marco_herramientas,image = imagen_abrir,
                                                       command = abrir_diálogo) 
boton_abrir.place(x = 116, y = 4)
tip.bind_widget(boton_abrir,balloonmsg = 'Abre diálogo existente')
boton_guardar = Button(marco_herramientas,image = imagen_guardar, 
                                                     command = guardar_diálogo) 
boton_guardar.place(x = 144, y = 4) 
tip.bind_widget(boton_guardar ,balloonmsg = 'Guarda diálogo')


# Barra de estado

marco_estados = Canvas(ventana_base)
marco_estados.config(bg = 'LightSteelBlue4', width = 1361 , height = 33)     
marco_estados.place(x = 1, y = 646)
imagen_dialogar = PhotoImage('dialogar',file = 'dialogar.png')
imagen_configurar = PhotoImage('configurar',file = 'configurar.png')
                                                                                                       
ventana_base.mainloop()













