class Juego:
    def __init__(self, palabra_oculta):
        self.palabra_oculta = palabra_oculta.lower()
        self.intentos_restantes = 6
        self.letras_adivinadas = []
        self.palabra_actual = "_" * len(self.palabra_oculta)

    def iniciar_juego(self):
        print("¡Bienvenido al juego del ahorcado!")
        print(f"La palabra tiene {len(self.palabra_oculta)} letras.")
        self.mostrar_progreso()

    def adivinar_letra(self, letra):
        if letra in self.letras_adivinadas:
            print("Ya has adivinado esa letra.")
            return False

        self.letras_adivinadas.append(letra)

        if letra in self.palabra_oculta:
            self.actualizar_palabra_actual(letra)
            print(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
        else:
            self.intentos_restantes -= 1
            print(f"Lo siento, la letra '{letra}' no está en la palabra. Te quedan {self.intentos_restantes} intentos.")

        self.mostrar_progreso()
        return True

    def actualizar_palabra_actual(self, letra):
        nueva_palabra = ""
        for i in range(len(self.palabra_oculta)):
            if self.palabra_oculta[i] == letra:
                nueva_palabra += letra
            else:
                nueva_palabra += self.palabra_actual[i]
        self.palabra_actual = nueva_palabra

    def mostrar_progreso(self):
        """Muestra el estado actual del juego"""
        print("\nPalabra: " + " ".join(self.palabra_actual))
        print("Intentos restantes:", self.intentos_restantes)
        print("Letras adivinadas:", ", ".join(sorted(self.letras_adivinadas)))
        print(self.dibujar_ahorcado())
    
    def ha_ganado(self):
        """Verifica si el jugador ha ganado"""
        return "_" not in self.palabra_actual
    
    def ha_perdido(self):
        """Verifica si el jugador ha perdido"""
        return self.intentos_restantes <= 0
    
    def jugar(self):
        """Inicia el juego y maneja el bucle principal"""
        self.iniciar_juego()
        
        while not self.ha_ganado() and not self.ha_perdido():
            letra = input("\nIngresa una letra: ").lower()
            
            if not letra.isalpha() or len(letra) != 1:
                print("Por favor, ingresa una sola letra.")
                continue
                
            self.adivinar_letra(letra)
        
        if self.ha_ganado():
            print(f"\n¡Felicidades! Has adivinado la palabra: {self.palabra_oculta}")
        else:
            print(f"\n¡Oh no! Te has quedado sin intentos. La palabra era: {self.palabra_oculta}")
    
    def dibujar_ahorcado(self):
        """Devuelve el dibujo ASCII del ahorcado según los intentos restantes"""
        dibujos = [
            """
                --------
                |      |
                |      O
                |     /|\\
                |     / \\
                |
              -----
            """,
            """
                --------
                |      |
                |      O
                |     /|\\
                |     / 
                |
              -----
            """,
            """
                --------
                |      |
                |      O
                |     /|\\
                |      
                |
              -----
            """,
            """
                --------
                |      |
                |      O
                |     /|
                |      
                |
              -----
            """,
            """
                --------
                |      |
                |      O
                |      |
                |      
                |
              -----
            """,
            """
                --------
                |      |
                |      O
                |      
                |      
                |
              -----
            """,
            """
                --------
                |      |
                |      
                |      
                |      
                |
              -----
            """
        ]
        return dibujos[self.intentos_restantes]