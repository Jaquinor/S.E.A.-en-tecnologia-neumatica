from rasa_sdk import Action
from tkinter import Tk, Menu, Label, Button, PhotoImage, LEFT, ttk, Text,\
     Canvas, filedialog as FileDialog
from tkinter.tix import *


# Inicio *********************************************************************

class ActionIniciar(Action):

  def name(self):
      return "action_iniciar"


  def run(self, dispatcher, tracker, domain):        
      dispatcher.utter_message(text="iniciando...")
      print("iniciando proceso")
      return
      
# Creación de los Agentes*****************************************************

class Agente(Action):

  def name(self):
      return "action_crear_agente"

  def run(self, dispatcher,tracker, domain):
      dispatcher.utter_message(text="Se crean los agentes:")
      print('Se crean los agentes:')

# Creación del agente interfaz cliente****************************************

      class icliente(Agente):
        def __init__(self):
          pass
      dispatcher.utter_message(text="icliente")
      print("icliente")
      
# Creación del agente interfaz técnico****************************************

      class iasesor(Agente):
        def __init__(self):
          pass
      dispatcher.utter_message(text="itecnico")
      print("itecnico")
  
# Creación del agente interfaz experto****************************************

      class iexperto(Agente):
        def __init__(self):
          pass
      dispatcher.utter_message(text="iexperto")
      print("iexperto")

# Creación del agente interfaz base conocimiento neumatica *******************

      class bcneumatica(Agente):
        def __init__(self):
          pass
      dispatcher.utter_message(text="bcneumatica")
      print("bcneumatica") 

# Creación del agente naca bot************************************************

      class nacabot(Agente):
        def __init__(self):
          pass
      dispatcher.utter_message(text="nacabot")
      print("nacabot")
      
      return
    
# Creación Ventana base*******************************************************

