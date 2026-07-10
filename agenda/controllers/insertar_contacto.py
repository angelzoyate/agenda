import web
import sqlite3

render = web.template.render('views', base='layout')

class InsertarContacto:
    
    def GET(self):
        
        return render.insertar_contacto()

    def POST(self):
       
        datos = web.input()
        
        nombre = datos.nombre
        primer_ap = datos.primer_apellido
        segundo_ap = datos.segundo_apellido
        email = datos.email
        telefono = datos.telefono

        exito = False

        try:
            
            conexion = sqlite3.connect("sql/agenda.db")
            cursor = conexion.cursor()
            
            query = """
                INSERT INTO contactos (nombre, primer_apellido, segundo_apellido, email, telefono)
                VALUES (?, ?, ?, ?, ?)
            """
            
            cursor.execute(query, (nombre, primer_ap, segundo_ap, email, telefono))
            conexion.commit()
            conexion.close()
            exito = True
            
        except sqlite3.Error as error:
            print(f"ERROR AL INSERTAR: {error.args}")
            return f"Hubo un error en la base de datos: {error.args}"

        if exito:
            web.ctx.status = '303 See Other'
            web.header('Location', '/lista_contactos')
            return ''
        else:
            return "No se pudo guardar el contacto."