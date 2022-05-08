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
    