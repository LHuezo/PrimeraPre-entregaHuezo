#Base de datos usuario-contraseña
BD={"lauty":"password123"}

#Funcion para mostrar informacion
def Mostrar_base_de_datos():
    print (BD)
#Funcion para alamcenar informacion
def registro_en_base_de_datos():
    user=input("Defina su nombre de usuario:")
    password=input("Genere una contraseña:")
    while user in BD:
        user=input("Este usuario ya esta regristrado, intente con otro:")
    else:
        BD[user]=password
        print("Su usuario se registro exitosamente")
#Funcion para login de usuarios
def login():
    nombre_esperado=input("Ingrese su nombre de usuario:")
    contraseña_esperada=input("Ingrese la contraseña correspondiente a su usuario:")
    while nombre_esperado not in BD:
        nombre_esperado=input("Este usuario no esta registrado intente otro:")

    intentos=3
    while (BD[nombre_esperado] != contraseña_esperada) and (intentos > 0):
        contraseña_esperada=input("La contraseña ingrsada no es la correcta, intente otra vez:")
        intentos -= 1
    else:
        if intentos==0:
            print("Se acabaron los intentos")
        else:
         print("Ha podido ingresar correctamente")

#Funcion para elgir cual de las acciones se quiere realizar
def menu_principal():
    print("Escriba \"Quiero registrarme\" para registrarse en la base de datos")
    print("Escriba \"Quiero ingresar\" para logearse en la base de datos")
    print("Escriba \"Quiero ver la informacion\" para ver la informacion en la base de datos")
    accion=input("Escriba algunas de las acciones mostradas anteriormente:")
    while (accion.capitalize() != "Quiero registrarme") and (accion.capitalize() != "Quiero ingresar") and (accion.capitalize() != "Quiero ver la informacion"):
        accion=input("El comando escrito no es ninguno de los esperados. Intente de nuevo:")
    else:
        if accion.capitalize() == "Quiero registrarme":
            registro_en_base_de_datos()
        elif accion.capitalize() == "Quiero ingresar":
            login()
        else:
            Mostrar_base_de_datos()

menu_principal()
    