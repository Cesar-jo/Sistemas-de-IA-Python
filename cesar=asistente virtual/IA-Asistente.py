from os import name
import sys
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from wikipedia.wikipedia import languages
import webbrowser
import keyboard
from pygame import mixer
import time


name = 'cesar'
#nuestra variable escuchr sera = a la funcion= sr.Recognizer que sirve para que nos reconosca la voz
escuchar = sr.Recognizer()
# le decimos que engine sera igual a nuestra libreria pyttsx3.init() que son las voces del asistente  virtual
engine = pyttsx3.init() 

def talk(text):
# Lo que hace esta funcion es decir algo que le escribamos
#con la funcion .say, imprimimos lo que queremos que diga en voz
    engine.say(text)
    engine.runAndWait() # y con la funcion = .runAndWait() coore o imprime en voz lo que le indicamos


''''
def activarAsistente():
    listen()
    while True:
        time.sleep(1)
'''

def listen():
#abrimos un bloque  try = que sirve para indicarle que deve de hacer el programa y except para las excepciones
#si hay un error
    try:
    # utilizamos la funcion sr.Microphone(), que sirve para activar el microfono
    #esta funcion la llamaremos = source
        with sr.Microphone() as source:
        #nos imprimira un mensaje de escuchando....
            print("Escuchando...")
        #pasamos la funcion .listen = que nos sirve para escuhar, osea que nos detecte el programa lo que decimos
        #y le pasamos la funcion sr.Microphone que la renombramos source= para que se active el microfono 
            voice = escuchar.listen(source)#y capte la funcion listend lo que decimos
            print("Reconociendo...")
        #Utilizaremos la funcion/API de google .recognize_google = lo que ara sera grabar lo que decimos
        # y combierte lo que decimos texto hablado  en texto escrito
            rec = escuchar.recognize_google(voice, language="es-ES")#y le pasamos la funcion de nuestra variable(voice)
            rec = rec.lower() # esta funcion hacemos que quite algo de lo que pedimos, en este caso el nombre
            if name in rec:
                # lo que hace  la funcion  .replace = es remplazar lo que le pedimo en este caso el name
                rec = rec.replace(name, '') # y lo deja en blanco = ''
        #imprimimos nuestra variable rec que lo que hara con la api de google es imprimir lo que decimos
                #print(rec)#imprimira lo que hablamos
    except:
        pass  
    return rec

