# Python_Biblioteca

Gestor de biblioteca por consola desarrollado en Python para 2.º de DAW. Permite consultar, buscar, prestar y devolver libros, además de dar de alta nuevos libros y socios. Los datos se guardan en ficheros de texto y cada operación importante queda registrada en un log.

## Vídeo de presentación

[Ver vídeo en Drive](PEGAR_AQUÍ_EL_ENLACE)

## Requisitos

- Python 3.10 o superior (el código usa anotaciones del tipo `int | None`).
- No hace falta instalar ninguna librería externa: solo se usa la biblioteca estándar.

## Cómo ejecutar el proyecto

1. Clona el repositorio o descomprime el proyecto.
2. Entra en la carpeta del proyecto:

   ```bash
   cd python_biblioteca
   ```

3. Ejecuta el programa:

   ```bash
   python _main.py
   ```

   En Linux o macOS puede que tengas que usar `python3 _main.py`.

Al arrancar, el programa carga los libros y los socios desde la carpeta `_data/` y muestra cuántos ha cargado. Si la carpeta `_data/` no existe, se crea automáticamente.

## Menú

El menú es cíclico: se vuelve a mostrar después de cada operación hasta que se elige la opción 8.

| Opción | Descripción |
|--------|-------------|
| 1 | Mostrar todos los libros |
| 2 | Mostrar los libros disponibles |
| 3 | Buscar libros por término del título (sin distinguir mayúsculas) |
| 4 | Prestar un libro a un socio (se piden el código del libro y el del socio) |
| 5 | Devolver el libro de un socio (se pide el código del socio) |
| 6 | Mostrar los socios que tienen un libro prestado |
| 7 | Añadir un libro o un socio |
| 8 | Acabar (guarda los datos y sale) |

### Reglas de los préstamos

- Un socio solo puede tener un libro a la vez.
- Un libro solo puede estar prestado a un socio a la vez.
- Si el libro o el socio no existen, o no se cumple alguna de las reglas anteriores, se lanza una excepción personalizada (`LendingError`) y el programa muestra el motivo sin cerrarse.

## Estructura del proyecto

El proyecto sigue una arquitectura **MVC** con **DAOs** para acceder a los datos.

```
python_biblioteca/
├── _main.py                 # Punto de entrada: define las rutas y arranca el controlador
├── controller.py            # Controlador: menú cíclico y flujo de cada opción
├── view.py                  # Vista: todos los input() y print() del programa
├── models/
│   ├── book.py              # Clase Book
│   └── member.py            # Clase Member
├── daos/
│   ├── dao_books.py         # DaoBooks: altas, bajas, modificaciones y búsquedas de libros
│   ├── dao_members.py       # DaoMembers: altas, bajas, modificaciones y búsquedas de socios
│   ├── dao_db.py            # ManagerDB: lectura y escritura de los ficheros de texto
│   └── dao_library.py       # ManagerLibrary: lógica de préstamos, devoluciones y log
├── errors/
│   └── lending_error.py     # Excepción personalizada LendingError
└── _data/
    ├── db_books.txt         # Libros
    ├── db_members.txt       # Socios
    └── log.txt              # Registro de operaciones
```

Reparto de responsabilidades:

- **Modelos**: representan un libro y un socio, y contienen la lógica propia de cada uno (`lend()`, `free()`, `has_book()`...).
- **DAOs**: no imprimen nada. Devuelven `True`/`False` o el objeto pedido, y es el controlador quien decide qué mostrar.
- **Vista**: es la única capa que interactúa con el usuario.
- **Controlador**: conecta la vista con la lógica de la biblioteca y gestiona los errores.

## Formato de los ficheros

Los campos se separan con `;` y hay un registro por línea.

**`_data/db_books.txt`**: `código;título;autor;año;categoría;socio`

```
0;El libro troll;El rubius;2016;Humor;free
```

Si el libro está disponible, el último campo es `free`. Si está prestado, contiene el código del socio.

**`_data/db_members.txt`**: `código;nombre;email;libro`

```
0;Nombre Apellido;correo@ejemplo.com;none
```

Si el socio no tiene ningún libro, el último campo es `none`. Si tiene uno, contiene el código del libro.

**`_data/log.txt`**: `[Fecha][evento][detalles]`

```
[2026-11-10 13:13:09][NUEVO_LIBRO][Libro añadido: El libro troll]
```

Eventos que se registran: `NUEVO_LIBRO`, `NUEVO_SOCIO`, `PRESTAMO` y `DEVOLUCION`.

## Persistencia

Los cambios se guardan en los ficheros de texto después de cada préstamo, devolución o alta, y de nuevo al salir con la opción 8. Si el programa se cierra de forma brusca, solo se pierde lo que no se haya guardado todavía.

## Posibles mejoras

- Añadir al menú las opciones de **modificar y eliminar** libros y socios (los DAOs ya tienen `update_*` y `remove_*`, solo falta conectarlos con el controlador y la vista).
- Validar los datos de entrada: formato del email, año de publicación en un rango razonable y evitar socios o libros duplicados.
- Permitir que un socio tenga **varios libros** a la vez, con un límite configurable.
- Guardar **fecha de préstamo y fecha límite de devolución**, y avisar de los préstamos vencidos.
- Mostrar el **historial de préstamos** de un libro o de un socio a partir del log.
- Sustituir los ficheros de texto por una base de datos (por ejemplo, **SQLite**) para evitar problemas con el carácter `;` dentro de los campos.
- Añadir **tests unitarios** (`unittest` o `pytest`) para los modelos y los DAOs.
- Crear una interfaz gráfica o una versión web de la aplicación.

## Autor

Nombre y apellidos — 2.º DAW
