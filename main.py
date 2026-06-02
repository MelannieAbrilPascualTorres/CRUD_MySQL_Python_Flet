
import flet as ft

import mysql.connector

import sys

def main(page: ft.Page):

    page.title = "CRUD Usuarios MySQL"

    page.bgcolor = ft.Colors.LIME_100

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    try:
        conn = mysql.connector.connect(

            host="localhost", 
            user="root",       
            password="admin"    
        )

        cursor = conn.cursor()

        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS crud_flet"
        )
        cursor.execute(
            "USE crud_flet"
        )

        cursor.execute("""

            CREATE TABLE IF NOT EXISTS usuarios2 (

                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100),
                correo VARCHAR(100),
                edad INT

            )

        """)

        conn.commit()

        print("✅ Conexión exitosa a MySQL")

    except Exception as e:

        print("❌ Error de conexión")
        print(e)

        return

    id_usuario = ft.TextField(

        label="ID",
        width=250,

        read_only=True,

        label_style=ft.TextStyle(color=ft.Colors.GREY_400)
    )


    nombre = ft.TextField(
        label="Nombre",

        autofocus=True,
        width=250,
        label_style=ft.TextStyle(color=ft.Colors.GREY_400)
    )

    correo = ft.TextField(label="Correo",width=250,label_style=ft.TextStyle(color=ft.Colors.GREY_400))

    edad = ft.TextField(label="Edad", width=250,  label_style=ft.TextStyle(color=ft.Colors.GREY_400))

    resultado = ft.Text()

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

        # Limpiar campos
        id_usuario.value = ""
        nombre.value = ""
        correo.value = ""
        edad.value = ""

        resultado.value = ""

        nombre.focus()

        page.update()

    def consultar(e):

        lista_datos.content.controls.clear()

        cursor.execute(

            "SELECT id, nombre, correo, edad FROM usuarios2"
        )

        registros = cursor.fetchall()

        for id_, nom, cor, ed in registros:

            def seleccionar(
                e,
                id_=id_,
                nom=nom,
                cor=cor,
                ed=ed
            ):

                id_usuario.value = str(id_)
                nombre.value = nom
                correo.value = cor
                edad.value = str(ed)

                resultado.value = f"Registro seleccionado ID: {id_}"
                resultado.color = "blue"

                page.update()

            lista_datos.content.controls.append(

                ft.ListTile(

                    title=ft.Text(
                        f"{nom} ({ed})"
                    ),

                    subtitle=ft.Text(cor),

                    on_click=seleccionar
                )
            )

        page.update()

    def guardar(e):
        
        if not nombre.value or not correo.value or not edad.value:

            resultado.value = "⚠️ Campos obligatorios"
            resultado.color = "red"

            page.update()
            return

        if not edad.value.isdigit():

            resultado.value = "⚠️ Edad inválida"
            resultado.color = "red"

            edad.value = ""
            edad.focus()

            page.update()
            return

        sql = """

            INSERT INTO usuarios2
            (nombre, correo, edad)

            VALUES (%s, %s, %s)

        """

        valores = (

            nombre.value,
            correo.value,
            edad.value
        )

        cursor.execute(sql, valores)

        conn.commit()

        resultado.value = "✅ Registro guardado"
        resultado.color = "green"

        limpiar(None)

        consultar(None)

        page.update()

    def actualizar(e):
        if not id_usuario.value:

            resultado.value = "⚠️ Selecciona un registro"
            resultado.color = "red"

            page.update()
            return

        sql = """

            UPDATE usuarios2

            SET
                nombre=%s,
                correo=%s,
                edad=%s

            WHERE id=%s

        """
        
        valores = (

            nombre.value,
            correo.value,
            edad.value,
            id_usuario.value
        )

        cursor.execute(sql, valores)

        conn.commit()

        resultado.value = "✏️ Registro actualizado"
        resultado.color = "blue"

        consultar(None)

        page.update()
        
    def eliminar(e):

        if not id_usuario.value:

            resultado.value = "⚠️ Selecciona un registro"
            resultado.color = "red"

            page.update()
            return

        sql = """

            DELETE FROM usuarios2
            WHERE id=%s

        """

        valores = (id_usuario.value,)

        cursor.execute(sql, valores)

        conn.commit()

        if cursor.rowcount > 0:

            resultado.value = "🗑️ Registro eliminado"
            resultado.color = "red"

            limpiar(None)
            consultar(None)

        else:

            resultado.value = "⚠️ Registro no encontrado"
            resultado.color = "orange"

        page.update()
        
    def salir(e):

        cursor.close()

        conn.close()

        sys.exit()
        
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
        on_click=eliminar,
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

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "CRUD USUARIOS MYSQL",
                        size=22,
                        weight="bold",
                        color="black"
                    ),

                    id_usuario,
                    nombre,
                    correo,
                    edad,

                    fila1,
                    fila2,

                    resultado,

                    lista_datos
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            width=420,
            padding=20,
            bgcolor=ft.Colors.GREY_100,
            border_radius=15
        )
    )*******************************************

    consultar(None)


ft.run(main)