from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():

    # Importación de clases desde otros módulos
    # para reutilizar código organizado

    # CREACIÓN DE OBJETOS PRODUCTO (PLATOS ECUATORIANOS)

    producto1 = Producto(
        "Encebollado",
        "Plato típico",
        3.00,
        15,
        True
    )

    producto2 = Producto(
        "Seco de pollo",
        "Plato típico",
        3.50,
        10,
        True
    )

    producto3 = Producto(
        "Hornado",
        "Plato típico",
        8.00,
        8,
        True
    )

    producto4 = Producto(
        "Colada morada",
        "Bebida tradicional",
        2.00,
        20,
        True
    )

    # CREACIÓN DE OBJETOS CLIENTE

    cliente1 = Cliente(
        "Milton Pérez",
        "miltonp@gmail.com",
        20,
        True
    )

    cliente2 = Cliente(
        "Gina López",
        "ginalp@gmail.com",
        22,
        True
    )

    # Creación de un objeto Restaurante

    restaurante = Restaurante()

    # Registro de productos

    restaurante.agregar_producto(producto1)
    restaurante.agregar_producto(producto2)
    restaurante.agregar_producto(producto3)
    restaurante.agregar_producto(producto4)

    # Registro de clientes

    restaurante.agregar_cliente(cliente1)
    restaurante.agregar_cliente(cliente2)

    # Visualización de información

    print("=== PLATOS ECUATORIANOS REGISTRADOS ===")
    restaurante.mostrar_productos()

    print("\n=== CLIENTES REGISTRADOS ===")
    restaurante.mostrar_clientes()


# Punto de inicio del programa

if __name__ == "__main__":
    main()