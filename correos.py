#Libreria - Menu - BD
import smtplib
import pyodbc
import time
def menu():
    print("  \t Menú ")
    print("\n 1. Ingrese un registro",
          "\n 2. Elimine un registro",
          "\n 3. Ver registros ya existentes",
          "\n 4. Enviar un correo predeterminado",
          "\n 5. Salir del menú")
    input (" ")
    opcion = int(input("Digite la opcion quiere realizar: "))
    return opcion

def conexion():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-656CLLE;DATABASE=correos_py;Trusted_Connection=yes;')
        print("¡Conexión Exitosa!")
        return connection
    except Exception as ex:
        print(f"Error. Conexión a DB. {ex}")

#Funcion para ingresar datos del registro que se desea agregar
def consulta_agregar():
    input (" ")
    nombre = input("Digite un nombre: ")
    cedula = input(f"Digite el número de identificación de {nombre}: ")
    correo = input(f"Digite el correo de {nombre}: ")
    edad = input(f"Digite la edad de {nombre}: ")
    ciudad = input(f"Digite la ciudad/municipio donde vive {nombre}: ")
    productos_adqui = input(f"Digite el nombre del producto comprado por {nombre}: ")
    fecha_compra = input("Digite la fecha de venta asi: Día - Mes - Año: ")
    query = "insert into usuario (nombre, cedula, correo, edad, ciudad, productos_adqui, fecha_compra) values ('" + nombre + "','" + cedula + "','" + correo + "','" + edad + "','" + ciudad + "','" + productos_adqui + "','" + fecha_compra + "') "
    return query

def consulta_eliminar():
    info = input("Digite el nombre de la persona para borrarla del registro hecho: ")
    query = "delete from usuario where nombre='" + info + "'"
    return query

#Funcion para agregar un registro a la BD
def agregar_registro():
    conect = conexion()
    agg_cursor = conect.cursor()
    query = consulta_agregar()
    agg_cursor.execute(query)
    agg_cursor.commit()
    agg_cursor.close()
    conect.close()
    input (" ")
    print("¡El registro fue agregado con exito!")

#Funcion para eliminar un registro de la BD
def eliminar_registro():
    conx = conexion()
    del_cursor = conx.cursor()
    query = consulta_eliminar()
    del_cursor.execute(query)
    del_cursor.commit()
    del_cursor.close()
    conx.commit()
    input (" ")
    print("¡El registro fue eliminado con exito!")


#Funcion para ver el registro guardado en la BD
def ver_registros():
    query = "select * from usuario;"
    conx = conexion()
    ver_cursor = conx.cursor()
    ver_cursor.execute(query)
    registro = ver_cursor.fetchone()
    while registro:
        print(registro)
        registro = ver_cursor.fetchone()
    ver_cursor.close()
    conx.close()
    input()


#Funcion para filtro de usuarios por edad
def menu_filtro():
    print("\t Filtro con el que se enviará el correo")
    print("1. Por la edad del usuario")
    opc = int(input("\n Opción que desea: "))
    if opc ==1:
        enviar_edad()
        return opc

def enviar_edad():
    print("\n 1. Menores de 40 años",
          "\n 2. Mayores de 50 Años")
    input (" ")

    opc = int(input("Digite la opción adecuada: "))
    return opc

   #funcion para registro de los usuarios con BD y condicional para edades 

def datos_clientes():
    datos = []
    conx = conexion()
    query = "select nombre, edad, correo from usuario;"
    ver_cursor = conx.cursor()
    ver_cursor.execute(query)
    registro = ver_cursor.fetchone()
    while registro:
        lista = list(registro)
        datos.append(lista)
        registro = ver_cursor.fetchone()
    conx.close()
    return datos

def filtro():
        clientes = []
        opc = enviar_edad()
        registros = datos_clientes()
        if opc == 1:
            opc = 40
            for n in registros:
                datos = n
                if int(datos[1]) <= opc:
                    print(n)
                clientes.append(n)
        elif opc == 2:
            opc = 50
            for n in registros:
                datos = n
                if int(datos[1]) >= opc:
                    print(n)
                    clientes.append(n)
        else:
            input("")
            print("Error. La opción no es valida!")
        return clientes

# funcion para el envio de correos conectado a BD.
def envio_correo():
    edades = ["Menor", "Mayor"]
    registros = filtro()
    for n in registros:
        cliente = n
        fecha = str(time.strftime("%d/%m/%Y"))
        nombre = str(cliente[0])
        edad = cliente[1]
        mail = cliente[2]
        mensaje = (f"Hola {nombre}. Este correo se envio de manera automatica por el ejercicio realizado de Python.")
        asunto = "Correo de prueba desde PY"
        mensaje = 'Subject: {}\n\n{}'.format(asunto, mensaje)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('salome.jaramillo557@pascualbravo.edu.co', 'jaramillo22')
        server.sendmail('salome.jaramillo557@pascualbravo.edu.co', mail, mensaje)
        server.quit()
        input (" ")
        print("El correo se envió adecuadamente a: ",
              f"\n Nombre: {nombre}, Correo: {mail}, Edad: {edad}")

  # Asignando condicional para opciones del menu     

def bucle():
    while True:
        opcion = menu()
        if opcion == 1:
            agregar_registro()
        elif opcion == 2:
            eliminar_registro()
        elif opcion == 3:
            ver_registros()
        elif opcion == 4:
            envio_correo()
        elif opcion == 5:
            print("Saliste del menú")
            break
        elif opcion >= 6:
            print("Digite una opción valida")
bucle()
    