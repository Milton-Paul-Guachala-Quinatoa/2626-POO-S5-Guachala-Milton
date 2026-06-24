class Cliente:

    def __init__(
        self,
        nombre: str,
        correo: str,
        edad: int,
        activo: bool
    ):

        # Identificadores descriptivos para almacenar
        # la información de cada cliente

        self.nombre = nombre
        self.correo = correo

        # Tipo de dato numérico entero

        self.edad = edad

        # Tipo de dato lógico

        self.activo = activo

    def mostrar_informacion(self) -> str:

        # Retorna una cadena de texto con la
        # información principal del cliente

        return (
            f"{self.nombre} | "
            f"{self.correo}"
        )

    def __str__(self) -> str:

        # Representación en texto del objeto Cliente

        return (
            f"{self.nombre} "
            f"({self.edad} años)"
            f" | {self.correo}"
        )