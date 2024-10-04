import argparse

# Crear el parser de argumentos
parser = argparse.ArgumentParser(description="Ingresa un número")
parser.add_argument('numero', type=int, help="Número ingresado por el usuario")

# Parsear los argumentos
args = parser.parse_args()

# Obtener el número ingresado
numero = args.numero

print(f"El número ingresado es: {numero}")
