def convertir_longitud(valor, desde, hacia):
    """Convierte entre diferentes unidades de longitud"""
    # Diccionario con factores de conversión a metros
    factores = {
        "mm": 0.001,      # milímetros a metros
        "cm": 0.01,       # centímetros a metros
        "m": 1,           # metros a metros
        "km": 1000,       # kilómetros a metros
        "pulgadas": 0.0254,  # pulgadas a metros
        "pies": 0.3048,   # pies a metros
        "yardas": 0.9144, # yardas a metros
        "millas": 1609.34 # millas a metros
    }
    
    # Convertimos primero a la unidad base (metros) y luego a la unidad destino
    return valor * factores[desde] / factores[hacia]

def convertir_temperatura(valor, desde, hacia):
    """Convierte entre diferentes unidades de temperatura"""
    # Primero convertimos a Celsius como unidad intermedia
    if desde == "celsius":
        celsius = valor
    elif desde == "fahrenheit":
        celsius = (valor - 32) * 5/9
    elif desde == "kelvin":
        celsius = valor - 273.15
    
    # Luego convertimos de Celsius a la unidad destino
    if hacia == "celsius":
        return celsius
    elif hacia == "fahrenheit":
        return (celsius * 9/5) + 32
    elif hacia == "kelvin":
        return celsius + 273.15

def convertir_masa(valor, desde, hacia):
    """Convierte entre diferentes unidades de masa"""
    # Diccionario con factores de conversión a gramos
    factores = {
        "mg": 0.001,      # miligramos a gramos
        "g": 1,           # gramos a gramos
        "kg": 1000,       # kilogramos a gramos
        "oz": 28.3495,    # onzas a gramos
        "lb": 453.592     # libras a gramos
    }
    
    # Convertimos primero a la unidad base (gramos) y luego a la unidad destino
    return valor * factores[desde] / factores[hacia]

def convertir_volumen(valor, desde, hacia):
    """Convierte entre diferentes unidades de volumen"""
    # Diccionario con factores de conversión a litros
    factores = {
        "ml": 0.001,      # mililitros a litros
        "cl": 0.01,       # centilitros a litros
        "l": 1,           # litros a litros
        "m3": 1000,       # metros cúbicos a litros
        "fl_oz": 0.0295735, # onzas líquidas a litros
        "gal": 3.78541    # galones a litros
    }
    
    # Convertimos primero a la unidad base (litros) y luego a la unidad destino
    return valor * factores[desde] / factores[hacia]

def mostrar_menu_principal():
    """Muestra el menú principal de categorías de conversión"""
    print("\n=== CONVERSOR DE UNIDADES ===")
    print("1. Longitud")
    print("2. Temperatura")
    print("3. Masa")
    print("4. Volumen")
    print("0. Salir")
    
    try:
        opcion = int(input("\nSeleccione una categoría (0-4): "))
        return opcion
    except ValueError:
        print("Error: Debe ingresar un número.")
        return -1

def mostrar_menu_longitud():
    """Muestra el menú de conversiones de longitud"""
    unidades = ["mm", "cm", "m", "km", "pulgadas", "pies", "yardas", "millas"]
    
    print("\n--- Conversión de Longitud ---")
    print("Unidades disponibles:")
    for i, unidad in enumerate(unidades, 1):
        print(f"{i}. {unidad}")
    
    try:
        desde = int(input("\nSeleccione la unidad de origen (1-8): ")) - 1
        hacia = int(input("Seleccione la unidad de destino (1-8): ")) - 1
        valor = float(input("Ingrese el valor a convertir: "))
        
        if 0 <= desde < len(unidades) and 0 <= hacia < len(unidades):
            resultado = convertir_longitud(valor, unidades[desde], unidades[hacia])
            print(f"\n{valor} {unidades[desde]} = {resultado:.6f} {unidades[hacia]}")
        else:
            print("Error: Selección de unidad inválida.")
    except ValueError:
        print("Error: Debe ingresar valores numéricos.")

def mostrar_menu_temperatura():
    """Muestra el menú de conversiones de temperatura"""
    unidades = ["celsius", "fahrenheit", "kelvin"]
    
    print("\n--- Conversión de Temperatura ---")
    print("Unidades disponibles:")
    for i, unidad in enumerate(unidades, 1):
        print(f"{i}. {unidad}")
    
    try:
        desde = int(input("\nSeleccione la unidad de origen (1-3): ")) - 1
        hacia = int(input("Seleccione la unidad de destino (1-3): ")) - 1
        valor = float(input("Ingrese el valor a convertir: "))
        
        if 0 <= desde < len(unidades) and 0 <= hacia < len(unidades):
            resultado = convertir_temperatura(valor, unidades[desde], unidades[hacia])
            print(f"\n{valor} {unidades[desde]} = {resultado:.2f} {unidades[hacia]}")
        else:
            print("Error: Selección de unidad inválida.")
    except ValueError:
        print("Error: Debe ingresar valores numéricos.")

def mostrar_menu_masa():
    """Muestra el menú de conversiones de masa"""
    unidades = ["mg", "g", "kg", "oz", "lb"]
    
    print("\n--- Conversión de Masa ---")
    print("Unidades disponibles:")
    for i, unidad in enumerate(unidades, 1):
        print(f"{i}. {unidad}")
    
    try:
        desde = int(input("\nSeleccione la unidad de origen (1-5): ")) - 1
        hacia = int(input("Seleccione la unidad de destino (1-5): ")) - 1
        valor = float(input("Ingrese el valor a convertir: "))
        
        if 0 <= desde < len(unidades) and 0 <= hacia < len(unidades):
            resultado = convertir_masa(valor, unidades[desde], unidades[hacia])
            print(f"\n{valor} {unidades[desde]} = {resultado:.6f} {unidades[hacia]}")
        else:
            print("Error: Selección de unidad inválida.")
    except ValueError:
        print("Error: Debe ingresar valores numéricos.")

def mostrar_menu_volumen():
    """Muestra el menú de conversiones de volumen"""
    unidades = ["ml", "cl", "l", "m3", "fl_oz", "gal"]
    nombres = ["mililitros", "centilitros", "litros", "metros cúbicos", "onzas líquidas", "galones"]
    
    print("\n--- Conversión de Volumen ---")
    print("Unidades disponibles:")
    for i, nombre in enumerate(nombres, 1):
        print(f"{i}. {nombre}")
    
    try:
        desde = int(input("\nSeleccione la unidad de origen (1-6): ")) - 1
        hacia = int(input("Seleccione la unidad de destino (1-6): ")) - 1
        valor = float(input("Ingrese el valor a convertir: "))
        
        if 0 <= desde < len(unidades) and 0 <= hacia < len(unidades):
            resultado = convertir_volumen(valor, unidades[desde], unidades[hacia])
            print(f"\n{valor} {nombres[desde]} = {resultado:.6f} {nombres[hacia]}")
        else:
            print("Error: Selección de unidad inválida.")
    except ValueError:
        print("Error: Debe ingresar valores numéricos.")

def main():
    """Función principal del programa"""
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == 0:
            print("\n¡Gracias por usar el conversor de unidades!")
            break
        elif opcion == 1:
            mostrar_menu_longitud()
        elif opcion == 2:
            mostrar_menu_temperatura()
        elif opcion == 3:
            mostrar_menu_masa()
        elif opcion == 4:
            mostrar_menu_volumen()
        else:
            print("Opción inválida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()