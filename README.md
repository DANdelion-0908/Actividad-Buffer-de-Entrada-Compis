# Actividad Buffer de Entrada Compis
 
#### Participantes
- Eunice Mata - 21231
- Hector Penedo - 22217

## Explicación
### ¿Qué hace el programa?
El programa simula un búfer de entrada con un tamaño fijo de 10 caracteres y procesa la entrada para extraer lexemas (palabras separadas por espacios) hasta encontrar "eof"

Ejemplo:
```ruby
entrada = list("Esto es un ejemplo de entrada con eof")
```

Regresa:
```
Lexema procesado: Esto
Lexema procesado: es
Lexema procesado: un
Lexema procesado: ejemplo
Lexema procesado: de
Lexema procesado: entrada
Lexema procesado: con
Lexema procesado: eof
```

Esto es realizado por medio de la implementación de una función de cargar buffer, que extrae una porción de la entrada con un tamaño máximo definido, si la porción extraída es menor al tamaño del búfer (porque se alcanzó el final de la entrada), se añade "eof" para indicar el final de la lectura. 

Y una función que hace uso de la carga del buffer para regresar todos los lexemas (cuando encuentre un espacio) y volver a llamar a la carga del buffer hasta que encuentre uno con la palabra "eof"

### Codigo: [Archivo Buffer Simulator](bufferSimulator.py)
