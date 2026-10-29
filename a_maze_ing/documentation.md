## This is to give me context of what I have done and what I'm doing right know


Resumen: lo que tienes por delante
Ya hecho
Parsing del config (funciona, con bugs menores que endurecerás al final)
build_grid: tablero de height filas por width columnas, todo en 15
Constante DIRECTIONS (peso, dx, dy, opuesta)
get_neighbors: devuelve la lista de (letra, (nx, ny)) válidos
DFS de práctica con visited compartido (en el grafo A, B, C)
Lo que viene, en orden

1. Abrir paso (el siguiente)

Recibe: grid, celda actual, dirección.
En la celda actual: poner a 0 el bit de esa dirección.
En el vecino: poner a 0 el bit de la opposite.
Truco: usar & ~peso, que es seguro aunque la pared ya estuviera abierta (restar no lo es).
Prueba: abre una pared en un 3x3 y comprueba a mano que las dos celdas quedan coherentes.

2. DFS sobre la cuadrícula

Nodo = (x, y), visited = set de tuplas.
Vecinos con get_neighbors, barajados (aleatorio).
Si el vecino no está visitado: abrir paso y llamar recursivamente.
Semilla fijada antes de generar (misma semilla, mismo laberinto).
Prueba: 3x3 primero, verificando a mano; luego 20x15.
Después: cambiar a pila explícita para evitar el límite de recursión.

3. Escribir el archivo hexadecimal

Cada celda a un dígito hex, una fila por línea.
Línea vacía, entrada, salida y camino.
Validar con maze_analyzer.py.

Con esto tienes un laberinto perfecto de punta a punta.

Después (resto del proyecto)
Camino más corto (recorrido en grafo sin pesos, respetando paredes) y salida en letras N/E/S/W
El “42”: reservar celdas antes del DFS; omitirlo con error si el tablero es pequeño
Modo PERFECT=False: partir del perfecto, abrir paredes extra, sin zonas 3x3, esquinas y centro abiertos
Visualización en terminal con menú (regenerar, mostrar/ocultar camino, colores, salir)
Entrega: clase única reutilizable, paquete mazegen-*, Makefile, LICENSE.md, .gitignore, README, flake8/mypy limpios
Endurecer parsing y errores (archivo no encontrado, claves que faltan, sin crashes)
Cuidados pendientes en lo que ya tienes
Renombrar DIRECCIONS → DIRECTIONS, clave "O" → "W", "wights" → "weight"
get_neighbors: tipo de retorno list[tuple[str, tuple[int, int]]] y quitar el print
heigh → height, colum → column
Tu siguiente acción
