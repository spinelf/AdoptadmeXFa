import os

def encabezado():
    
   print("  ##     #####     #####   ######   ######     ##              ##   ##  ##   ##              ####  ##   ##  ##   ##   ####     #####   ######")
   print(" ####     ## ##   ##   ##   ##  ##  # ## #    ####             ##   ##  ###  ##               ##   ##   ##  ###  ##    ##     ##   ##   ##  ##")
   print("##  ##    ##  ##  ##   ##   ##  ##    ##     ##  ##            ##   ##  #### ##               ##   ##   ##  #### ##    ##     ##   ##   ##  ##")
   print("##  ##    ##  ##  ##   ##   #####     ##     ##  ##            ##   ##  ## ####               ##   ##   ##  ## ####    ##     ##   ##   #####")
   print("######    ##  ##  ##   ##   ##        ##     ######            ##   ##  ##  ###           ##  ##   ##   ##  ##  ###    ##     ##   ##   ## ##")
   print("##  ##    ## ##   ##   ##   ##        ##     ##  ##            ##   ##  ##   ##           ##  ##   ##   ##  ##   ##    ##     ##   ##   ##  ##")
   print("##  ##   #####     #####   ####      ####    ##  ##             #####   ##   ##            ####     #####   ##   ##   ####     #####   #### ##")  
   print(" ")
   print(" ") 

def menu():
    print("Bienvenidos a mi carta de presentación")
    print(" ")
    print("1. Me presento")
    print("2. Ver mis motivaciones para entrar en el grupo de trabajo")
    print("3. Ir a mi repositorio")
    print("4. Ver mi curriculum")
    print("5. Salir")

    opcion= int(input("¿Qué os apetece ver, elige una opción? "))
    
    return opcion

def porqueAdoptarme():
    
       
    print("Mi nombre es Silvia y estoy muy contenta de estar en el proceso de selección")
    print("Os voy a presentar mis principales motivaciones para que me adopteís:")
    print("1. Me apasiona desde muy pequeña el mundo de los ordenadores y la tecnología")
    print("2. Empece en la programación con 8 años pero al final mis estudios fueron por otro camino y he decidido que eso tiene que camnbiar y esta es mi opotunidad.")
    print("3. Ahora que he vuelto a retomar la progrmación me he dado cuenta de que es algo en lo que puedo estar horas ya que me encantan los desafios y el ser capaz de resolverlos")
    print("4. Disfruto colaborando con otros desarrolladores para crear proyectos, me encanta el trabajo en equipo.")
    print("5. Quiero aprender y crecer profesionalmente en un entorno que me permita desarrolar mis habilidades")


def presentacion():
    
    print("Siempre he sido apasionada de los datos y las nuevas tecnologías. Hace unos años decidí dar un emocionante giro \na mi vida profesional y adentrarme en el fascinante mundo tech. Estudié un grado superior en desarrollo de aplicaciones\nweb y completé mi formación con un bootcamp de Data Analyst. Me considero una persona muy orientada a objetivos, organizada\ny proactiva, con una gran motivación para aprender y crecer en el ámbito IT. Con más de 15 años de experiencia en el sector\nfinanciero, puedo contribuir en el sector de la tecnología con mi notable experiencia en business, y a la vez con una perspectiva\nfresca y conocimientos técnicos actualizados.")
    
    print("Podéis encontrar mi linkedin en: www.linkedin.com/in/silviapiñel")
    
def repositorio():
    
    print("Si quieres ver mi repositorio copia y pega el siguiente link en tu navegador:  https://github.com/spinelf/AdoptadmeXFa.git")   

def curriculum():
    pass

respuesta="y"

while respuesta == "y":

    encabezado()

    opcionuser= menu()


    if opcionuser == 1:
    
        presentacion()
        input("Pulse Enter para continuar")
        

    elif opcionuser == 2:
    
        porqueAdoptarme()
        input("Pulse Enter para continuar")

    elif opcionuser == 3:
    
        repositorio()
        input("Pulse Enter para continuar")

    elif opcionuser == 4:
    
        curriculum()
        input("Pulse Enter para continuar")

    elif opcionuser == 5:
    
        quit()

    else: 
    
        print("Elige una opción entre el 1 y el 4, Muchas gracias!!!")