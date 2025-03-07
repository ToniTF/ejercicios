import random
import os

def cargar_palabras():
    """
    Carga la lista de palabras desde un archivo y devuelve una palabra aleatoria
    
    Returns:
        str: Una palabra aleatoria del archivo
    """
    # Lista de palabras incorporadas en caso de que el archivo no esté disponible
    palabras_predeterminadas = [
        # Programación
        "programacion", "computadora", "desarrollo", "python", "algoritmo",
        "variable", "funcion", "clase", "objeto", "herencia", "polimorfismo",
        "abstraccion", "encapsulamiento", "framework", "biblioteca", "modulo",
        "iteracion", "condicion", "excepcion", "iterador", "generador", "decorador",
        "instancia", "metodo", "atributo", "constructor", "diccionario", "lista", 
        "tupla", "conjunto",
        
        # Palabras comunes
        "casa", "perro", "gato", "libro", "mesa", "silla", "arbol", "telefono",
        "ventana", "puerta", "escuela", "ciudad", "amigo", "familia", "trabajo",
        "comida", "tiempo", "dinero", "musica", "pelicula", "deporte", "cielo",
        "tierra", "agua", "fuego", "aire", "sol", "luna", "estrella", "camino",
        
        # Transporte
        "coche", "bicicleta", "avion", "barco", "tren", "autobus", "metro",
        "motocicleta", "helicoptero", "tranvia", "patinete", "cohete", "submarino",
        
        # Naturaleza
        "montaña", "playa", "oceano", "rio", "lago", "bosque", "jardin",
        "flor", "fruta", "verdura", "animal", "insecto", "dinosaurio", "tigre",
        "elefante", "jirafa", "ballena", "delfin", "aguila", "cocodrilo",
        
        # Personas
        "persona", "niño", "hombre", "mujer", "doctor", "profesor", "estudiante",
        "ingeniero", "artista", "bombero", "policia", "abogado", "escritor", "actor",
        
        # Emociones y conceptos
        "amor", "felicidad", "tristeza", "miedo", "esperanza", "coraje", "amistad",
        "libertad", "justicia", "paz", "guerra", "conocimiento", "sabiduria", "belleza",
        
        # Objetos cotidianos
        "reloj", "espejo", "camara", "maleta", "tijeras", "paraguas", "lapiz",
        "cuaderno", "botella", "tenedor", "cuchillo", "cuchara", "plato", "vaso",
        "almohada", "manta", "cortina", "alfombra", "calendario", "lampara",
        
        # Tecnología
        "internet", "robot", "satelite", "teclado", "pantalla", "bateria", "antena",
        "memoria", "archivo", "mensaje", "correo", "aplicacion", "virus", "conexion",
        
        # Alimentos
        "galleta", "chocolate", "helado", "hamburguesa", "ensalada", "pasta",
        "paella", "tortilla", "queso", "leche", "zumo", "cafe", "cerveza",
        "manzana", "platano", "naranja", "tomate", "zanahoria", "patata"
    ]
    
    try:
        # Intenta construir la ruta al archivo de palabras
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        directorio_raiz = os.path.dirname(os.path.dirname(directorio_actual))
        ruta_archivo = os.path.join(directorio_raiz, '..', 'data', 'palabras.txt')
        
        # Intenta abrir el archivo
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            palabras = [palabra.strip() for palabra in archivo.readlines() if palabra.strip()]
        
        # Verifica si se cargaron palabras desde el archivo
        if palabras:
            print(f"Se han cargado {len(palabras)} palabras del archivo.")
            # Selecciona una palabra aleatoria
            palabra = random.choice(palabras)
            print(f"DEBUG: Palabra seleccionada: {palabra}")  # Para depuración
            return palabra
        else:
            print("El archivo de palabras está vacío. Usando lista predeterminada.")
            return random.choice(palabras_predeterminadas)
            
    except Exception as e:
        print(f"Error al cargar el archivo de palabras: {e}")
        print("Usando lista de palabras predeterminada.")
        return random.choice(palabras_predeterminadas)