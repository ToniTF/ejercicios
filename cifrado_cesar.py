def cifrado_cesar(texto, desplazamiento):
    """
    Codifica un texto utilizando el cifrado César con el desplazamiento especificado.
    
    Args:
        texto (str): El texto a cifrar
        desplazamiento (int): El número de posiciones a desplazar cada letra
    
    Returns:
        str: El texto cifrado
    """
    # Resultado donde almacenaremos el texto cifrado
    texto_cifrado = ""
    
    # Procesamos cada carácter del texto
    for caracter in texto:
        # Ciframos solo letras, manteniendo cualquier otro carácter intacto
        if caracter.isalpha():
            # Determinamos el código ASCII base (65 para mayúsculas, 97 para minúsculas)
            codigo_base = 65 if caracter.isupper() else 97
            
            # Convertimos el carácter a su valor numérico (0-25 para A-Z/a-z)
            valor_numerico = ord(caracter) - codigo_base
            
            # Aplicamos el desplazamiento y usamos módulo 26 para mantenerlo en el rango del alfabeto
            valor_cifrado = (valor_numerico + desplazamiento) % 26
            
            # Convertimos el valor cifrado de nuevo a un carácter
            caracter_cifrado = chr(valor_cifrado + codigo_base)
            
            # Añadimos el carácter cifrado al resultado
            texto_cifrado += caracter_cifrado
        else:
            # Si no es una letra, lo mantenemos sin cambios
            texto_cifrado += caracter
    
    return texto_cifrado

def main():
    """Función principal del programa"""
    # Mostramos un breve título y explicación
    print("=== CIFRADO CÉSAR ===")
    print("Este programa codifica un texto usando el cifrado César.")
    print("El cifrado César desplaza cada letra un número fijo de posiciones en el alfabeto.")
    
    # Solicitamos el texto a cifrar
    texto = input("\nIntroduce el texto que deseas cifrar: ")
    
    # Verificamos que se haya introducido un texto
    if not texto:
        print("No has introducido ningún texto.")
        return
    
    # Solicitamos la clave de desplazamiento
    try:
        desplazamiento = int(input("Introduce la clave de desplazamiento (número entero): "))
    except ValueError:
        print("Error: La clave debe ser un número entero.")
        return
    
    # Ciframos el texto
    texto_cifrado = cifrado_cesar(texto, desplazamiento)
    
    # Mostramos el resultado (añadido debug para verificar)
    print("\nRESULTADO DEL CIFRADO:")
    print("-----------------------")
    print(f"Texto original: {texto}")
    print(f"Clave de desplazamiento: {desplazamiento}")
    print(f"Texto cifrado: {texto_cifrado}")
    
    # Opcional: Mostrar cómo descifrar
    print("\nPara descifrar este texto, usa la misma aplicación con una clave de", -desplazamiento)

# Punto de entrada del programa
if __name__ == "__main__":
    main()