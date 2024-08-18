import os
import webbrowser

def abrir_curriculum(): #Funcion para abrir el curriculum PDF
    ruta_pdf = "CVSilviaPinel.pdf"
    webbrouser.open(ruta_pdf)

def encabezado():   # Detalle estético que se muestra en cada una de las pantallas :)
    
   print("  ##     #####     #####   ######   ######     ##              ##   ##  ##   ##              ####  ##   ##  ##   ##   ####     #####   ######")
   print(" ####     ## ##   ##   ##   ##  ##  # ## #    ####             ##   ##  ###  ##               ##   ##   ##  ###  ##    ##     ##   ##   ##  ##")
   print("##  ##    ##  ##  ##   ##   ##  ##    ##     ##  ##            ##   ##  #### ##               ##   ##   ##  #### ##    ##     ##   ##   ##  ##")
   print("##  ##    ##  ##  ##   ##   #####     ##     ##  ##            ##   ##  ## ####               ##   ##   ##  ## ####    ##     ##   ##   #####")
   print("######    ##  ##  ##   ##   ##        ##     ######            ##   ##  ##  ###           ##  ##   ##   ##  ##  ###    ##     ##   ##   ## ##")
   print("##  ##    ## ##   ##   ##   ##        ##     ##  ##            ##   ##  ##   ##           ##  ##   ##   ##  ##   ##    ##     ##   ##   ##  ##")
   print("##  ##   #####     #####   ####      ####    ##  ##             #####   ##   ##            ####     #####   ##   ##   ####     #####   #### ##")  
   print(" ")
   print(" ") 

def menu():   #Este es el menú principal donde podemos controlar todas las opciones de nuestro menú.
    
    os.system("cls")
    continuar =True
    while continuar:
        opcionCorrecta =False   # Se ejecutará hasta que el usuario presione la opción 5 para salir.
        os.system("cls")
        while not opcionCorrecta:
            encabezado()
            print("")
            print
            print("===========================================    Menú    ====================================================")
            print("")
            
            print("Bienvenidos a mi carta de presentación")
            print(" ")
            print("1. Me presento")
            print("2. Ver mis motivaciones para entrar en el grupo de trabajo")
            print("3. Ir a mi repositorio")
            print("4. Ver mi curriculum en PDF")
            print("5. Salir")
            
            opcion= int(input("Elige una opción:  "))
            
            if opcion <1 or opcion >5:
                 print("La opción introducida no esta disponible")
            
            elif opcion ==9:
                continuar=False
                print ("Muchas gracias por interesarte por mi perfil")
                break
            else:
                opcionCorrecta=True
                llamarOpcionCorrecta(opcion)

def llamarOpcionCorrecta(opcion):  #Esta función nos permite llamar a las funciones que realizan las acciones seleccionadas por el usuario.
  
    if opcion == 1:      # Esta opción nos muestra la presentación de mi perfil
        
       os.system("cls")
       encabezado()
       print("")
       presentacion()
       print("")
       input("Pulse Enter para continuar  ")
       os.system("cls")
 
        
    elif opcion == 2:     # Esta opción nos muestra las motivaciones que me han llevado hasta aquí.
        
        os.system("cls")
        encabezado()
        print("")
        porqueAdoptarme()
        print("")
        input("Pulse Enter para continuar  ")
        os.system("cls")
        
    elif opcion == 3:   # Esta opción nos muestra el link a mi repositorio Github
        os.system("cls")
        encabezado()
        print("")
        repositorio()
        print("")
        input("Pulse Enter para continuar  ")
        os.system("cls")  
    
    elif option==4: #Esta opcion abre mi curriculum en PDF
        os.system("cls")
        encabezado()
        print("")
        abrir_curriculum()
        print("")
        input("Pulse Enter para continuar")
        os.system("cls")

    
    elif opcion == 5:  # Pulsando la opción 4 salimos del programa
        
         quit()

    else:
        pass
    


def presentacion():
    
    print("Siempre he sido apasionada de los datos y las nuevas tecnologías. Hace unos años decidí dar un emocionante giro \na mi vida profesional y adentrarme en el fascinante mundo tech. Estudié un grado superior en desarrollo de aplicaciones\nweb y completé mi formación con un bootcamp de Data Analyst. Me considero una persona muy orientada a objetivos, organizada\ny proactiva, con una gran motivación para aprender y crecer en el ámbito IT. Con más de 15 años de experiencia en el sector\nfinanciero, puedo contribuir en el sector de la tecnología con mi notable experiencia en business, y a la vez con una perspectiva\nfresca y conocimientos técnicos actualizados.")
    print("")
    print("Podéis encontrar mi linkedin en: www.linkedin.com/in/silviapiñel")
    print("")

def porqueAdoptarme():
    
    print(" ")   
    print("Mi nombre es Silvia y estoy muy contenta de estar en el proceso de selección")
    print(" ") 
    print("Os voy a presentar mis principales motivaciones para que me adopteís:")
    print(" ") 
    print("1. Me apasiona desde muy pequeña el mundo de los ordenadores y la tecnología")
    print("2. Empece en la programación con 8 años pero al final mis estudios fueron por otro camino y he decidido que eso tenía que camnbiar y esta es mi opotunidad.")
    print("3. Ahora que he vuelto a retomar la progrmación me he dado cuenta de que es algo en lo que puedo estar horas ya que me encantan los desafios y el ser capaz de resolverlos")
    print("4. Disfruto colaborando con otros desarrolladores para crear proyectos, me encanta el trabajo en equipo.")
    print("5. Quiero aprender y crecer profesionalmente en un entorno que me permita desarrolar mis habilidades")
    print(" ")


    
def repositorio():
    
    print("")
    print("Si quieres ver mi repositorio copia y pega el siguiente link en tu navegador:  https://github.com/spinelf/AdoptadmeXFa.git")   
    print("")

os.system("cls")  
menu()
