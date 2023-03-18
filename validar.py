#Nombre del archivo: validar.py
#Autor: Dayhana Acevedo Gutierrez 
#Fecha: Marzo 18/2023
#Descripcion: Programa que valida el nombre, la edad y el correo

while True:
    menu="""
    Bienvenidos al registro de usuarios, llene los campos que le soliciten y seleccione un numero del 1 al 3: 
    [1]Digitar su Nombre 
    [2]Digitar su edad
    [3]Digitar su correo electronico 
    [4]Salir
    """
    print(menu)
    opcion=input('Entre la opcion 1, 2, 3 o 4: ')
    if opcion=='1':
        while True:
            nombre=input('Digite su Nombre: ')
            if nombre.isalpha():
                print("Su nombre es:",nombre)
                break
            else:
                print("Su nombre esta mal digitado")

            
    elif opcion=='2':
        while True:
            edad=input('Digite su edad: ')
            if edad.isdigit():
                print("Su edad es:",edad)
                break
            else:
                print("Su edad esta mal digitada")


    elif opcion=='3':
        while True:
            Correo=input('Digite su correo: ')
            if Correo.find('@')==1 and Correo.find('.')>=0:
                print("Su correo es:",Correo)
                break
            else:
                print("Su correo esta mal digitado")

    
    elif opcion=='4':
        exit()



