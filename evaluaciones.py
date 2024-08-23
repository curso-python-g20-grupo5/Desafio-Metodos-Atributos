from pizza import Pizza

# a. Mostrar los valores de los atributos de clase de la clase importada
print("Ingredientes proteicos disponibles:", Pizza.ingredientes_proteicos)
print("Ingredientes vegetales disponibles:", Pizza.ingredientes_vegetales)
print("Tipos de masa disponibles:", Pizza.tipos_de_masa)

# b. Validar si "salsa de tomate" está en la lista ["salsa de tomate", "salsa bbq"]
print(
    "¿Salsa de tomate está en la lista de opciones?",
    Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]),
)

# c. Crear una instancia y solicitar ingredientes y tipo de masa
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

# d. Mostrar los ingredientes y tipo de masa de la instancia, y si es una pizza válida
print("Ingrediente proteico:", mi_pizza.ingrediente_proteico)
print("Primer ingrediente vegetal:", mi_pizza.ingrediente_vegetal1)
print("Segundo ingrediente vegetal:", mi_pizza.ingrediente_vegetal2)
print("Tipo de masa:", mi_pizza.tipo_masa)
# Extra para mostrar precio y tamaño
print("Precio:", mi_pizza.precio)
print("Tamaño:", mi_pizza.tamano)
print("¿Es una pizza válida?", mi_pizza.es_pizza_valida)

# e. Intentar mostrar si la clase Pizza es válida o no (esto debería generar un error)
# El error se genera debido a que es_pizza_valida es un atributo de instancia, no de clase
try:
    print("¿Es la clase Pizza válida?", Pizza.es_pizza_valida)
except AttributeError as e:
    print("Error:", e)
