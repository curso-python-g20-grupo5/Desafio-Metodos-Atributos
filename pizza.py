from ingredientes import ingredientes_proteicos, ingredientes_vegetales, tipos_de_masa


class Pizza:
    """
    Clase que representa una pizza.

    Atributos:
        ingrediente_proteico (str): El ingrediente proteico de la pizza.
        ingrediente_vegetal1 (str): El primer ingrediente vegetal de la pizza.
        ingrediente_vegetal2 (str): El segundo ingrediente vegetal de la pizza.
        tipo_masa (str): El tipo de masa de la pizza.
        es_pizza_valida (bool): Indica si la pizza es válida según los ingredientes y tipo de masa.

    Métodos:
        validar_elemento(elemento, lista_posibles):
            Valida si un elemento se encuentra en una lista de valores posibles.

        realizar_pedido():
            Solicita al usuario los ingredientes y tipo de masa, y valida si la pizza es correcta.
    """

    # Atributos de clase
    ingredientes_proteicos = ingredientes_proteicos
    ingredientes_vegetales = ingredientes_vegetales
    tipos_de_masa = tipos_de_masa
    precio = "$10.000"
    tamano = "Familiar"

    def __init__(self):
        """
        Inicializa una nueva instancia de la clase Pizza.
        """
        self.ingrediente_proteico = None
        self.ingrediente_vegetal1 = None
        self.ingrediente_vegetal2 = None
        self.tipo_masa = None
        self.es_pizza_valida = False #se es válida solo cuando se validen los ingredientes y la masa

    @staticmethod
    def validar_elemento(elemento, lista_posibles):
        """
        Valida si un elemento se encuentra en una lista de valores posibles.

        Args:
            elemento (str): El elemento a validar.
            lista_posibles (list): Los valores posibles a considerar para el elemento ingresado.

        Returns:
            bool: True si el elemento está en la lista de posibles, False en caso contrario.
        """
        return elemento in lista_posibles

    def realizar_pedido(self):
        """
        Solicita al usuario ingresar los ingredientes y el tipo de masa para la pizza.
        Evalúa si los ingredientes y la masa son válidos, y determina si la pizza es válida.
        """
        # Solicita al usuario que ingrese el ingrediente proteico.
        self.ingrediente_proteico = input("Ingrese un ingrediente proteico: ")

        # Solicita al usuario el primer ingrediente vegetal.
        self.ingrediente_vegetal1 = input("Ingrese el primer ingrediente vegetal: ")

        # Solicita al usuario el segundo ingrediente vegetal.
        self.ingrediente_vegetal2 = input("Ingrese el segundo ingrediente vegetal: ")

        # Solicita al usuario el tipo de masa.
        self.tipo_masa = input("Ingrese el tipo de masa: ")

        # Valida si los ingredientes y la masa ingresados están en las listas
        if (
            self.validar_elemento(self.ingrediente_proteico, ingredientes_proteicos)
            and self.validar_elemento(self.ingrediente_vegetal1, ingredientes_vegetales)
            and self.validar_elemento(self.ingrediente_vegetal2, ingredientes_vegetales)
            and self.validar_elemento(self.tipo_masa, tipos_de_masa)
        ):
            # Si todos los ingredientes y la masa son válidos, la pizza se marca como válida.
            self.es_pizza_valida = True
        else:
            # Si alguno de los ingredientes o la masa no son válidos, la pizza se marca como no válida.
            self.es_pizza_valida = False
