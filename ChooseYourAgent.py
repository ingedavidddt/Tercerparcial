# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 20:53:29 2023

@author: david
"""
import tkinter as tk
global cuadro_resultado

cuadro_opciones = None
cuadro_resultado = None
cuadro_agentes = None
cuadro_Habilidades = None









# Preguntas adicionales con opciones predefinidas
preguntas_iniciales = [
    "¿Prefieres jugar de manera agresiva, buscando enfrentamientos directos,\n o te inclinas más hacia un enfoque táctico y de apoyo?",
    "¿Te sientes más cómodo liderando ataques, defendiendo zonas, recopilando \ninformación o eliminando enemigos en duelos?",
    "¿Te gustaría tener habilidades que bloqueen la visión del enemigo, controlen \nel campo de batalla, obtengan información o desorganizen a tus oponentes?",
    "¿Prefieres armas de corto alcance para enfrentamientos cercanos o armas de \nlargo alcance para tiroteos a distancia?",
    "¿Te gusta planificar estrategias con tu equipo o prefieres tomar decisiones \nrápidas y adaptarte sobre la marcha?",
    "¿Te sientes más cómodo liderando el equipo, siguiendo las instrucciones de \notros o trabajando de manera independiente?",
    "¿Tienes experiencia en otros juegos de disparos tácticos o en juegos que \nrequieren habilidades estratégicas?",
    
]

# Opciones predefinidas para cada pregunta
opciones_preguntas = [
    ["Agresiva", "Táctica"],
    ["Liderando ataques", "Defendiendo zonas", "Recopilando información", "Eliminando enemigos en duelos"],
    ["Bloquear visión", "Controlar campo de batalla", "Obtener información", "Desorganizar oponentes"],
    ["Corto alcance", "Largo alcance"],
    ["Planificar estrategias", "Tomar decisiones rápidas", "Adaptarse sobre la marcha"],
    ["Liderar equipo", "Seguir instrucciones", "Trabajar de manera independiente"],
    ["Sí", "No"]
   
]

respuestas = []

roles_disponibles = ["Controlador", "Duelista", "Centinela", "Iniciador"]

funciones_roles = {
    "Controlador": "Agentes diseñados para controlar el campo de batalla, proporcionando utilidades que bloquean la visión del enemigo y controlan el espacio",
    "Duelista": "Agentes especializados en el combate directo y la eliminación de enemigos. Tienen habilidades que les permiten enfrentarse en duelos individuales",
    "Centinela": "Agentes encargados de la vigilancia y la obtención de información. Sus habilidades se centran en la detección de enemigos y la creación de un área segura",
    "Iniciador": "Agentes que lideran el ataque, abriendo oportunidades para el equipo y desorganizando al enemigo. Suelen tener habilidades de reconocimiento y disturbio"
}

Rol_Determinado = []


agentes = {
    'Brimstone': {
        'Rol': 'Controlador',
        'Habilidades': ['Incendiario', 'Estimulante', 'Cielo de Fuego', 'Estela Orbital']
    },
    'Jett': {
        'Rol': 'Duelista',
        'Habilidades': ['Corriente Ascendente', 'Corte de Viento', 'Ráfaga de Ráfagas', 'Tormenta de Cuchillas']
    },
    'Phoenix': {
        'Rol': 'Duelista',
        'Habilidades': ['Ronda Caliente', 'Muro de Fuego', 'Estímulo', 'Ráfaga Curva']
    },
    'Sage': {
        'Rol': 'Centinela',
        'Habilidades': ['Estimulante', 'Orbe Curativo', 'Muro de Hielo', 'Resurrección']
    },
    'Sova': {
        'Rol': 'Iniciador',
        'Habilidades': ['Flecha de Choque', 'Flecha de Rastreo', 'Drone de Observación', 'Flecha Deslizante']
    },
    'Breach': {
        'Rol': 'Iniciador',
        'Habilidades': ['Sismos', 'Carga Ciega', 'Falla', 'Temblor']
    },
    'Cypher': {
        'Rol': 'Centinela',
        'Habilidades': ['Cámara de Vigilancia', 'Trampa de Cables', 'Trampa de Asedio Neural', 'Afinación del Espionaje']
    },
    'Omen': {
        'Rol': 'Controlador',
        'Habilidades': ['Ceguera Paranoica', 'Teletransporte Sombrío', 'Cubrimiento Tenebroso', 'Paranoia'
        ]
    },
    'Raze': {
        'Rol': 'Duelista',
        'Habilidades': ['Bomba de Carga', 'Granada Cluster', 'Pintura con Explosivos', 'Showstopper']
    },
    'Viper': {
        'Rol': 'Controladora',
        'Habilidades': ['Poison Cloud', 'Cóctel de Humo', 'Pitón', 'Víbora Embrujada']
    },
    'Reyna': {
        'Rol': 'Duelista',
        'Habilidades': ['Desgarro Devorador', 'Orbe Deslumbrante', 'Anulación Lejana', 'Eco Espeluznante']
    },
    'Killjoy': {
        'Rol': 'Centinela',
        'Habilidades': ['Torreta Nanoenjambre', 'Nanosondas', 'Barreira de Bloqueio', 'Derrube']
    },
    'Skye': {
        'Rol': 'Iniciadora',
        'Habilidades': ['Regeneración', 'Flor Frenética', 'Fauces Predadoras', 'Amenaza Tropical']
    },
    'Yoru': {
        'Rol': 'Duelista',
        'Habilidades': ['Teleportación', 'Bramido', 'Fragmentación', 'Dimensional Drift']
    },
    'Astra': {
        'Rol': 'Controladora',
        'Habilidades': ['Estelar', 'Impulso Gravitacional', 'Nexo Celestial', 'División Astral']
    },
    'KAY/O': {
        'Rol': 'Iniciador',
        'Habilidades': ['FRAG/mento', 'Cuchillas Recuperables', 'ALFA', 'Neutralización']
    },
    'Chamber': {
        'Rol': 'Centinela',
        'Habilidades': ['Desvio', 'Condenación', 'Siluetas', 'Defensa de Cámara']
    },
    'Neon': {
        'Rol': 'Duelista',
        'Habilidades': ['Punzón de Rayo', 'Parada Trascendental', 'Deslumbramiento Neon', 'Fragmento Imparable']
    },
    'Fade': {
        'Rol': 'Iniciador',
        'Habilidades': ['Alfa Flash', 'Lanza Paranoia', 'Translocador Cuántico', 'Teletransportador Radiante']
    },
    'Harbor': {
        'Rol': 'Controlador',
        'Habilidades': ['Dron Ciberespacial', 'Campos de Energía', 'Impulso Utopiano', 'Bomba Asesina']
    },
    'Gekko': {
        'Rol': 'Iniciador',
        'Habilidades': ['Maldición de Gekko', 'Disparo Silente', 'Rayo Fugaz', 'Engaño de Gekko']
    },
    'Deadlock': {
        'Rol': 'Centinela',
        'Habilidades': ['Derrumbe', 'Torreta Autónoma', 'Barrera Dimensional', 'Supresión Resoluta']
    },
}

def centrar_ventana(ventana):
    ventana.update_idletasks()
    ancho_ventana = ventana.winfo_width()
    altura_ventana = ventana.winfo_height()

    # Obtener las dimensiones de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    altura_pantalla = ventana.winfo_screenheight()

    # Calcular la posición para centrar la ventana
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (altura_pantalla - altura_ventana) // 2

    # Configurar la geometría de la ventana
    ventana.geometry(f"{ancho_ventana}x{altura_ventana}+{x}+{y}")

def cargar_ventana1():
    # Ocultar el frame actual
    frameInicial.pack_forget()

    # Mostrar el nuevo frame
    frame_1.pack(pady=20)
        
def cargar_ventana2():
    
    global cuadro_resultado
    global cuadro_opciones
    global menu_roles
    obtener_respuestas()
    
    
    rolSugerido, Rol_Determinado = determinar_rol(respuestas)
    print(Rol_Determinado)

    
    
    frame_1.pack_forget()
    
 
    frame_2.pack(pady=20)      
    
    etiqueta_RolSugerido = tk.Label(frame_2, text="segun tus respuestas anteriores el rol que mejor se adapta a ti es:", font=("Helvetica", 10))
    etiqueta_RolSugerido.pack(pady=10)

    etiqueta_MostrarRol = tk.Label(frame_2, text = Rol_Determinado, font=("Helvetica", 10))
    etiqueta_MostrarRol.pack(pady=1)

    etiqueta_instruciones = tk.Label(frame_2, text="a continuacion se muestran las caracteristicas de todos los roles por si crees \nque el rol encontrado no es lo tuyo, despues presiona " + "continuar" + " para escoger tu agente ", font=("Helvetica", 10))
    etiqueta_instruciones.pack(pady=10)
            
                

     # Cuadro de opciones para escoger el rol
           
            
    indice = 0
            
    indice = obtener_posicion_rol_sugerido()
    
         
                
    cuadro_opciones = tk.StringVar(frame_2)
    cuadro_opciones.set(roles_disponibles[indice])  # Establecer un valor predeterminado
    cuadro_opciones.trace("w", mostrar_funcion_rol)  # Asociar la función al cambio en la opción seleccionada
    menu_roles = tk.OptionMenu(frame_2, cuadro_opciones, *roles_disponibles)
    menu_roles.pack(pady=10)
     
    

    # Cuadro de texto para mostrar la función del rol
    cuadro_resultado = tk.Text(frame_2, height=8, width=40, state=tk.DISABLED)
    cuadro_resultado.pack(pady=10)
     
    mostrar_funcion_rol()      
    boton_EscogerAgenteSegunRol = tk.Button(frame_2, text="Continuar", command=cargar_ventana3)

    boton_EscogerAgenteSegunRol.pack(pady=10)
    

    
def cargar_ventana3():
    global cuadro_agentes
    global cuadro_Habilidades
    global menu_agentes
    
    global RolSeleccionado
    RolSeleccionado = cuadro_opciones.get()
    
    print("el rol seleccionado es", RolSeleccionado)
    
    
    obtener_respuestas()
    # Ocultar el frame actual
    frame_2.pack_forget()

    # Mostrar el nuevo frame
    frame_3.pack(pady=20)
    
    # Mostrar la función del rol inicialmente
    mostrar_caracteristicas_agente()
    
    mostrar_agentes_por_rol(RolSeleccionado)

    # Crear la caja de opciones para seleccionar el agente

    agentes_por_defecto = obtener_agentes_por_rol(RolSeleccionado)

    cuadro_agentes = tk.StringVar(frame_3)
    cuadro_agentes.set(agentes_por_defecto[0])  # Establecer un valor predeterminado
    cuadro_agentes.trace("w", mostrar_caracteristicas_agente)  # Asociar la función al cambio en la opción seleccionada


    menu_agentes = tk.OptionMenu(frame_3, cuadro_agentes, *agentes_por_defecto)
    menu_agentes.pack(pady=10)

    # Cuadro de texto para mostrar la función del rol
    cuadro_Habilidades = tk.Text(frame_3, height=8, width=40, state=tk.DISABLED)
    cuadro_Habilidades.pack(pady=10)

    cuadro_Habilidades.config(state=tk.DISABLED)
    
    mostrar_caracteristicas_agente()
    
    boton_AgenteSeleccionado = tk.Button(frame_3, text="Continuar", command=cargar_ventana4)

    boton_AgenteSeleccionado.pack(pady=10)
    


    
def cargar_ventana4():
    
    global agenteSeleccioado
    
    agenteSeleccioado = cuadro_agentes.get()
    
    frame_3.pack_forget()

    # Mostrar el nuevo frame
    frame_4.pack(pady=20)
    
    etiqueta_Agente_seleccioado = tk.Label(frame_4, text="el agente que mejor se adapta a ti es", font=("Helvetica", 10))
    etiqueta_Agente_seleccioado.pack(pady=10)
    etiqueta_Agente_seleccioado = tk.Label(frame_4, text=agenteSeleccioado , font=("Helvetica", 10))
    etiqueta_Agente_seleccioado.pack(pady=10)
    
    boton_Salir = tk.Button(frame_3, text="Continuar", command = salir)

    boton_Salir.pack(pady=10)
    
def salir():
    ventana.destroy()
    
def obtener_posicion_rol_sugerido():
    rolSugerido, Rol_Determinado = determinar_rol(respuestas)  # Asumiendo que la función sugerir_rol devuelve el rol sugerido
    try:
        posicion = roles_disponibles.index(Rol_Determinado)
        return posicion
    except ValueError:
        # El rol sugerido no se encuentra en la lista roles_disponibles
        return -1  # O un valor que indique que el rol no se encontró
    
def mostrar_funcion_rol(*args):

    obtener_respuestas()
    rol_seleccionado = cuadro_opciones.get()
    funcion_rol = funciones_roles.get(rol_seleccionado, "Función no especificada")
    cuadro_resultado.config(state=tk.NORMAL)
    cuadro_resultado.delete("1.0", tk.END)  # Limpiar el contenido actual
    cuadro_resultado.insert(tk.END, f"Rol: {rol_seleccionado}\n\nFunción:\n{funcion_rol}")
    cuadro_resultado.config(state=tk.DISABLED)
    
def determinar_rol(respuestas):

    puntajes = {
        "Duelista": 0,
        "Controlador": 0,
        "Centinela": 0,
        "Iniciador": 0
    }

    print(respuestas)
    for i, respuesta in enumerate(respuestas):

        if respuesta == "Agresiva":
            puntajes["Duelista"] += 1
            print("fDGSG")
        elif respuesta== "Tactica":
            puntajes["Controlador"] += 1        
                
       
        elif respuesta== "Liderando ataques":
            puntajes["Duelista"] += 1
        elif respuesta == "Defendiendo zonas":
            puntajes["Centinela"] += 1
        elif respuesta == "Recopilando información":
            puntajes["Centinela"] += 1
        elif respuesta == "Eliminando enemigos en duelos":
            puntajes["Iniciador"] += 1
            puntajes["Duelista"] += 1
                
             
        elif respuesta == "Bloquear visión":
            puntajes["Controlador"] += 1
        elif respuesta == "Controlar campo de batalla":
            puntajes["Controlador"] += 1
            puntajes["Centinela"] += 1
        elif respuesta == "Obtener información":
            puntajes["Centinela"] += 1
        elif respuesta == "Desorganizar oponentes":
            puntajes["Iniciador"] += 1
            puntajes["Controlador"] += 1   
                
         
        elif respuesta == "Corto alcance":
            puntajes["Duelista"] += 1
            puntajes["Centinela"] += 1
        elif respuesta == "Largo alcance":
            puntajes["Controlador"] += 1         
            puntajes["Iniciador"] += 1
                
                
        
        elif respuesta == "Planificar estrategias":
            puntajes["Controlador"] += 1
        elif respuesta == "Tomar decisiones rápidas":
            puntajes["Duelista"] += 1
        elif respuesta == "Adaptarse sobre la marcha":
            puntajes["Duelista"] += 1            
            puntajes["Iniciador"] += 1
                
                
        
        elif respuesta == "Liderar equipo":
            puntajes["Controlador"] += 1
        elif respuesta == "Seguir instrucciones":
            puntajes["Centinela"] += 1
        elif respuesta == "Trabajar de manera independiente":
            puntajes["Duelista"] += 1            
            puntajes["Centinela"] += 1
                
        
        elif respuesta == "Si":
            puntajes["Duelista"] += 1
        elif respuesta == "No":
            puntajes["Controlador"] += 1
            puntajes["Iniciador"] += 1
            puntajes["Centinela"] += 1

            
            
    # Determinar el rol con el puntaje más alto
    rol = max(puntajes, key=puntajes.get)
    print(puntajes)
    Rol_Determinado = rol
    return respuestas, rol

def obtener_respuestas():
    # Limpiar la lista de respuestas antes de agregar nuevas respuestas
    respuestas.clear()

    # Recorrer los cuadros de opciones y agregar las respuestas a la lista
    for cuadro_opciones in cuadros_opciones:
        respuesta = cuadro_opciones.get()
        respuestas.append(respuesta)


def mostrar_agentes_por_rol(rol_seleccionado):
    agentes_del_rol = []

    # Recorrer la lista de agentes y agregar los que coincidan con el rol seleccionado
    for agente, detalles in agentes.items():
        if detalles['Rol'] == rol_seleccionado:
            agentes_del_rol.append(agente)

    # Mostrar los agentes del rol
    if agentes_del_rol:
        resultado = f"Agentes del rol '{rol_seleccionado}': {', '.join(agentes_del_rol)}"
    else:
        resultado = f"No hay agentes asociados al rol '{rol_seleccionado}'."



def mostrar_caracteristicas_agente(*args):
    agente_seleccionado = cuadro_agentes.get()
    
    # Obtener las características del agente seleccionado
    caracteristicas_agente = obtener_caracteristicas_agente(agente_seleccionado)
    
    # Mostrar las características en el cuadro de texto
    cuadro_Habilidades.config(state=tk.NORMAL)
    cuadro_Habilidades.delete("1.0", tk.END)  # Limpiar el contenido actual
    cuadro_Habilidades.insert(tk.END, f"\n\nCaracterísticas de {agente_seleccionado}:\n{caracteristicas_agente}")
    cuadro_Habilidades.config(state=tk.DISABLED)

def obtener_agentes_por_rol(rol_seleccionado):
    
    print("el rol seleciconado es ",rol_seleccionado)
    agentes_por_rol = []

    for agente, detalles_agente in agentes.items():
        if detalles_agente['Rol'] == rol_seleccionado:
            agentes_por_rol.append(agente)

    return agentes_por_rol

def obtener_caracteristicas_agente(agente):
    detalles_agente = agentes.get(agente, {})
    rol_agente = detalles_agente.get('Rol', 'Rol no especificado')
    habilidades_agente = ', '.join(detalles_agente.get('Habilidades', []))
    
    caracteristicas = f"Rol: {rol_agente}\nHabilidades: {habilidades_agente}"
    
    return caracteristicas
#----------------------------------------------------------------------------------------------------------

# Crear la ventana
ventana = tk.Tk()
ventana.title("Choose your Agent")

ventana.minsize(900, 900)  # Tamaño mínimo de la ventana: ancho=300, altura=200
ventana.maxsize(1200, 1200)  # Tamaño máximo de la ventana: ancho=800, altura=600

# Ajustar el tamaño de la ventana directamente
#ventana.geometry("400x400")  # Ajusta las dimensiones según tus necesidades

# Centrar la ventana en la pantalla
centrar_ventana(ventana)

# Frame principal
frameInicial = tk.Frame(ventana)
frameInicial.pack(pady=20)



# Crear un cuadro de texto
#cuadro_texto = tk.Entry(ventana, width=30)  # Puedes ajustar el ancho según tus necesidades
#cuadro_texto.pack(pady=10)

etiqueta_titulo = tk.Label(frameInicial, text="Escoge tu agente", font=("Helvetica", 40))
etiqueta_titulo.pack(pady=10)


# Botón para obtener el rol seleccionado
boton_Comenzar = tk.Button(frameInicial, text="Comenzar", command=cargar_ventana1)
boton_Comenzar.pack(pady=10)



# Iniciar el bucle principal


frame_1 = tk.Frame(ventana)
frame_1.pack_forget()

cuadros_opciones = []

for i, pregunta in enumerate(preguntas_iniciales):
            
    # Crear una etiqueta para mostrar la pregunta
    etiqueta_pregunta = tk.Label(frame_1, text=pregunta)
    etiqueta_pregunta.pack(pady=5)
            
    cuadro_opciones = tk.StringVar(frame_1)
    cuadro_opciones.set(opciones_preguntas[i][0])  # Establecer un valor predeterminado
            
            
    menu_opciones = tk.OptionMenu(frame_1, cuadro_opciones, *opciones_preguntas[i])
    menu_opciones.pack(pady=5)
    cuadros_opciones.append(cuadro_opciones)
            
boton_escogerRol = tk.Button(frame_1, text="Comenzar", command=cargar_ventana2)
boton_escogerRol.pack(pady=10)
        
    #-----------------------------------------------------------------------------------------------------------------------
        
frame_2 = tk.Frame()
    
rolSugerido, rol = determinar_rol(respuestas)

etiqueta_RolSugerido = tk.Label()

etiqueta_MostrarRol = tk.Label()

etiqueta_instruciones = tk.Label()
        
            # Cuadro de opciones para escoger el rol
       
        
indice = 0
        
indice = obtener_posicion_rol_sugerido()
            
           
cuadro_opciones = tk.StringVar()
cuadro_opciones.trace("w", mostrar_funcion_rol)
        
# Cuadro de texto para mostrar la función del rol

#cuadro_resultado = tk.Text()
        
boton_EscogerAgenteSegunRol = tk.Button()



#-----------------------------------------------------------------------------------------------------------------------    



#----------------------------------------------------------------------------------------------------------------------

frame_3 = tk.Frame()
frame_3.pack_forget()

mostrar_agentes_por_rol(rol)

# Crear la caja de opciones para seleccionar el agente

agentes_por_defecto = obtener_agentes_por_rol(rol)

cuadro_agentes = tk.StringVar(frame_3)



# Cuadro de texto para mostrar la función del rol
cuadro_Habilidades = tk.Text()


boton_AgenteSeleccionado = tk.Button()

#----------------------------------------------------------------------------------------------------------------------

frame_4 = tk.Frame()
frame_4.pack_forget()

etiqueta_Agente_seleccioado = tk.Label()
etiqueta_Agente_seleccioado2 = tk.Label()
boton_Salir = tk.Button()

ventana.mainloop()






