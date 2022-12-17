# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 13:14:31 2022

@author: José Fernando Aquino Ruilova
"""

# *****************************************************************************
# *                                                                           *
# *                                                                           *
# * Universidad Nacional Abierta                                              *
# * Centro Local Aragua (04)                                                  *
# * Ingenieria de Sistemas (236)                                              *
# * Practicas Profesionales II (341)                                          *
# *                                                                           *
# *                                                                           *
# *                                                                           *
# *                    SISTEMA DE INTELIGENCIA ARTIFICIAL                     *
# *                       PARA AUTOMATIZAR ASESORÍAS                          *
# *                               EN NEUMÁTICA                                *
# *                                                                           *
# *                                                                           *
# *                                                                           *
# *                                                                           *
# *                                                                           *
# *                                           José Fernando Aquino Ruilova    *
# *                                                C.I. 7.253.181             *
# *                                                                           *
# *                                                                           *
# *****************************************************************************

# Importación de modulos, paquetes y bibliotecas ******************************

# import aioxmpp Libreria Python de XMPP
from tkinter import Tk, Menu, Label, Button, PhotoImage, LEFT, ttk, Text,\
     Canvas, filedialog as FileDialog
from tkinter.tix import *

# Inicialización de Variables *************************************************

nro_dialogo = 0

# Definición de la clase Agente************************************************

"""
   Se crea el Agente que servirá de plantilla para el resto de los agentes
      Argumentos:
         jid (str): Identificador del agente de la forma username@server
         password (str): Contraseña para conectar al servidor
         verify_security (bool): Verificacion de certificado SSL
