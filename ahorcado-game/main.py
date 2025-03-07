from src.utils.palabras import cargar_palabras
from src.game import Juego
import random

def main():
    print("¡Bienvenido al Juego del Ahorcado!")
    
    jugar_partida = True
    while jugar_partida:
        # Carga una palabra aleatoria
        palabra_secreta = cargar_palabras()
        
        # Crea una instancia del juego con la palabra seleccionada
        juego = Juego(palabra_secreta)
        
        # Inicia el juego
        juego.jugar()
        
        # Pregunta si quiere jugar de nuevo
        while True:
            respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
            if respuesta in ['s', 'si', 'sí']:
                # Salimos del bucle interno para iniciar un nuevo juego
                break
            elif respuesta in ['n', 'no']:
                print("¡Gracias por jugar! Hasta pronto.")
                jugar_partida = False
                break
            else:
                print("Por favor, responde 's' para sí o 'n' para no.")

if __name__ == "__main__":
    # Inicializa la semilla del generador de números aleatorios
    random.seed()
    main()