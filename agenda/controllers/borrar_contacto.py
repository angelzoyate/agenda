import web
import sqlite3

render = web.template.render('views', base='layout')

class BorrarContacto:

    def buscarContacto(self, id_contacto:int):
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM contactos WHERE id_contacto = ?"
            cursor.execute(query,(id_contacto,))
            resultado = cursor.fetchone()

            if resultado is None:
                conexion.close()
                return None

            contacto = {
                "id_contacto":resultado[0],
                "nombre":resultado[1],
                "primer_apellido":resultado[2],
                "segundo_apellido":resultado[3],
                "email":resultado[4],
                "telefono":resultado[5]
            }
            conexion.close()
            print(contacto)
            return contacto
        except sqlite3.Error as error:
            print(f"ERROR 102: {error.args}")
            return None
        except Exception as error:
            print(f"ERROR 103: {error.args}")
            return None

    def eliminarContacto(self, id_contacto: int):
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            cursor = conexion.cursor()
            query = "DELETE FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (id_contacto,))
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.Error as error:
            print(f"ERROR 104 (Borrado): {error.args}")
            return False

    def GET(self, id_contacto:int):
        print(f"ID_CONTACTO: {id_contacto}")
        contacto = self.buscarContacto(id_contacto)
        if contacto is None:
            raise web.seeother('/lista_contactos') # Si no existe, redirige
        return render.borrar_contacto(contacto)
    
    def POST(self, id_contacto: int):
        # Llamamos al método que borra usando el ID que viene en la URL
        exito = self.eliminarContacto(id_contacto)
        
        if exito:
            # Redirige de vuelta a la lista de contactos si se borró con éxito
            raise web.seeother('/lista_contactos')
        else:
            return "No se pudo eliminar el contacto. Ocurrió un error."