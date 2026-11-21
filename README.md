<div align="center">

# 🛒 Sistema de Gestión de Usuarios y Productos

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Colorama](https://img.shields.io/badge/CLI-Colorama-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)

**Aplicación de consola interactiva desarrollada en Python con persistencia de datos en SQLite.**  
Permite gestionar el registro y acceso de usuarios, así como administrar un inventario completo de productos de forma rápida y segura.

</div>

---

## ✨ Funcionalidades

### 👤 Módulo de Usuarios
- **Registro con validación:** Alta de nuevos usuarios verificando que el nombre de usuario no exista previamente en la base de datos.
- **Contraseña segura:** Validación estricta de clave numérica de **4 dígitos** ingresada de forma oculta en consola mediante `getpass`, con confirmación explícita antes de guardar.
- **Inicio de sesión (Login):** Autenticación contra la base de datos SQLite para habilitar el acceso al menú de gestión.

### 📦 Módulo de Productos (CRUD)
- **➕ Agregar productos:** Carga de productos indicando `nombre`, `precio` y `categoría`, evitando registros duplicados.
- **📋 Mostrar productos:** Visualización tabular en consola de todo el inventario almacenado (con aviso si la base se encuentra vacía).
- **🔍 Buscar productos:** Búsqueda instantánea por nombre que devuelve precio y categoría actual.
- **🗑️ Eliminar productos:** Baja de registros existentes con validación previa y confirmación visual.

### 🎨 Interfaz de Consola
- **Experiencia visual mejorada:** Uso de `colorama` para resaltar títulos, menús, alertas de error y confirmaciones de éxito.
- **Navegación estructurada:** Menús interactivos implementados con `match / case`.

---

## 📂 Estructura del Proyecto

```text
entrega-final-python-sql/
│
├── 📄 main.py          # Punto de entrada: menú inicial de Registro (R) e Inicio de Sesión (L)
├── ⚙️ funciones.py     # Lógica principal: autenticación, menú CRUD y consultas a la base de datos
├── 🗄️ datos.db         # Base de datos SQLite generada automáticamente
└── 📘 README.md        # Documentación del proyecto
```

---

## 🗄️ Estructura de la Base de Datos (`datos.db`)

La persistencia se maneja a través de la librería **`dataset`**, organizando la información en dos tablas relacionales:

### Tabla `Usuarios`
| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `id` | `INTEGER (PK)` | Identificador único autoincremental |
| `nombre` | `TEXT` | Nombre del usuario |
| `apellido` | `TEXT` | Apellido del usuario |
| `usuario` | `TEXT` | Nombre de usuario único para iniciar sesión |
| `clave` | `TEXT` | Contraseña numérica de 4 dígitos |

### Tabla `Productos`
| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `id` | `INTEGER (PK)` | Identificador único autoincremental |
| `nombre` | `TEXT` | Nombre del producto |
| `precio` | `FLOAT` | Precio unitario del producto |
| `categoria` | `TEXT` | Categoría a la que pertenece (ej. *bebida, fiambre, lácteo*) |

---

## 🚀 Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   cd TU_REPOSITORIO
   ```

2. **Instalar las dependencias necesarias:**
   ```bash
   pip install dataset colorama
   ```

3. **Ejecutar el programa:**
   ```bash
   python main.py
   ```

---

## 🛠️ Tecnologías Utilizadas

- **[Python 3.10+](https://www.python.org/)** — Lenguaje principal y control de flujo con `match / case`.
- **[SQLite](https://www.sqlite.org/)** — Motor de base de datos ligero y local.
- **[dataset](https://dataset.readthedocs.io/)** — ORM minimalista para interactuar con SQLite usando diccionarios de Python.
- **[Colorama](https://pypi.org/project/colorama/)** — Estilizado y colores ANSI en terminal.
- **[getpass](https://docs.python.org/3/library/getpass.html)** — Entrada segura de contraseñas ocultas en consola.