class CreaVentanaBase(Action):

  def name(self):
      return "action_crear_ventana_base"

  def run(self, dispatcher, tracker, domain):        
      dispatcher.utter_message(text="crea ventana base")
      print("crea ventana base")

      # Ventana base
      ventana_base = Tk()
      tip = Balloon(ventana_base)
      ventana_base.state('zoomed')
      ventana_base.geometry('750x750+200+1')
      
      # ventana_base.geometry('750x700+200+1')
      ventana_base.iconbitmap('.\\imagenes_sea\\loto.ico')
      ventana_base.title('SISTEMA EXPERTO EN ASESORÍA DE TECNOLOGÍA'''
                         ' NEUMÁTICA (SEA Neumática)')
      menu_pricipal = Menu(ventana_base)
      ventana_base.config(menu=menu_pricipal, bg='gray')
      # Menu de diálogo

      menu_de_dialogo = Menu(menu_pricipal, tearoff=0)
      menu_pricipal.add_cascade(label='Diálogo', men=menu_de_dialogo)
      menu_de_dialogo.config(bg='lightgray')

      imagen_nuevo = PhotoImage('Nuevo', 
                                 file='C:\\Users\\aquin\\Proyectos_SEA\\pruebas\\5-interfaz_usuario\\imagenes_sea\\nuevo.png')
      menu_de_dialogo.add_command(label='Nuevo...', image=imagen_nuevo,
                                  compound=LEFT,
#                                  command=icomunicacion.inicia_dialogo,
                                  accelerator='Ctrl+N')

      menu_de_dialogo.add_separator()
      imagen_abrir = PhotoImage('Abrir', file='C:\\Users\\aquin\\Proyectos_SEA\\pruebas\\5-interfaz_usuario\\imagenes_sea\\abrir.png')
      menu_de_dialogo.add_command(label='Abrir...', image=imagen_abrir,
                                  compound=LEFT,
#                                  command=Aicomunicacion.abre_dialogo,
                                  accelerator='Ctrl+A')

      menu_de_dialogo.add_separator()
      imagen_guardar = PhotoImage('Guardar', file='C:\\Users\\aquin\\Proyectos_SEA\\pruebas\\5-interfaz_usuario\\imagenes_sea\\guardar.png')
      menu_de_dialogo.add_command(label='Guardar...', image=imagen_guardar,
                                  compound=LEFT,
#                                  command=Aicomunicacion.guarda_dialogo,
                                  accelerator='Ctrl+G')

      menu_de_dialogo.add_separator()
      imagen_salir = PhotoImage('Salir', file='C:\\Users\\aquin\\Proyectos_SEA\\pruebas\\5-interfaz_usuario\\imagenes_sea\\salir.png')
      menu_de_dialogo.add_command(label='Salir...', image=imagen_salir,
                                  compound=LEFT, 
#                                  command=Aicomunicacion.sale,
                                  accelerator='Ctrl+S')

      # Menu de ayuda

      menu_de_ayuda = Menu(menu_pricipal, tearoff=0)
      menu_pricipal.add_cascade(label="Ayuda", menu=menu_de_ayuda)
      menu_de_ayuda.config(bg='lightgray')

      imagen_acerca = PhotoImage('Acerca', file='C:\\Users\\aquin\\Proyectos_SEA\\pruebas\\5-interfaz_usuario\\imagenes_sea\\acerca.png')
      menu_de_ayuda.add_command(label="Acerca de SEA Neumatica",
                                image=imagen_acerca, 
                                compound=LEFT,
#                                command=Aicomunicacion.acerca
                                )
      menu_de_ayuda.add_separator()
      imagen_documento = PhotoImage('Documento',
                                    file='C:\\Users\\aquin\\Proyectos_SEA\\pruebas\\5-interfaz_usuario\\imagenes_sea\\documento.png')
      menu_de_ayuda.add_command(label="Documentacion SEA...",
                                image=imagen_documento,
                                compound=LEFT, 
#                                command=Aicomunicacion.documentacion
                                )

      # Barra de herramientas

      marco_herramientas = Canvas(ventana_base)
      marco_herramientas.config(bg='LightSteelBlue4', width=1361, height=30)
      marco_herramientas.place(x=1, y=1)
      boton_salir = Button(marco_herramientas, image=imagen_salir,
#                           command=Aicomunicacion.sale
                           )
      boton_salir.place(x=4, y=4)
      tip.bind_widget(boton_salir, balloonmsg='Salir del sistema')
      boton_acerca = Button(marco_herramientas, image=imagen_acerca,
#                            command=Aicomunicacion.acerca
                            )
      boton_acerca.place(x=32, y=4)
      tip.bind_widget(boton_acerca, balloonmsg='Acerca del sistema SEA')

      boton_documentacion = Button(marco_herramientas,
                                   image=imagen_documento,
#                                   command=Aicomunicacion.documentacion
                                   )
      boton_documentacion.place(x=60, y=4)
      tip.bind_widget(boton_documentacion,
                      balloonmsg='Documentacion del sistema SEA')
      boton_dialogo = Button(marco_herramientas, image=imagen_nuevo,
#                             command=Aicomunicacion.inicia_dialogo
                             )
      boton_dialogo.place(x=88, y=4)
      tip.bind_widget(boton_dialogo, balloonmsg='Abre nuevo diálogo')
      boton_abrir = Button(marco_herramientas, image=imagen_abrir,
#                           command=Aicomunicacion.abre_dialogo
                           )
      boton_abrir.place(x=116, y=4)
      tip.bind_widget(boton_abrir, balloonmsg='Abre diálogo existente')
      boton_guardar = Button(marco_herramientas, image=imagen_guardar,
#                             command=Aicomunicacion.guarda_dialogo
                             )
      boton_guardar.place(x=144, y=4)
      tip.bind_widget(boton_guardar, balloonmsg='Guarda diálogo')

      # Barra de estado

      marco_estados = Canvas(ventana_base)
      marco_estados.config(bg='LightSteelBlue4', width=1361, height=33)
      marco_estados.place(x=1, y=646)
      imagen_dialogar = PhotoImage('dialogar',
                                   file='C:\\Users\\aquin\\Proyectos_SEA\\pruebas\\5-interfaz_usuario\\imagenes_sea\\dialogar.png')
      imagen_configurar = PhotoImage('configurar',
                                     file='C:\\Users\\aquin\\Proyectos_SEA\\pruebas\\5-interfaz_usuario\\imagenes_sea\\configurar.png')
      
      ventana_base.mainloop()
      
      return    
 

    
  
    

