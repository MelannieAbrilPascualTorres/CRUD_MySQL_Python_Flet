
import flet as ft
import mysql.connector
import sys
import bcrypt

def main(page: ft.Page):
    page.title = "Sistema de alumnos"
    page.bgcolor = ft.Colors.LIME_100
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    try:
        conexion = mysql.connector.connect(

            host="localhost", 
            user="root",       
            password=""    
        )
        cursor = conexion.cursor()
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS escuela_db"
        )
        cursor.execute(
            "USE escuela_db"
        )
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS alumnos (
                       matricula VARCHAR(20) PRIMARY KEY,
                       apellido_paterno VARCHAR(50) NOT NULL,
                       apellido_materno VARCHAR(50) NOT NULL,
                       nombres VARCHAR(100) NOT NULL,
                       curp VARCHAR(18) NOT NULL,
                       especialidad VARCHAR(100) NOT NULL,
                       telefono CHAR(10) NOT NULL,
                       ciudad_origen VARCHAR(100) NOT NULL,
                       estado VARCHAR(50) NOT NULL,
                       disciplina VARCHAR(100) NOT NULL,
                       foto VARCHAR (255)
            )

        """)
        cursor.execute("""

            CREATE TABLE IF NOT EXISTS usuarios (
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       usuario VARCHAR(50) UNIQUE NOT NULL,
                       password VARCHAR(255) NOT NULL
            )

        """)
        conexion.commit()
        cursor.execute(
            "SELECT * FROM usuarios WHERE usuario = %s",
            ("Melannie",)
        )
        if cursor.fetchone() is None:

            password_hash = bcrypt.hashpw(
            "Melannie1".encode(),
            bcrypt.gensalt()
            ).decode()
            cursor.execute(
                """
                INSERT INTO usuarios (usuario, password)
                VALUES (%s, %s)
                """,
                ("Melannie", password_hash)
            )
            conexion.commit()
        print("✅ Conexión exitosa a MySQL")
    except Exception as e:
        print("❌ Error de conexión")
        print(e)
        return

    matricula = ft.TextField(label="Matricula",width=250, capitalization=ft.TextCapitalization.CHARACTERS, label_style=ft.TextStyle(color=ft.Colors.GREY_400))
    apellido_paterno = ft.TextField(label="Apellido Paterno", width=250,  label_style=ft.TextStyle(color=ft.Colors.GREY_400))
    apellido_materno = ft.TextField(label="Apellido Materno", width=250,  label_style=ft.TextStyle(color=ft.Colors.GREY_400))
    nombres = ft.TextField(label="Nombres", width=250,  label_style=ft.TextStyle(color=ft.Colors.GREY_400))
    curp = ft.TextField(label="Curp", width=250,  label_style=ft.TextStyle(color=ft.Colors.GREY_400))
    especialidad = ft.TextField(label="Especialidad", width=250,  label_style=ft.TextStyle(color=ft.Colors.GREY_400))
    telefono = ft.TextField(label="Telefono", width=250,  label_style=ft.TextStyle(color=ft.Colors.GREY_400))
    ciudad_origen = ft.TextField(label="Ciudad de origen", width=250,  label_style=ft.TextStyle(color=ft.Colors.GREY_400))
    estado = ft.Dropdown(label="Estado", width=250, options=[
        ft.dropdown.Option("Chihuahua"),
        ft.dropdown.Option("Sonora"),
        ft.dropdown.Option("Coahuila"),
        ft.dropdown.Option("Durango")]
        )
    disciplina = ft.Dropdown(label="Disciplina", width=250, options=[
        ft.dropdown.Option("Fútbol"),
        ft.dropdown.Option("Basquetbol"),
        ft.dropdown.Option("Voleibol")
    ] )
    foto = ft.TextField(label="Foto", width=250, label_style=ft.TextStyle(color=ft.Colors.GREY_400))
    resultado = ft.Text()
    resultado.data = False
    busqueda = ft.TextField(
         label="Buscar matrícula o apellido",
        width=350
    )

    imagen_alumno = ft.Image(
        src="https://static.vecteezy.com/system/resources/previews/005/544/753/original/profile-icon-design-free-vector.jpg",
        width=120,
        height=120,
    )

    usuario_login = ft.TextField(
        label="Usuario",
        width=250
    )

    password_login = ft.TextField(
        label="Contraseña",
        width=250,
        password=True,
    can_reveal_password=True
    )

    resultado_login = ft.Text()

    lista_datos = ft.Container(

        content=ft.Column(

            scroll=ft.ScrollMode.AUTO
        ),
        height=180,
        width=350,
        bgcolor=ft.Colors.WHITE,
        padding=5
    )
    

    def limpiar(e):
        matricula.value = ""
        matricula.disabled = False
        apellido_paterno.value = ""
        apellido_materno.value = ""
        nombres.value = ""
        curp.value = ""
        especialidad.value = ""
        telefono.value = ""
        ciudad_origen.value = ""
        estado.value = None
        disciplina.value = None
        foto.value = ""
        imagen_alumno.src = "https://static.vecteezy.com/system/resources/previews/005/544/753/original/profile-icon-design-free-vector.jpg"
        page.update()

    def login(e):
        cursor.execute(
            "SELECT password FROM usuarios WHERE usuario = %s",
            (usuario_login.value,)
        )
        usuario = cursor.fetchone()
        if usuario:
            password_guardada = usuario[0]
            if bcrypt.checkpw(
                password_login.value.encode(),
                password_guardada.encode()
            ):
                resultado_login.value = "Acceso correcto"
                resultado_login.color = "green"
                usuario_login.value = ""
                password_login.value = ""
                contenedor_login.visible = False
                contenedor_sistema.visible = True
            else:
                resultado_login.value = "Contraseña incorrecta"
                resultado_login.color = "red"
        else:
            resultado_login.value = "Usuario no encontrado"
            resultado_login.color = "red"
        page.update()

    def consultar(e):
        lista_datos.content.controls.clear()
        if matricula.value: 
            cursor.execute("""
               SELECT *
               FROM alumnos
               WHERE matricula = %s
            """,(matricula.value.upper(),))
            alumno = cursor.fetchone()
            if alumno:
                matricula.value = alumno[0]
                apellido_paterno.value = alumno[1]
                apellido_materno.value = alumno[2]
                nombres.value = alumno[3]
                curp.value = alumno[4]
                especialidad.value = alumno[5]
                telefono.value = alumno[6]
                ciudad_origen.value = alumno[7]
                estado.value = alumno[8]
                disciplina.value = alumno[9]
                foto.value = alumno[10]
                if alumno[10]:
                    imagen_alumno.src = alumno[10]
                else:
                    imagen_alumno.src = "https://static.vecteezy.com/system/resources/previews/005/544/753/original/profile-icon-design-free-vector.jpg"

                matricula.disabled = True

                resultado.value = "Alumno encontrado"
                resultado.color = "green"
            else:
               resultado.value = "Matricula no encontrada"
               resultado.color = "red"
            page.update()
            cargar_lista()
            return
        elif apellido_paterno.value:
            cursor.execute("""
               SELECT matricula,
               apellido_paterno,
               apellido_materno,
               nombres
               FROM alumnos
               WHERE apellido_paterno LIKE %s
            """,(f"%{apellido_paterno.value}%",))
        else:
            cursor.execute("""
                SELECT matricula,
                apellido_paterno,
                apellido_materno,
                nombres
                FROM alumnos
            """)
        registros = cursor.fetchall()
        if not registros:
            resultado.value = "No se encontraron registros"
            resultado.color = "orange"
        else:
            for matr, ap_pate, ap_mate, nom in registros:
                lista_datos.content.controls.append(
                    ft.ListTile(
                        title=ft.Text(f"{matr} - {nom}"),
                        subtitle=ft.Text(f"{ap_pate} {ap_mate}"),
                        on_click=lambda e, m=matr: cargar_alumno(m)
                    )
                )
            resultado.value = f"Se encontraron {len(registros)} alumnos"
            resultado.color = "blue"
        page.update()

    def guardar(e):
        if matricula.disabled:
            resultado.value = "Use Actualizar para modificar un alumno existente"
            resultado.color = "orange"
            page.update()
            return
        
        if (
            not matricula.value or
            not apellido_paterno.value or
            not apellido_materno.value or
            not nombres.value or
            not curp.value or
            not especialidad.value or
            not telefono.value or
            not ciudad_origen.value or
            not estado.value or
            not disciplina.value or
            not foto.value
        ):
            resultado.value = "Complete todos los campos"
            resultado.color = "red"
            page.update()
            return            
        curp.value = curp.value.upper()
        matricula.value = matricula.value.upper()
        if len(curp.value) != 18:
            resultado.value = "La CURP debe tener 18 caracteres"
            resultado.color = "red"
            page.update()
            return
        if not telefono.value.isdigit() or len(telefono.value) != 10:
            resultado.value = "El teléfono debe tener 10 dígitos"
            resultado.color = "red"
            page.update()
            return
        
        if not (
            foto.value.lower().endswith(".jpg")
            or foto.value.lower().endswith(".jpeg")
            or foto.value.lower().endswith(".png")
        ):
           resultado.value = "La foto debe ser JPG o PNG"
           resultado.color = "red"
           page.update()
           return

        sql = """
        INSERT INTO alumnos (
        matricula, 
        apellido_paterno,
        apellido_materno,
        nombres,
        curp,
        especialidad,
        telefono,
        ciudad_origen,
        estado,
        disciplina,
        foto
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        
        valores = (
            matricula.value,
            apellido_paterno.value,
            apellido_materno.value,
            nombres.value,
            curp.value,
            especialidad.value,
            telefono.value,
            ciudad_origen.value,
            estado.value,
            disciplina.value,
            foto.value
        )
        try:
            cursor.execute(sql, valores)
            conexion.commit()
            cargar_lista()
            limpiar(None)
            resultado.value = "Alumno guardado correctamente"
            resultado.color ="green"
        except Exception as error:
            resultado.value = f"Error: {error}"
        page.update()


    def actualizar(e):
        if (
            not matricula.value or
            not apellido_paterno.value or
            not apellido_materno.value or
            not nombres.value or
            not curp.value or
            not especialidad.value or
            not telefono.value or
            not ciudad_origen.value or
            not estado.value or
            not disciplina.value or
            not foto.value
        ):
            resultado.value = "Complete todos los campos"
            resultado.color = "red"
            page.update()
            return
        if len(curp.value) != 18:
            resultado.value = "La CURP debe tener 18 caracteres"
            resultado.color = "red"
            page.update()
            return
        curp.value = curp.value.upper()
        if not telefono.value.isdigit() or len(telefono.value) != 10:
            resultado.value = "El teléfono debe tener 10 dígitos"
            resultado.color = "red"
            page.update()
            return
        
        if not (
            foto.value.lower().endswith(".jpg")
            or foto.value.lower().endswith(".jpeg")
            or foto.value.lower().endswith(".png")
        ):
           resultado.value = "La foto debe ser JPG o PNG"
           resultado.color = "red"
           page.update()
           return
        
        try:
            cursor.execute("""
                UPDATE alumnos
                SET
                    apellido_paterno = %s,
                    apellido_materno = %s,
                    nombres = %s,
                    curp = %s,
                    especialidad = %s,
                    telefono = %s,
                    ciudad_origen = %s,
                    estado = %s,
                    disciplina = %s,
                    foto = %s
                WHERE matricula = %s
            """, (
                apellido_paterno.value,
                apellido_materno.value,
                nombres.value,
                curp.value.upper(),
                especialidad.value,
                telefono.value,
                ciudad_origen.value,
                estado.value,
                disciplina.value,
                foto.value,
                matricula.value.upper()
            ))
            conexion.commit()
            cargar_lista()
            if cursor.rowcount > 0:
                resultado.value = "Alumno actualizado correctamente"
                resultado.color = "green"
            else:
                resultado.value = "Matrícula no encontrada"
                resultado.color = "orange"
        except Exception as error:
            resultado.value = f"Error: {error}"
            resultado.color = "red"
        page.update()
         


    def confirmar_eliminacion(e):
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirmar eliminación"),
            content=ft.Text("¿Está seguro de eliminar este alumno?"),
            actions=[
                ft.TextButton(
                    "Sí",
                    on_click=lambda e: eliminar(e)
                ),
                ft.TextButton(
                    "No",
                    on_click=lambda e: cerrar_dialogo(dlg)
                )
            ] 
        )

        page.overlay.append(dlg)
        dlg.open = True
        page.update()
 
    def cerrar_dialogo(dlg):
        dlg.open = False
        page.update()

    def eliminar(e):
        if not matricula.value:
            resultado.value = "Ingrese una matrícula"
            resultado.color = "red"
            page.update()
            return

        try:
            cursor.execute(
                "DELETE FROM alumnos WHERE matricula = %s",
                (matricula.value.upper(),)
            )
            conexion.commit()
            if cursor.rowcount > 0:
                resultado.value = "Alumno eliminado correctamente"
                resultado.color = "green"
                limpiar(None)
                cargar_lista()
            else:
                resultado.value = "Matrícula no encontrada"
                resultado.color = "orange"
        except Exception as error:
            resultado.value = f"Error: {error}"
            resultado.color = "red"
        page.update()

    def cargar_lista():
        lista_datos.content.controls.clear()

        cursor.execute("""
            SELECT matricula,
                   apellido_paterno,
                   apellido_materno,
                   nombres
            FROM alumnos
            ORDER BY apellido_paterno
        """)

        registros = cursor.fetchall()

        for matr, ap_pat, ap_mat, nom in registros:

            lista_datos.content.controls.append(
                ft.ListTile(
                    title=ft.Text(f"{nom}"),
                    subtitle=ft.Text(
                        f"{matr} - {ap_pat} {ap_mat}"
                    ),
                    on_click=lambda e, m=matr: cargar_alumno(m)
                )
            )
        page.update()

    def cargar_alumno(matricula_buscar):
        cursor.execute("""
            SELECT *
            FROM alumnos
            WHERE matricula = %s
        """, (matricula_buscar,))

        alumno = cursor.fetchone()

        if alumno:
            matricula.value = alumno[0]
            apellido_paterno.value = alumno[1]
            apellido_materno.value = alumno[2]
            nombres.value = alumno[3]
            curp.value = alumno[4]
            especialidad.value = alumno[5]
            telefono.value = alumno[6]
            ciudad_origen.value = alumno[7]
            estado.value = alumno[8]
            disciplina.value = alumno[9]
            foto.value = alumno[10]
            matricula.disabled = True

            if alumno[10]:
                imagen_alumno.src = alumno[10]

            page.update()

    def buscar(e): 
        lista_datos.content.controls.clear()

        cursor.execute("""
            SELECT matricula,
                   apellido_paterno,
                    apellido_materno,
                    nombres
            FROM alumnos
            WHERE matricula LIKE %s
               OR apellido_paterno LIKE %s
               OR apellido_materno LIKE %s
            ORDER BY apellido_paterno
        """,
        (
            f"%{busqueda.value}%",
            f"%{busqueda.value}%",
            f"%{busqueda.value}%"
        ))
        registros = cursor.fetchall()
        for matr, ap_pat, ap_mat, nom in registros:
            lista_datos.content.controls.append(
                ft.ListTile(
                    title=ft.Text(nom),
                    subtitle=ft.Text(
                        f"{matr} - {ap_pat} {ap_mat}"
                    ),
                    on_click=lambda e, m=matr: cargar_alumno(m)
                )
            )

        page.update()

    def salir(e):
        cursor.close()
        conexion.close()
        sys.exit()


