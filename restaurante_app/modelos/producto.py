class Producto:

    def __init__(
        self,
        nombre: str,
        categoria: str,
        precio: float,
        cantidad: int,
        disponible: bool
    ):

        # Identificadores descriptivos para almacenar
        # la información de cada producto

        self.nombre = nombre
        self.categoria = categoria

        # Tipos de datos numéricos

        self.precio = precio
        self.cantidad = cantidad

        # Tipo de dato lógico

        self.disponible = disponible

    def mostrar_informacion(self) -> str:

        # Retorna una cadena de texto con la
        # información principal del producto

        return (
            f"Producto: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Cantidad: {self.cantidad}"
        )

    def __str__(self) -> str:

        # Representación en texto del objeto Producto

        return (
            f"{self.nombre} | "
        f"{self.categoria} | "
        f"${self.precio:.2f} | "
        f"Stock: {self.cantidad}"
    )