def run():
    rec = listen()
    if 'reproduce' in rec: # le decimos que si encuentra que decimos reproduce
       musica = rec.replace('reproduce', '') # va a remplazar eso que decimos con la funcion = .replace
       talk('Reproduciendo' + musica) #por lo que queremos que reprodusca, en este caso musica, y lo concatenamos +
       #con la libreria de pywhatkit y la funcion = .playonyt
       #  hace que podamos reproducir cualquier video en youtube
       pywhatkit.playonyt(musica)

    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)

    elif 'busca' in rec:
        buscar = rec.replace('busca', '')
        wikipedia.set_lang("es-ES")
        #el 1 al final le decimos que nos dija la informacion solo 1 vez o tambien que dija solo la primer oración
        info = wikipedia.summary(buscar, 1)
        talk(info)

    
    elif 'alarma' in rec:
        num = rec.replace('alarma', '')
        num = num.strip()
        talk("Alarma activada a las" + num + " horas")
        while True:
            #llamamos la libreria que son para la consulta del tiempo y hora = datetime.datetime
            # con la funcion .now() = sirve para traer o consultar la fecha y hora que tenemos actualmente
            #con la funciom = .strftime pasamos esa hora y fecha a string osea a texto
            #le pasamos como la queremos osea por hora y minutos = ('%H:%M')
            #y todo eso sera igual a nuestra variable == num
            if datetime.datetime.now().strftime('%H:%M') == num:
                #podemos poner print en vez de talk 
                talk("Despieeerrrtaaaa que se te hace tarde")
                #inicialisamos nuestra libreria
                mixer.init()
                #la funcion .musica.load sirve para que cargue o reprodusca una cancion (aqui ira la ruta de la cancion a reproducir)
                mixer.musica.load("alarma-auronplay.mp3")
                #y con esta funcion = .music.play() reproducimos la cancion
                mixer.music.play()
                if 'parar' in rec:
                #if keyboard.read_key() == "s":
                    mixer.music.stop()
                    break




    elif 'Amazon' in rec:
        amazon = rec.replace('amazon', '')
        webbrowser.open('https://www.amazon.com.mx/')
        talk('Abriendo' + amazon)


    elif 'facebook' in rec:
        facebook = rec.replace('facebook', '')
        webbrowser.open('https://es-es.facebook.com/')
        talk('Abriendo' + facebook)


    elif 'Youtube' in rec:
        yt = rec.replace('youtube', '')
        webbrowser.open('https://www.youtube.com/')
        talk('Abriendo' + yt)
    

    elif 'Noticias' in rec:
        nt = rec.replace('Noticias', '')
        webbrowser.open('https://www.eluniversal.com.mx/')
        talk('Abriendo' + nt)

    
    elif 'Whatsapp' in rec:
        wsptt = rec.replace('Whatsapp', '')
        webbrowser.open('https://web.whatsapp.com/')
        talk('Abriendo' + wsptt)

    
    elif 'eres' in rec:
        im = rec.replace('eres', '')
        talk('Hola soy Cesar2.0, Fui creado el 11 de mayo del 2021, a las 5:40 de la tarde, por el programador y desarrollador de software, César Jose Valladares Rodriguez, quien me proclamo como cesar2.0, mucho gusto en conocerte, estoy para lo que me pidas')


    elif 'chinga tu madre' in rec:
        chin = rec.replace('chinga tu madre', '')
        talk('No te entendi que me querias perdir, pero chinga la tuya por si acaso')

    elif 'Vete a la berga' in rec:
        vrg = rec.replace('vete a la vrg', '')
        talk('La Verga, es una aldea, está en Canarias y tiene alrededor de 63 habitantes. La berga está situada cerca de Los Caideros., asi que cuando te manden a la verga, ya sabras como llegar puñeton ajajajaj.')

    elif 'Que puedes hacer' in rec:
        hacer = rec.replace('Que puedes hacer', '')
        talk('Hola, que tal, pues te cuento, podemos entablar una conversacion sencilla, puedo traducirte todo lo que me pidas, puedo generarte una alarma, resolverte problemas matematicos, dercirte tu frase del dia o solamente frases, estoy en constante cambio, por lo momneto todo eso pjedo hacer, espera mis posteriores actualizaciones para ver que cosas nuevas tendre.')
    


    elif 'puerta' in rec:
        talk("Porfavor digite la contraseña para poder abrir la puerta de tu recamara")
        
        password = int(input("Ingrese la contraseña: "))
        if password == 20012703:
            talk("Bienvenido mi lord cesar, puede pasar")
        else:
            talk('Contraseña incorrecta, vuelva a intentar')


    '''
    elif 'reconocimiento facial' in rec:
        talk('Perfecto, veremos quien eres en nuestra red neuronal artificial ya entrenada')
        phat = 'C:/Users/ternu/OneDrive/Escritorio/Redesneuronalespython/capasalida-reconocimientoFacial.py'
        archivo = open(phat)
'''


#creamos un bucle que contenga un listado de palabras, para que nuestro interado = i pase o recorra ese array
    for i in ['stop', 'termina', 'terminar', 'parar', 'apagar', 'apagate']:
        #le decimos que si nuestro interador = i dice = rec alguna palabra que tenemos en nuestro array = ['stop', 'termina', 'terminar', 'parar']:
        if i in rec:
            #que nos dija que esta cerrando el asistente
            talk('Sesion finalizada, saliendo del asistente')
            # y lo cerramos con el break
            break
 

    else:
        print("reconozco: " + rec)

while True:
    run()
    #activarAsistente()
