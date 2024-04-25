#Base de datos usuario-contraseña
base_de_datos={"lauty":"password123"}

#Funcion para mostrar informacion
def mostrar_base_de_datos():
    for clave,valor in base_de_datos.items():
        print(clave,":", valor)
#Funcion para alamcenar informacion
def registro_en_base_de_datos():
    user=input("Defina su nombre de usuario:")
    password=input("Genere una contraseña:")
    while user in base_de_datos:
        user=input("Este usuario ya esta regristrado, intente con otro:")
    else:
        base_de_datos[user]=password
        print("Su usuario se registro exitosamente")
#Funcion para login de usuarios
def login():
    nombre_esperado=input("Ingrese su nombre de usuario:")
    password_esperada=input("Ingrese la contraseña correspondiente a su usuario:")
    while nombre_esperado not in base_de_datos:
        nombre_esperado=input("Este usuario no esta registrado intente otro:")

    intentos=3
    while (base_de_datos[nombre_esperado] != password_esperada) and (intentos > 0):
        password_esperada=input("La contraseña ingrsada no es la correcta, intente otra vez:")
        intentos -= 1
    else:
        if intentos==0:
            print("Se acabaron los intentos")
        else:
         print("Ha podido ingresar correctamente")

#Funcion para elgir cual de las acciones se quiere realizar
def menu_principal():
    print("Escriba el numero \"1\" para registrarse en la base de datos")
    print("Escriba el numero \"2\" para logearse en la base de datos")
    print("Escriba el numero \"3\" para ver la informacion en la base de datos")
    accion=input("Escriba algunas de las acciones mostradas anteriormente:")
    while (int(accion) != 1) and (int(accion) != 2 ) and (int(accion) != 3):
        accion=input("El comando escrito no es ninguno de los esperados. Intente de nuevo:")
    else:
        if int(accion) == 1:
            registro_en_base_de_datos()
        elif int(accion) == 2:
            login()
        else:
            mostrar_base_de_datos()

menu_principal()