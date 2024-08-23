# Desafío - Métodos y Atributos

Este proyecto contiene una clase `Pizza` que permite a los usuarios realizar pedidos de pizzas con ingredientes específicos y un tipo de masa. El proyecto está organizado en tres archivos principales:

1. `pizza.py`: Define la clase `Pizza` con métodos para validar elementos y realizar pedidos. Este archivo importa las listas de ingredientes y tipos de masa desde `ingredientes.py`.
2. `ingredientes.py`: Contiene las listas de ingredientes proteicos, vegetales y tipos de masa posibles.
3. `evaluaciones.py`: Realiza pruebas sobre la clase `Pizza` y muestra resultados en pantalla.

## Estructura del Proyecto

### ingredientes.py

Este módulo contiene listas de ingredientes posibles que se pueden utilizar para crear una pizza. Las listas están categorizadas en:

- **ingredientes_proteicos**: Contiene opciones como `pollo`, `vacuno`, y `carne vegetal`.
- **ingredientes_vegetales**: Incluye ingredientes como `tomate`, `aceitunas`, y `champiñones`.
- **tipos_de_masa**: Define los tipos de masa posibles, como `tradicional` y `delgada`.

### pizza.py

Este módulo define la clase `Pizza`, que permite al usuario crear una pizza personalizada y validar si la combinación de ingredientes seleccionada es válida. Los métodos principales de la clase son:

- **validar_elemento(elemento, lista_posibles)**: Método estático que verifica si un ingrediente o tipo de masa es válido.
- **realizar_pedido()**: Solicita al usuario ingresar los ingredientes y tipo de masa, y determina si la pizza creada es válida.

### evaluaciones.py

Este módulo evalúa sobre las combinaciones de ingredientes o análisis de pedidos previos. El objetivo principal es realizar varias evaluaciones y mostrar información sobre la clase `Pizza` definida en `pizza.py`.

1. **Mostrar Atributos de Clase:** 
   - Utiliza la función `print()` para mostrar los valores de los atributos de clase de `Pizza` sin crear una instancia de ella.

2. **Validar Elementos:**
   - Verifica si el elemento "salsa de tomate" se encuentra en la lista `["salsa de tomate", "salsa bbq"]` utilizando el método `validar_elemento` de la clase `Pizza`.

3. **Realizar Pedido de Pizza:**
   - Crea una instancia de la clase `Pizza` y llama al método `realizar_pedido()` para que el usuario pueda ingresar los ingredientes y el tipo de masa.

4. **Mostrar Detalles del Pedido:**
   - Después de que el usuario haya ingresado los ingredientes y el tipo de masa, muestra los ingredientes seleccionados y si la pizza es válida o no.

5. **Mostrar Error Intencionado:**
   - Intenta acceder al atributo `es_pizza_valida` de la clase `Pizza` sin crear una instancia, lo que genera un error intencionado para demostrar la diferencia entre atributos de clase y atributos de instancia.

## Instrucciones de uso

1. Asegúrate de que los tres archivos (`pizza.py`, `ingredientes.py`, `evaluaciones.py`) estén en el mismo directorio.
2. Ejecuta `evaluaciones.py` para interactuar con el sistema de pedidos de pizzas y verificar si los ingredientes ingresados son válidos.
3. Sigue las instrucciones en pantalla para ingresar los ingredientes y tipo de masa.

## Requerimientos

- Python 3.x

## Ejecución

```bash
python evaluaciones.py
```
## Autores y Autoras

- [Rosa Rubio](https://github.com/PaulinaRubioP)
- [Valery Maragaño](https://github.com/Valyxp)
- [Marco Alvarado](https://github.com/7pixel-cl)
- [Esteban Hernández](https://github.com/stivhc)

⌨️ con ❤️ por el Grupo 5 - G20 😊
