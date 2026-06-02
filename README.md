Trabajo individual:

Especificaciones del Proyecto Final: Sistema CRUD Alumnos (Python + MySQL)
Proyect de Evaluación para la Unidad3: Deberán desarrollar una aplicación con Python-Flet que implemente un sistema CRUD (Create, Read, Update, Delete) conectado a una base de datos relacional (MySQL). 

Objetivo de este proyecto: Alumno deberá demostrar su dominio en la integración de bases de datos, lógica de programación en Python y diseño de interfaces de usuario.

1. Requisitos Técnicos y Arquitectura
Lenguaje de programación: Python 3.x.
Gestor de Base de Datos: MySQL.
Conector: mysql-connector-python o PyMySQL.
Interfaz Gráfica (GUI):  Se utilizará el framework Flet. La aplicación deberá ser multi página (o manejar vistas dinámicas) para separar claramente la pantalla de Login del panel principal del CRUD.
2. Requisitos Funcionales y Módulos del Sistema:

A) Pantalla de Inicio (Login / Control de Acceso)
Antes de acceder al sistema, la aplicación deberá mostrar una pantalla de autenticación.
Formulario de inicio de sesión con campos para Usuario y Contraseña.
Mejora requerida: Las contraseñas en la base de datos no deben guardarse en texto plano; deben implementar encriptación/hashing básico (por ejemplo, utilizando la librería bcrypt o hashlib).
Validación de credenciales con mensajes de error claros en caso de datos incorrectos.
B. Gestión del Perfil del Alumno (Módulo CRUD)
Una vez autenticado, el usuario tendrá acceso al panel principal para gestionar los perfiles de los alumnos. La base de datos y la interfaz deben soportar obligatoriamente los siguientes campos:
Matrícula (Llave primaria / Identificador único)
Apellido Paterno
Apellido Materno
Nombre(s)
CURP (Con validación de formato de 18 caracteres)
Especialidad
Teléfono (A 10 dígitos)
Ciudad de Origen
Estado (Deberá ser un menú desplegable / ComboBox alimentado desde la base de datos o un catálogo estático).
Disciplinas Deportivas (Menú desplegable o checkboxes para selección).
Foto de Perfil: El sistema debe permitir cargar una imagen, mostrarla en la interfaz y almacenarla de manera óptima (se sugiere guardar la ruta local de la imagen o el archivo en formato BLOB en la base de datos).
C. Operaciones CRUD Requeridas
Insertar (Create): Registro de nuevos alumnos validando que los campos obligatorios no estén vacíos.
Consultar (Read): Visualización de los alumnos registrados en una tabla o lista (ej. Treeview en Tkinter). Debe incluir un buscador por matrícula o apellido.
Modificar (Update): Selección de un alumno existente para editar cualquiera de sus campos (excepto la matrícula) y actualizarlo en la base de datos.
Borrar (Delete): Eliminación de registros del sistema, solicitando siempre una confirmación emergente antes de proceder.


Para elevar la calidad del proyecto, se han integrado las siguientes mejoras obligatorias dentro de la nota máxima:Manejo de Excepciones (try-except): El sistema no debe cerrarse inesperadamente si falla la conexión a la base de datos o si se introduce un dato erróneo.Validación de Datos: Restricciones numéricas para el teléfono, mayúsculas automáticas para la CURP y formato correcto de imagen.Diseño de Interfaz (UX/UI): Uso de una paleta de colores armónica, tipografías legibles y distribución limpia de los elementos en pantalla.
4. Entregables y Formato de Envío
El proyecto deberá entregarse en la plataforma digital a más tardar el 8 de Junio] e incluir:Código Fuente: Carpeta del proyecto en Python (archivos .py).Script SQL: Archivo .sql con la estructura de la base de datos (tablas, llaves primarias y algunos registros de prueba).Documento PDF:  capturas de pantalla del funcionamiento del sistema (Login, Inserción, Consulta, Edición y Borrado).