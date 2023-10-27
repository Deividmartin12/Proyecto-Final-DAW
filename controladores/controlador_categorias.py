from bd import obtenerConexion

def insertar_categoria(nombre, descripcion):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "INSERT INTO categoria(nombre, descripcion) VALUES (%s, %s)",
            (nombre, descripcion)
        )
    conexion.commit()
    conexion.close()

def obtener_categorias():
    conexion = obtenerConexion()
    categorias = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT categoria_id, nombre, descripcion FROM categoria")
        categorias = cursor.fetchall()
    conexion.close()
    return categorias

def eliminar_categoria(id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM categoria WHERE categoria_id = %s", (id,))
    conexion.commit()
    conexion.close()

def obtener_categoria_por_id(id):
    conexion = obtenerConexion()
    categoria = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT categoria_id, nombre, descripcion FROM categoria WHERE categoria_id = %s", (id,))
        categoria = cursor.fetchone()
    conexion.close()
    return categoria

def actualizar_categoria(nombre, descripcion, id):
    conexion = obtenerConexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE categoria SET nombre = %s, descripcion = %s WHERE categoria_id = %s",
            (nombre, descripcion, id)
        )
    conexion.commit()
    conexion.close()