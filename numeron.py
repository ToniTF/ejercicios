def es_primo(num):
    """Verifica si un número es primo"""
    # Los números menores o iguales a 1 no son primos por definición
    if num <= 1:
        return False
    
    # 2 y 3 son números primos
    if num <= 3:
        return True
    
    # Si es divisible por 2 o por 3, no es primo
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    # Comenzamos a verificar desde 5, aumentando de 6 en 6
    # Esto es una optimización porque todos los primos mayores que 3 
    # son de la forma 6k±1
    i = 5
    # Solo necesitamos comprobar hasta la raíz cuadrada del número
    while i * i <= num:
        # Verificamos si el número es divisible por i o por i+2
        # Esto cubre las formas 6k-1 y 6k+1
        if num % i == 0 or num % (i + 2) == 0:
            return False
        # Incrementamos i en 6 para continuar con la optimización
        i += 6
    
    # Si no encontramos divisores, el número es primo
    return True

def generar_n_primos(n):
    """Genera los primeros n números primos"""
    # Lista que almacenará los números primos encontrados
    primos = []
    # Comenzamos desde el primer número primo
    numero = 2
    
    # Continuamos hasta tener n números primos
    while len(primos) < n:
        # Si el número es primo, lo añadimos a la lista
        if es_primo(numero):
            primos.append(numero)
        # Pasamos al siguiente número
        numero += 1
    
    # Devolvemos la lista con los n primeros números primos
    return primos

def main():
    try:
        # Solicitamos al usuario la cantidad de números primos a generar
        n = int(input("Ingrese la cantidad de números primos que desea generar: "))
        
        # Verificamos que el número sea positivo
        if n <= 0:
            print("Por favor ingrese un número entero positivo.")
            return
        
        # Generamos los n primeros números primos
        numeros_primos = generar_n_primos(n)
        
        # Mostramos los resultados
        print(f"\nLos primeros {n} números primos son:")
        # Enumeramos los primos para mostrarlos con su posición
        for i, primo in enumerate(numeros_primos, 1):
            print(f"{i}. {primo}")
        
    except ValueError:
        # Capturamos el error si el usuario no ingresa un número válido
        print("Error: Debe ingresar un número entero válido.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()