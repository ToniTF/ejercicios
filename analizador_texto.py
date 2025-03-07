def analizar_texto(texto):
    """
    Analiza un texto proporcionado y devuelve estadísticas sobre el mismo.
    
    Args:
        texto (str): El texto a analizar
        
    Returns:
        tuple: (número de palabras, número de vocales, número de consonantes, palabra más larga)
    """
    # Verificamos que el texto no esté vacío
    if not texto:
        return 0, 0, 0, ""
    
    # Convertimos el texto a minúsculas para facilitar el análisis
    texto = texto.lower()
    
    # Dividimos el texto en palabras
    palabras = texto.split()
    num_palabras = len(palabras)
    
    # Inicializamos contadores
    vocales = 0
    consonantes = 0
    
    # Definimos las vocales (incluyendo vocales con acentos en español)
    todas_vocales = "aeiouáéíóúü"
    
    # Analizamos cada caracter del texto
    for caracter in texto:
        # Verificamos si es una letra
        if caracter.isalpha():
            if caracter in todas_vocales:
                vocales += 1
            else:
                consonantes += 1
    
    # Encontramos la palabra más larga
    palabra_mas_larga = ""
    for palabra in palabras:
        # Limpiamos la palabra de signos de puntuación
        palabra_limpia = ''.join(c for c in palabra if c.isalpha())
        if len(palabra_limpia) > len(palabra_mas_larga):
            palabra_mas_larga = palabra_limpia
    
    return num_palabras, vocales, consonantes, palabra_mas_larga

def main():
    """Función principal del programa"""
    # Solicitamos al usuario que introduzca un texto
    print("Por favor, introduce un texto para analizar:")
    texto = input()
    
    # Verificamos que el texto no esté vacío
    if not texto.strip():
        print("No has introducido ningún texto.")
        return
    
    # Analizamos el texto
    num_palabras, num_vocales, num_consonantes, palabra_mas_larga = analizar_texto(texto)
    
    # Mostramos los resultados
    print("\nRESULTADOS DEL ANÁLISIS:")
    print("-----------------------")
    print(f"Cantidad de palabras: {num_palabras}")
    print(f"Cantidad de vocales: {num_vocales}")
    print(f"Cantidad de consonantes: {num_consonantes}")
    print(f"Palabra más larga: '{palabra_mas_larga}' ({len(palabra_mas_larga)} letras)")

# Punto de entrada del programa
if __name__ == "__main__":
    main()