# INTERFAZ
    
    btn_buscar = ft.ElevatedButton(
        
        "Buscar",
        on_click=buscar
    )
    
    btn_guardar = ft.ElevatedButton(

        "Guardar",
        on_click=guardar,
        width=100
    )
    btn_consultar = ft.ElevatedButton(

        "Consultar",
        on_click=consultar,
        width=110
    )
    btn_actualizar = ft.ElevatedButton(

        "Actualizar",
        on_click=actualizar,
        width=115
    )
    btn_eliminar = ft.ElevatedButton(

        "Eliminar",
        on_click=confirmar_eliminacion,
        width=105
    )
    btn_limpiar = ft.ElevatedButton(

        "Limpiar",
        on_click=limpiar,
        width=100
    )
    btn_salir = ft.ElevatedButton(

        "Salir",
        on_click=salir,
        width=100,

        bgcolor="red",
        color="white"
    )
    btn_login = ft.ElevatedButton(
        "Iniciar sesión",
        on_click=login
    )
    fila1 = ft.Row(
        [
            btn_guardar,
            btn_consultar,
            btn_actualizar
        ],
        alignment=ft.MainAxisAlignment.CENTER 
    )
    fila2 = ft.Row(
        [
            btn_eliminar,
            btn_limpiar,
            btn_salir
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    contenedor_login = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Inicio de sesión",
                    size=22,
                    weight="bold"
                ),
                usuario_login,
                password_login,
                btn_login,
                resultado_login
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        width=400,
        padding=20,
        bgcolor=ft.Colors.WHITE,
        border_radius=15
    )

    contenedor_sistema = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "SISTEMA DE ALUMNOS",
                    size=22,
                    weight="bold",
                    color="black"
                ),

                matricula,
                apellido_paterno,
                apellido_materno,
                nombres,
                curp,
                especialidad,
                telefono,
                ciudad_origen,
                estado,
                disciplina,
                foto,
                imagen_alumno,

                fila1,
                fila2,

                resultado,

                busqueda,
                btn_buscar,

                lista_datos
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        ),
        width=500,
        padding=20,
        bgcolor=ft.Colors.GREY_100,
        border_radius=15,
        visible=False
    )

    page.add(
        contenedor_login,
        contenedor_sistema,
        
    )
    cargar_lista()

    # consultar(None)

ft.run(main)