"""

print('Se crea la plantilla de Agente')


class Agente ():
    def __init__(self, jid: str, password: str, verify_security: bool = False):

        # *** Atributos del Agente ********************************************

        # self.jid = aioxmpp.JID.fromstr(jid)
        self.jid = jid
        self.password = password
        self.verify_security = verify_security

# * Tareas del Agente *********************************************************

    def solicita_servicio():

        global solicitud_servicio, tarea, concepto, componente_combo,\
               concepto_combo
        print('Tarea solicitar servicio')
        if concepto == 'componente':
            Aicomunicacion.prompt_nacabot('Dare asesoria'
                                          + tarea + concepto + ' '
                                          + componente_combo.get())
        else:
            Aicomunicacion.prompt_nacabot('Dare asesoria' + tarea + concepto)
            Aicomunicacion.prompt_nacabot('¿Tienes las características'''
                                          ' de lo que requieres?')
            Aicomunicacion.prompt_usuario()
            solicitud_servicio = ''
            return solicitud_servicio

    def recibe_solicitud(solicitud_servicio):
        global solicitud_recibida
        print('Recibiendo solicitud:')
        solicitud_recibida = solicitud_servicio
        print(solicitud_recibida)
        Nacabot.procesa_solicitud(solicitud_recibida)
        return solicitud_recibida

    def procesa_solicitud(solicitud_recibida):
        global solicitud_procesada, enter
        print('Procesando solicitud usando técnicas de PLN')

        # Preprocesamiento o normalizacón de la solicitud
        global minusculas, oraciones, palabras, no_funcionales, no_ruidosas
        global no_paradas, derivadas, lemantizadas, etiquetadas, reconocidas

        Nacabot.minusculiza(solicitud_recibida)
        Nacabot.tokeniza_palabras(minusculas)
        Nacabot.elimina_funcionales(palabras)
        Nacabot.elimina_ruido(no_funcionales)
        Nacabot.deriva(no_ruidosas)
        Nacabot.lemantiza(derivadas)
        Nacabot.etiqueta(lemantizadas)
        Nacabot.reconoce_entidad(etiquetadas)
        Nacabot.tokeniza_oraciones(reconocidas)

        solicitud_procesada = "*****Solicitud procesada*****"
        print(solicitud_procesada)
        enter.destroy()
        return solicitud_procesada

    def procesa_asesoria(solicitud_procesada):
        global asesoria_procesada
        print('Asesorando')
        print('----> decir - preguntar - accionar')
        return asesoria_procesada

    def valida_asesoria(asesoria_procesada):
        global asesoria_validada
        print('Valorando la capacidad de asesoría')
        return asesoria_validada

    def prepara_asesoria(asesoria_validada):
        global asesoria_preparada, servicio_preparado
        print('preparando la asesoría')
        print('----> decir - preguntar - accionar')
        print('preparando el servicio')
        servicio_preparado = asesoria_preparada
        return servicio_preparado

    def experto_asesora(asesoria_validada):
        global asesoria_experto
        print('Experto asesorando')
        return asesoria_experto

    def Procesa_entrenamiento(solicitud_procesada):
        global entrenamiento_procesado
        print('Entrenando')
        print('----> decir - preguntar - accionar')
        return entrenamiento_procesado

    def valida_entrenamiento(entrenamiento_procesado):
        global entrenamiento_validado
        print('Valorando la capacidad de entrenamiento')
        return entrenamiento_validado

    def prepara_entrenamiento(entrenamiento_validado):
        global entrenamiento_preparado, servicio_preparado
        print('preparando el entrenamiento')
        print('----> decir - preguntar - accionar')
        print('preparando el servicio')
        servicio_preparado = entrenamiento_preparado
        return servicio_preparado

    def experto_entrena(entrenamiento_validado):
        global entrenamiento_experto
        print('Experto entrenando')
        return entrenamiento_experto

    def procesa_servicio(servicio_preparado):
        global servicio_procesado
        print('Procesando servicio')
        print('----> decir - preguntar - accionar')
        return servicio_procesado

    def entrega_servicio(servicio_procesado):
        global servicio_entregado
        print('entregando servicio')
        return servicio_entregado

    def recibe_servicio(servicio_entregado):
        global servicio_recibido
        print('Recibiendo servicio')
        return servicio_recibido

# * Sub-Tareas de la interfaz de comunicación *********************************

    def prompt_nacabot(palabras):

        global contador_linea, lienzo_dialogo
        Label(lienzo_dialogo, text='NACABot>>>', bg='black',
              fg='green').place(x=10, y=50 + 20*contador_linea)
        Label(lienzo_dialogo, text=palabras, bg='black',
              fg='lightgreen').place(x=100, y=50 + 20*contador_linea)
        contador_linea = contador_linea + 1

    def prompt_usuario():

        global contador_linea, texto_usuario, enter, lienzo_dialogo
        Label(lienzo_dialogo, text='Usuario>>>', bg='black',
              fg='lightblue').place(x=10, y=50 + 20*contador_linea)
        texto_usuario = Text(lienzo_dialogo, width=56, height=1, fg='black',
                             bg='lightblue')
        texto_usuario.place(x=100, y=50 + 20*contador_linea)
        enter = Button(lienzo_dialogo, text='Enter', bg='lightblue',
                       fg='black',
                       command=Aicomunicacion.obtiene_entrada)
        enter.place(x=555, y=50 + 20*contador_linea)
        contador_linea = contador_linea + 1

    def obtiene_entrada():
        global texto_usuario, solicitud_servicio
        solicitud_servicio = texto_usuario.get("1.0", "end")
        print('Se obtiene solicitud de servicio:')
        print(solicitud_servicio)
        Aicomunicacion.recibe_solicitud(solicitud_servicio)

    def inicia_dialogo():

        # Marco de diálogo

        global nro_dialogo
        global contador_linea
        contador_linea = 0
        nro_dialogo = nro_dialogo + 1
        número = str(nro_dialogo)
        dialogo = 'Diálogo ' + número
        global marco_dialogo
        marco_dialogo = Canvas(ventana_base)
        marco_dialogo.config(bg='darkgray', width=630, height=605)
        marco_dialogo.place(x=2, y=36)
        Label(marco_dialogo, text=dialogo, bg='darkgray', fg='black')\
            .place(x=20, y=10)
        global boton_configurar_t
        boton_configurar_t = Button(marco_dialogo,
                                    text='Configurar',
                                    command=Aicomunicacion.configura)
        boton_configurar_t.place(x=555, y=10)
        global boton_destruir
        boton_destruir = Button(marco_dialogo, text="X",
                                command=Aicomunicacion.cierra_dialogo)
        global etiqueta_dialogar
        etiqueta_dialogar = Label(marco_estados, image=imagen_dialogar)
        etiqueta_dialogar.place(x=4, y=4)
        global etiqueta_configurar_t
        etiqueta_configurar_t = \
            Label(marco_estados, text='Dialogando sin configuración...')
        etiqueta_configurar_t.place(x=35, y=8)

        # Lienzo del diálogo

        global lienzo_dialogo

        lienzo_dialogo = Canvas(marco_dialogo)
        lienzo_dialogo.config(bg='black', width=600, height=545, bd=5)
        lienzo_dialogo.place(x=10, y=40)
        Label(lienzo_dialogo, text='VENTANA DE DIÁLOGO', bg='black',
              fg='green').place(x=230, y=10)
        Aicomunicacion.prompt_nacabot('Hola! por favor configura '''
                                      'el diálogo')

    def cierra_dialogo():
        global marco_dialogo, etiqueta_configurar_t
        marco_dialogo.destroy()
        etiqueta_configurar_t.destroy()
        etiqueta_dialogar.destroy()

    def configura():

        global boton_configurar_t
        boton_configurar_t.destroy()
        global etiqueta_dialogar
        etiqueta_dialogar.destroy()
        global etiqueta_configurar
        etiqueta_configurar = Label(marco_estados, image=imagen_configurar)
        etiqueta_configurar.place(x=4, y=4)
        global etiqueta_configurar_t
        etiqueta_configurar_t.destroy()
        etiqueta_configurar_t = Label(marco_estados,
                                      text='Configurando diálogo...')
        etiqueta_configurar_t.place(x=35, y=8)
        global lienzo_configuracion
        lienzo_configuracion = Canvas(marco_dialogo)
        lienzo_configuracion.config(bg='lightgray', width=610, height=110)
        lienzo_configuracion.place(x=10, y=40)
        Label(lienzo_configuracion, text='Seleccionar el objetivo del '''
              'diálogo; la tarea y el concepto sobre el cual se desea '''
              'dialogar.',
              bg='lightgray', fg='black').place(x=10, y=5)
        labelTop = Label(lienzo_configuracion,
                         text="Seleccionar objetivo", bg='lightgray',
                         fg='black')
        labelTop.place(x=10, y=30)
        global objetivo_combo
        objetivo_combo = ttk.Combobox(lienzo_configuracion,
                                      values=['asesoria', 'entrenamiento'])
        objetivo_combo.place(x=10, y=50)
        objetivo_combo.bind("<<ComboboxSelected>>",
                            Aicomunicacion.selecciona_objetivo)
        labelTop = Label(lienzo_configuracion,
                         text="Seleccionar tarea", bg='lightgray',
                         fg='black')
        labelTop.place(x=160, y=30)
        global tarea_combo
        tarea_combo = ttk.Combobox(lienzo_configuracion,
                                   values=['configuracion', 'diagnostico'])
        tarea_combo.place(x=160, y=50)
        tarea_combo.bind("<<ComboboxSelected>>",
                         Aicomunicacion.selecciona_tarea)
        labelTop = Label(lienzo_configuracion,
                         text="Seleccionar concepto", bg='lightgray',
                         fg='black')
        labelTop.place(x=310, y=30)
        global concepto_combo
        concepto_combo = ttk.Combobox(lienzo_configuracion,
                                      values=['componente', 'sistema'])
        concepto_combo.place(x=310, y=50)
        concepto_combo.bind("<<ComboboxSelected>>",
                            Aicomunicacion.selecciona_concepto)
        global boton_aplicar
        boton_aplicar = Button(marco_dialogo, text='Aplicar',
                               command=Aicomunicacion.aplica)

    def selecciona_concepto(event):

        print('selección del concepto', concepto_combo.get())
        if concepto_combo.get() == 'componente':
            labelTop = Label(lienzo_configuracion,
                             text="Seleccionar componente",
                             bg='lightgray', fg='black')
            labelTop.place(x=460, y=30)
            global componente_combo
            componente_combo = ttk.Combobox(lienzo_configuracion,
                                            values=['accesorio',
                                                    'unidad de mtto',
                                                    'valvula', 'cilindro'])
            componente_combo.place(x=460, y=50)
            componente_combo.bind("<<ComboboxSelected>>",
                                  Aicomunicacion.selecciona_componente)
        if concepto_combo.get() == 'sistema':
            Aicomunicacion.selecciona_sistema()

    def selecciona_componente(event):

        print('selección del componente', componente_combo.get())
        global boton_aplicar
        boton_aplicar.place(x=575, y=10)

    def selecciona_objetivo(event):

        print('selección del objetivo de', objetivo_combo.get())

    def selecciona_sistema():
        print('selección de sistema')
        global boton_aplicar
        boton_aplicar.place(x=575, y=10)

    def selecciona_tarea(event):
        print('selección de la tarea de', tarea_combo.get())

    def aplica():

        global tarea
        global concepto
        global texto
        global etiqueta_configurar
        etiqueta_configurar.destroy()
        global etiqueta_dialogar
        etiqueta_dialogar = Label(marco_estados, image=imagen_dialogar)
        etiqueta_dialogar.place(x=4, y=4)
        seleccion = ['ok', 'ok', 'ok']
        if objetivo_combo.get() == 'entrenamiento':
            objetivo = 'Se entrenará al usuario xxx'
        elif objetivo_combo.get() == 'asesoria':
            objetivo = 'Se asesorará al usuario xxx'
        else:
            seleccion[0] = 'nok'
        if tarea_combo.get() == 'diagnostico':
            tarea = ' sobre el diagnostico'
        elif tarea_combo.get() == 'configuracion':
            tarea = ' sobre la configuracion'
        else:
            seleccion[1] = 'nok'
        if concepto_combo.get() == 'sistema':
            concepto = ' de un sistema.'
        elif concepto_combo.get() == 'componente':
            concepto = ' del'+' componente'
        else:
            seleccion[2] = 'nok'

        print(seleccion)

        if seleccion == ['ok', 'ok', 'ok']:
            if concepto_combo.get() != 'sistema':
                texto = objetivo+tarea+concepto+' '+componente_combo.get()
            else:
                texto = objetivo+tarea+concepto
            Label(marco_dialogo, text=texto,
                  bg='darkgray', fg='black').place(x=90, y=10)
        if objetivo_combo.get() == 'entrenamiento':
            texto = 'Recibiendo entrenamiento'+tarea+concepto
        if objetivo_combo.get() == 'asesoria':
            if concepto_combo.get() != 'sistema':
                texto = 'Brindando asesoria' + tarea + concepto + ' '\
                                             + componente_combo.get()
            else:
                texto = 'Brindando asesoria' + tarea + concepto
        else:
            Label(lienzo_configuracion, text='Debe seleccionar todas '''
                  'las opciones antes de aplicar al diálogo',
                  bg='lightgray', fg='black').place(x=10, y=80)
        global boton_aplicar
        boton_aplicar.destroy()
        global boton_destruir
        boton_destruir.place(x=600, y=10)
        print('A dialogar con el objetivo de', objetivo_combo.get())
        lienzo_configuracion.destroy()
        global etiqueta_configurar_t
        etiqueta_configurar_t.destroy()
        etiqueta_configurar_t = Label(marco_estados, text=texto)
        etiqueta_configurar_t.place(x=35, y=8)
        Aicomunicacion.solicita_servicio()

    def sale_configuracion():  # no se usa, por que?
        print('salir')

    def abre_dialogo():
        archivo = FileDialog.askopenfilename(title='Abrir diálogo')
        print(archivo)

    def guarda_dialogo():
        archivo = FileDialog.asksaveasfilename(title='Guardar'''
                                               'diálogo como')
    #    inputpath1 = FileDialog.inputpath.set(input_path)
        print(archivo)

    def sale():
        ventana_base.destroy()

    def acerca():

        marco_acerca = Canvas(ventana_base)
        marco_acerca.config(bg='lightgray', width=630, height=605)
        marco_acerca.place(x=637, y=36)
        Label(marco_acerca, text='ACERCA DE SEA NEUMÁTICA',
              bg='lightgray', fg='black').place(x=20, y=10)
        Button(marco_acerca, text="X",
               command=marco_acerca.destroy).place(x=605, y=10)
        lienzo = Canvas(marco_acerca)
        lienzo.config(bg='gray', width=600, height=545, bd=5)
        lienzo.place(x=10, y=40)
        Label(lienzo, text='XXXXXXXXXX', bg='gray',
              fg='black').place(x=230, y=10)

    def documentacion():

        marco_documentacion = Canvas(ventana_base)
        marco_documentacion.config(bg='lightgray', width=630, height=605)
        marco_documentacion.place(x=637, y=36)
        Label(marco_documentacion, text='DOCUMENTACIÓN DE SEA NEUMÁTICA',
              bg='lightgray', fg='black').place(x=20, y=10)
        Button(marco_documentacion, text="X",
               command=marco_documentacion.destroy).place(x=605, y=10)

        lienzo = Canvas(marco_documentacion)
        lienzo.config(bg='gray', width=600, height=545, bd=5)
        lienzo.place(x=10, y=40)
        Label(lienzo, text='XXXXXXXXXX', bg='gray',
              fg='black').place(x=210, y=10)

# Sub-Tareas PLN **************************************************************

    # Preprocesamiento

    def minusculiza(solicitud_recibida):
        global minusculas
        print('minusculiza palabras')
        minusculas = solicitud_recibida.lower()
        print('minusculas = ', minusculas)
        return minusculas

    def tokeniza_palabras(minusculas):
        global palabras
        print('Tokeniza en palabras')
#        palabras = nltk.word_tokenize(minusculas, "spanish")

        print('palabras = ', palabras)
        return palabras

    def elimina_funcionales(palabras):
        global no_funcionales
        print('Elimina palabras funcionales')
        # Se carga corpus de palabras funcionales
#        palabras_funcionales = nltk.corpus.stopwords.words("spanish")
        # Transforma a string para poder ser usada por tokenize
#        palabras = nltk.word_tokenize(" ".join(palabras), "spanish")
        no_funcionales = []
        for token in palabras:
            if token not in palabras_funcionales:
                no_funcionales.append(token)
        print('no_funcionales = ', no_funcionales)
        return no_funcionales

    def elimina_ruido(no_funcionales):
        global no_ruidosas
        print('Elimina el ruido')
        no_ruidosas = no_funcionales
        print('no_ruidosas = ', no_ruidosas)
        return no_ruidosas

    def deriva(no_ruidosas):
        global derivadas
        print('Deriva palabras')
        derivadas = no_ruidosas
        print('derivadas = ', derivadas)
        return derivadas

    def lemantiza(derivadas):
        global lemantizadas
        print('Lemantiza palabras')
        lemantizadas = derivadas
        print('lemantizadas = ', lemantizadas)
        return lemantizadas

    def etiqueta(lemantizadas):
        global etiquetadas
        print('Etiqueta palabras')
        etiquetadas = lemantizadas
        print('etiquetadas = ', etiquetadas)
        return etiquetadas

    def reconoce_entidad(etiquetadas):
        global reconocidas
        print('Reconoce palabras')
        reconocidas = etiquetadas
        print('reconocidas = ', reconocidas)
        return reconocidas

    def tokeniza_oraciones(reconocidas):
        global oraciones
        print('Tokeniza en oraciones')
#        oraciones = nltk.sent_tokenize(" ".join(reconocidas), "spanish")
        print('oraciones = ', oraciones)
        return oraciones

# Definición del agente interfaz de usuario **********************************


print('Se crea el agente interfaz de usuario')


class Aicomunicacion(Agente):

    def __init__(self):
        pass


# Definición del agente interfaz de cliente ***********************************

print('Se crea el agente interfaz de cliente')


class Aicliente(Aicomunicacion):
    def __init__(self):
        pass


# Definición del agente interfaz de técnico ***********************************

print('Se crea el agente interfaz de técnico')


class Aitecnico(Aicomunicacion):
    def __init__(self):
        pass


# Definición del agente interfaz de experto ***********************************

print('Se crea el agente interfaz de experto')


class Aiexperto(Aicomunicacion):
    def __init__(self):
        pass


# Definición del agente Nacabot ***********************************************

print('Se crea el agente Nacabot')


class Nacabot(Agente):
    def __init__(self):
        pass


# Definición del agente interfaz de la base de conocimiennto ******************

print('Se crea el agente interfaz de la base de conocimiennto')


class Aibc(Agente):
    def __init__(self):
        pass


# Bloque principal ************************************************************

# * Ventana de la interfaz de comunicación ************************************

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

imagen_nuevo = PhotoImage('Nuevo', file='.\\imagenes_sea\\nuevo.png')
menu_de_dialogo.add_command(label='Nuevo...', image=imagen_nuevo,
                            compound=LEFT,
                            command=Aicomunicacion.inicia_dialogo,
                            accelerator='Ctrl+N')

menu_de_dialogo.add_separator()
imagen_abrir = PhotoImage('Abrir', file='.\\imagenes_sea\\abrir.png')
menu_de_dialogo.add_command(label='Abrir...', image=imagen_abrir,
                            compound=LEFT,
                            command=Aicomunicacion.abre_dialogo,
                            accelerator='Ctrl+A')

menu_de_dialogo.add_separator()
imagen_guardar = PhotoImage('Guardar', file='.\\imagenes_sea\\guardar.png')
menu_de_dialogo.add_command(label='Guardar...', image=imagen_guardar,
                            compound=LEFT,
                            command=Aicomunicacion.guarda_dialogo,
                            accelerator='Ctrl+G')

menu_de_dialogo.add_separator()
imagen_salir = PhotoImage('Salir', file='.\\imagenes_sea\\salir.png')
menu_de_dialogo.add_command(label='Salir...', image=imagen_salir,
                            compound=LEFT, command=Aicomunicacion.sale,
                            accelerator='Ctrl+S')

# Menu de ayuda

menu_de_ayuda = Menu(menu_pricipal, tearoff=0)
menu_pricipal.add_cascade(label="Ayuda", menu=menu_de_ayuda)
menu_de_ayuda.config(bg='lightgray')

imagen_acerca = PhotoImage('Acerca', file='.\\imagenes_sea\\acerca.png')
menu_de_ayuda.add_command(label="Acerca de SEA Neumatica",
                          image=imagen_acerca, compound=LEFT,
                          command=Aicomunicacion.acerca)
menu_de_ayuda.add_separator()
imagen_documento = PhotoImage('Documento',
                              file='.\\imagenes_sea\\documento.png')
menu_de_ayuda.add_command(label="Documentacion SEA...",
                          image=imagen_documento,
                          compound=LEFT, command=Aicomunicacion.documentacion)

# Barra de herramientas

marco_herramientas = Canvas(ventana_base)
marco_herramientas.config(bg='LightSteelBlue4', width=1361, height=30)
marco_herramientas.place(x=1, y=1)
boton_salir = Button(marco_herramientas, image=imagen_salir,
                     command=Aicomunicacion.sale)
boton_salir.place(x=4, y=4)
tip.bind_widget(boton_salir, balloonmsg='Salir del sistema')
boton_acerca = Button(marco_herramientas, image=imagen_acerca,
                      command=Aicomunicacion.acerca)
boton_acerca.place(x=32, y=4)
tip.bind_widget(boton_acerca, balloonmsg='Acerca del sistema SEA')

boton_documentacion = Button(marco_herramientas,
                             image=imagen_documento,
                             command=Aicomunicacion.documentacion)
boton_documentacion.place(x=60, y=4)
tip.bind_widget(boton_documentacion,
                balloonmsg='Documentacion del sistema SEA')
boton_dialogo = Button(marco_herramientas, image=imagen_nuevo,
                       command=Aicomunicacion.inicia_dialogo)
boton_dialogo.place(x=88, y=4)
tip.bind_widget(boton_dialogo, balloonmsg='Abre nuevo diálogo')
boton_abrir = Button(marco_herramientas, image=imagen_abrir,
                     command=Aicomunicacion.abre_dialogo)
boton_abrir.place(x=116, y=4)
tip.bind_widget(boton_abrir, balloonmsg='Abre diálogo existente')
boton_guardar = Button(marco_herramientas, image=imagen_guardar,
                       command=Aicomunicacion.guarda_dialogo)
boton_guardar.place(x=144, y=4)
tip.bind_widget(boton_guardar, balloonmsg='Guarda diálogo')

# Barra de estado

marco_estados = Canvas(ventana_base)
marco_estados.config(bg='LightSteelBlue4', width=1361, height=33)
marco_estados.place(x=1, y=646)
imagen_dialogar = PhotoImage('dialogar',
                             file='.\\imagenes_sea\\dialogar.png')
imagen_configurar = PhotoImage('configurar',
                               file='.\\imagenes_sea\\configurar.png')

ventana_base.mainloop()
