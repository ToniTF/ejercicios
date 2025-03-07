def mostrar_horcado(intentos_restantes):
    estados = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """,
        """
           ------
           |
           |
           |
           |
           |
        """,
    ]
    return estados[intentos_restantes] if intentos_restantes >= 0 else estados[0]


def mostrar_progreso(palabra_oculta, letras_adivinadas):
    progreso = ''.join(letra if letra in letras_adivinadas else '_' for letra in palabra_oculta)
    return progreso