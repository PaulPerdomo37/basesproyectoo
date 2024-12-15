import mysql.connector

def conectar_db():
    """Conecta a la base de datos MySQL usando XAMPP."""
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",  # Usuario por defecto en XAMPP
            password="",  # Sin contraseña por defecto en XAMPP
            database="SistemaEmpleados"  # Nombre correcto de la base de datos
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

def agregar_empleado(nombre, usuario, contrasena, horario):
    """Agrega un empleado a la base de datos."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = (
                "INSERT INTO Empleado (Nombre, Usuario, Contraseña, Horario) "
                "VALUES (%s, %s, %s, %s)"
            )
            valores = (nombre, usuario, contrasena, horario)
            cursor.execute(query, valores)
            conexion.commit()
            print("Empleado agregado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al agregar empleado: {err}")
        finally:
            cursor.close()
            conexion.close()

def listar_empleados():
    """Lista todos los empleados de la base de datos."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "SELECT * FROM Empleado"
            cursor.execute(query)
            empleados = cursor.fetchall()

            print("Lista de empleados:")
            for empleado in empleados:
                print(f"ID: {empleado[0]}, Nombre: {empleado[1]}, Usuario: {empleado[2]}, Horario: {empleado[4]}")
        except mysql.connector.Error as err:
            print(f"Error al listar empleados: {err}")
        finally:
            cursor.close()
            conexion.close()

def eliminar_empleado(id_empleado):
    """Elimina un empleado por ID."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "DELETE FROM Empleado WHERE ID_Empleado = %s"
            cursor.execute(query, (id_empleado,))
            conexion.commit()
            if cursor.rowcount > 0:
                print("Empleado eliminado exitosamente.")
            else:
                print("No se encontró un empleado con ese ID.")
        except mysql.connector.Error as err:
            print(f"Error al eliminar empleado: {err}")
        finally:
            cursor.close()
            conexion.close()
def validar_usuario(tabla, usuario, contrasena):
    """Valida el usuario y contraseña en la tabla correspondiente."""
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = f"SELECT * FROM {tabla} WHERE Usuario = %s AND Contraseña = %s"
            cursor.execute(query, (usuario, contrasena))
            resultado = cursor.fetchone()
            return resultado is not None  # Devuelve True si el usuario existe
        except mysql.connector.Error as err:
            print(f"Error al validar usuario: {err}")
            return False
        finally:
            cursor.close()
            conexion.close()
# Menú de la aplicación
def menu_administrador():
    """Muestra el menú de administrador."""
    while True:
        print("\n=== Menú Administrador ===")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Eliminar empleado")
        print("4. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            usuario = input("Usuario: ")
            contrasena = input("Contraseña: ")
            horario = input("Horario (ej. 08:00-17:00): ")
            agregar_empleado(nombre, usuario, contrasena, horario)
        elif opcion == "2":
            listar_empleados()
        elif opcion == "3":
            id_empleado = int(input("ID del empleado a eliminar: "))
            eliminar_empleado(id_empleado)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
def menu_encargado_inventario():
    """Muestra el menú del encargado de inventario."""
    print("\n=== Menú Encargado de Inventario ===")
    print("Acceso a funciones relacionadas con el inventario aún no implementadas.")

def menu_soporte_cliente():
    """Muestra el menú de soporte al cliente."""
    print("\n=== Menú Soporte al Cliente ===")
    print("Acceso a funciones relacionadas con soporte al cliente aún no implementadas.")

def menu_especialista_marketing():
    """Muestra el menú del especialista en marketing."""
    print("\n=== Menú Especialista en Marketing ===")
    print("Acceso a funciones relacionadas con marketing aún no implementadas.")

def menu_principal():
    while True:
        print("\n=== Sistema de Gestión ===")
        print("1. Ingresar como Administrador")
        print("2. Ingresar como Encargado de Inventario")
        print("3. Ingresar como Soporte al Cliente")
        print("4. Ingresar como Especialista en Marketing")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            usuario = input("Usuario: ")
            contrasena = input("Contraseña: ")
            if validar_usuario("administradorgeneral", usuario, contrasena):
                menu_administrador()
            else:
                print("Usuario o contraseña incorrectos para Administrador.")

        elif opcion == "2":
            usuario = input("Usuario: ")
            contrasena = input("Contraseña: ")
            if validar_usuario("encargadoinventario", usuario, contrasena):
                menu_encargado_inventario()
            else:
                print("Usuario o contraseña incorrectos para Encargado de Inventario.")

        elif opcion == "3":
            usuario = input("Usuario: ")
            contrasena = input("Contraseña: ")
            if validar_usuario("soportecliente", usuario, contrasena):
                menu_soporte_cliente()
            else:
                print("Usuario o contraseña incorrectos para Soporte al Cliente.")

        elif opcion == "4":
            usuario = input("Usuario: ")
            contrasena = input("Contraseña: ")
            if validar_usuario("especialistamarketing", usuario, contrasena):
                menu_especialista_marketing()
            else:
                print("Usuario o contraseña incorrectos para Especialista en Marketing.")

        elif opcion == "5":
            print("Saliendo del sistema. Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()
