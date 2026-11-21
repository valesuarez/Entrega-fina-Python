Sistema de Gestión de Usuarios y Productos (Python + SQLite)

Aplicación de consola desarrollada en Python que permite registrar e iniciar sesión con usuarios y administrar un inventario de productos almacenado de forma persistente en una base de datos SQLite mediante la librería dataset.

Características principales

Gestión de Usuarios:

Registro: Alta de nuevos usuarios con validación de duplicados y contraseña numérica de 4 dígitos oculta en consola (getpass).

Inicio de sesión (Login): Autenticación contra la base de datos antes de acceder al menú principal.

Gestión de Productos (CRUD):

Agregar productos: Carga de nombre, precio y categoría verificando que el producto no exista previamente.

Mostrar productos: Listado completo de todos los productos registrados en la base de datos.

Buscar productos: Consulta rápida por nombre con visualización de precio y categoría.

Eliminar productos: Baja de productos existentes con confirmación en pantalla.

Interfaz en consola: Uso de colores y estilos mediante colorama para diferenciar mensajes de éxito, advertencia, error y menús.

Estructura del proyecto

├── main.py         # Punto de entrada de la aplicación (menú de Registro / Login)
├── funciones.py    # Lógica de usuarios, menú principal y operaciones sobre productos
├── datos.db        # Base de datos SQLite (tablas: Usuarios y Productos)
└── README.md       # Documentación del proyecto

Tecnologías utilizadas

Python

SQLite

dataset — Abstracción sencilla para bases de datos SQL.

Colorama — Colores ANSI multiplataforma en terminal.
