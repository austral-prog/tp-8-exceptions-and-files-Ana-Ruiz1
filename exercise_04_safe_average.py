# Ejercicio 4 - Promedio seguro con manejo de errores


def safe_average(filename):
    """
    Lee un archivo donde hay UN número por línea y retorna el promedio de
    los números válidos (como float).

    Reglas:
    - Las líneas que no se puedan convertir a float deben ignorarse (usar
      try/except ValueError internamente).
    - Las líneas vacías también se ignoran.
    - Si el archivo no existe, propagar FileNotFoundError.
    - Si el archivo existe pero no contiene ningún número válido, lanzar
      ValueError("no valid numbers").

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        float - promedio de los números válidos.

    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si no hay números válidos en el archivo.

    Ejemplo:
        # archivo contiene: "10\n20\nno_es_un_numero\n30\n"
        safe_average("numeros.txt") -> 20.0
    """
    try:
        with open(filename, 'r') as archivo:
            contenido = archivo.read()
            lista_numeros = contenido.split()
            if len(lista_numeros) > 0:
                suma = 0
                for linea in lista_numeros:
                    suma += float(linea)
                promedio = suma / len(lista_numeros)
                return promedio
    except FileNotFoundError:
        raise FileNotFoundError("El archivo no fue encontrado")
    except ValueError:
        print("no valid numbers")
