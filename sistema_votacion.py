import datetime  # Para manejar fechas en la elección
import random  # Para generar códigos aleatorios
import string  # Para acceder a caracteres para los códigos de verificación
from collections import Counter  # Utilidad para contar elementos (aunque no se usa en el código actual)

class Persona:
    """
    Clase base para representar a una persona en el sistema electoral.
    """
    def __init__(self, nombre, id_documento):
        """
        Inicializa una instancia de Persona.
        
        Args:
            nombre (str): Nombre completo de la persona
            id_documento (str): Número de documento de identidad
        """
        self.nombre = nombre  # Almacena el nombre de la persona
        self.id_documento = id_documento  # Almacena el ID único de la persona

    def __str__(self):
        """
        Retorna la representación en string de la persona.
        
        Returns:
            str: Descripción textual de la persona
        """
        return f"{self.nombre} (ID: {self.id_documento})"  # Formatea la información básica de la persona


class Candidato(Persona):
    """
    Clase que representa a un candidato en una elección.
    """
    def __init__(self, nombre, id_documento, partido):
        """
        Inicializa un nuevo candidato.
        
        Args:
            nombre (str): Nombre completo del candidato
            id_documento (str): Número de documento de identidad
            partido (str): Partido político al que pertenece el candidato
        """
        super().__init__(nombre, id_documento)  # Llama al constructor de la clase padre (Persona)
        self.partido = partido  # Almacena el partido político del candidato
        self.votos = 0  # Inicializa el contador de votos en cero
    
    def incrementar_voto(self):
        """
        Incrementa en uno el contador de votos del candidato.
        """
        self.votos += 1  # Aumenta en 1 el contador de votos
    
    def __str__(self):
        """
        Retorna la representación en string del candidato.
        
        Returns:
            str: Descripción textual del candidato
        """
        return f"{self.nombre} - Partido: {self.partido} (ID: {self.id_documento})"  # Muestra información específica del candidato


class Votante(Persona):
    """
    Clase que representa a un votante en una elección.
    """
    def __init__(self, nombre, id_documento):
        """
        Inicializa un nuevo votante.
        
        Args:
            nombre (str): Nombre completo del votante
            id_documento (str): Número de documento de identidad
        """
        super().__init__(nombre, id_documento)  # Llama al constructor de la clase padre
        self.ha_votado = False  # Inicialmente el votante no ha emitido su voto
        self.codigo_verificacion = None  # No tiene código de verificación hasta que vote
    
    def emitir_voto(self, candidato):
        """
        Registra el voto del votante para un candidato específico.
        
        Args:
            candidato (Candidato): Candidato seleccionado por el votante
            
        Returns:
            bool: True si el voto se emitió correctamente, False si el votante ya había votado
        """
        if self.ha_votado:  # Verifica si el votante ya emitió su voto
            return False  # Si ya votó, no permite votar de nuevo
        
        # Generamos un código de verificación aleatorio
        self.codigo_verificacion = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))  # Crea un código alfanumérico de 8 caracteres
        self.ha_votado = True  # Marca al votante como "ha votado"
        candidato.incrementar_voto()  # Incrementa el contador de votos del candidato elegido
        return True  # Indica que el voto se registró correctamente
    
    def __str__(self):
        """
        Retorna la representación en string del votante.
        
        Returns:
            str: Descripción textual del votante
        """
        status = "Ha votado" if self.ha_votado else "No ha votado"  # Define el estado del votante
        return f"{self.nombre} (ID: {self.id_documento}) - {status}"  # Muestra la información del votante incluyendo su estado


class Eleccion:
    """
    Clase que representa un proceso electoral.
    """
    def __init__(self, nombre, fecha=None):
        """
        Inicializa una nueva elección.
        
        Args:
            nombre (str): Nombre o título de la elección
            fecha (datetime.date, opcional): Fecha de la elección. Si es None, se usa la fecha actual
        """
        self.nombre = nombre  # Almacena el nombre de la elección
        self.fecha = fecha or datetime.date.today()  # Si no se especifica fecha, usa la actual
        self.candidatos = []  # Lista vacía para almacenar los candidatos
        self.votantes = {}  # Diccionario con id_documento como clave (para búsqueda rápida)
        self.estado = "Preparación"  # Estados: Preparación, Votación, Finalizada
        self.votos_blancos = 0  # Contador para votos en blanco
        self.votos_nulos = 0  # Contador para votos nulos
    
    def registrar_candidato(self, candidato):
        """
        Añade un candidato a la elección.
        
        Args:
            candidato (Candidato): El candidato a añadir
            
        Returns:
            bool: True si se añadió correctamente, False si ya existe o la elección está cerrada
        """
        if self.estado != "Preparación":  # Verifica que la elección esté en fase de preparación
            print("Error: No se pueden añadir candidatos una vez iniciada la votación.")
            return False
        
        # Comprobamos si ya existe un candidato con el mismo ID
        for c in self.candidatos:  # Recorre la lista de candidatos
            if c.id_documento == candidato.id_documento:  # Verifica si el ID ya existe
                print(f"Error: Ya existe un candidato con ID {candidato.id_documento}.")
                return False
        
        self.candidatos.append(candidato)  # Añade el candidato a la lista
        print(f"Candidato {candidato.nombre} registrado correctamente.")
        return True  # Indica que se registró correctamente
    
    def registrar_votante(self, votante):
        """
        Añade un votante a la elección.
        
        Args:
            votante (Votante): El votante a añadir
            
        Returns:
            bool: True si se añadió correctamente, False si ya existe
        """
        if votante.id_documento in self.votantes:  # Verifica si el ID ya existe en el diccionario
            print(f"Error: Ya existe un votante con ID {votante.id_documento}.")
            return False
        
        self.votantes[votante.id_documento] = votante  # Añade el votante al diccionario usando su ID como clave
        print(f"Votante {votante.nombre} registrado correctamente.")
        return True  # Indica que se registró correctamente
    
    def iniciar_votacion(self):
        """
        Inicia el proceso de votación.
        
        Returns:
            bool: True si se inició correctamente, False si no hay candidatos o ya estaba iniciada
        """
        if self.estado != "Preparación":  # Verifica que esté en fase de preparación
            print("Error: La votación ya ha sido iniciada o finalizada.")
            return False
        
        if len(self.candidatos) == 0:  # Verifica que haya al menos un candidato
            print("Error: No se puede iniciar la votación sin candidatos.")
            return False
        
        self.estado = "Votación"  # Cambia el estado a "Votación"
        print(f"Votación '{self.nombre}' iniciada correctamente.")
        return True  # Indica que se inició correctamente
    
    def finalizar_votacion(self):
        """
        Finaliza el proceso de votación.
        
        Returns:
            bool: True si se finalizó correctamente, False si no estaba en fase de votación
        """
        if self.estado != "Votación":  # Verifica que esté en fase de votación
            print("Error: No se puede finalizar una votación que no está en curso.")
            return False
        
        self.estado = "Finalizada"  # Cambia el estado a "Finalizada"
        print(f"Votación '{self.nombre}' finalizada correctamente.")
        return True  # Indica que se finalizó correctamente
    
    def emitir_voto(self, id_votante, indice_candidato=None):
        """
        Registra el voto de un votante para un candidato.
        
        Args:
            id_votante (str): ID del votante
            indice_candidato (int, opcional): Índice del candidato elegido.
                                            None para voto en blanco, -1 para voto nulo
            
        Returns:
            bool: True si el voto se registró correctamente, False en caso contrario
        """
        if self.estado != "Votación":  # Verifica que la elección esté en fase de votación
            print("Error: La votación no está en curso.")
            return False
        
        if id_votante not in self.votantes:  # Verifica que el votante esté registrado
            print(f"Error: No existe un votante con ID {id_votante}.")
            return False
        
        votante = self.votantes[id_votante]  # Obtiene el objeto votante del diccionario
        
        if votante.ha_votado:  # Verifica que el votante no haya votado ya
            print(f"Error: El votante {votante.nombre} ya ha emitido su voto.")
            return False
        
        # Procesamos el voto según la opción seleccionada
        if indice_candidato is None:  # Voto en blanco
            # Voto en blanco
            self.votos_blancos += 1  # Incrementa el contador de votos en blanco
            votante.ha_votado = True  # Marca al votante como "ha votado"
            votante.codigo_verificacion = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))  # Genera código de verificación
            print("Voto en blanco registrado correctamente.")
            print(f"Código de verificación: {votante.codigo_verificacion}")
        
        elif indice_candidato == -1:  # Voto nulo
            # Voto nulo
            self.votos_nulos += 1  # Incrementa el contador de votos nulos
            votante.ha_votado = True  # Marca al votante como "ha votado"
            votante.codigo_verificacion = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))  # Genera código de verificación
            print("Voto nulo registrado correctamente.")
            print(f"Código de verificación: {votante.codigo_verificacion}")
        
        elif 0 <= indice_candidato < len(self.candidatos):  # Voto a candidato válido
            # Voto a candidato
            candidato = self.candidatos[indice_candidato]  # Obtiene el candidato por su índice
            votante.emitir_voto(candidato)  # Usa el método del votante para emitir el voto
            print(f"Voto para {candidato.nombre} registrado correctamente.")
            print(f"Código de verificación: {votante.codigo_verificacion}")
        
        else:  # Opción inválida
            print("Error: Opción de voto inválida.")
            return False
        
        return True  # Indica que el voto se registró correctamente
    
    def mostrar_resultados(self):
        """
        Muestra los resultados de la votación.
        
        Returns:
            bool: True si los resultados se mostraron correctamente, False si la elección no ha finalizado
        """
        if self.estado != "Finalizada":  # Verifica que la elección esté finalizada
            print("Error: No se pueden mostrar los resultados hasta que la elección finalice.")
            return False
        
        # Calcula el total de votos sumando los votos de cada candidato más los votos blancos y nulos
        total_votos = sum(c.votos for c in self.candidatos) + self.votos_blancos + self.votos_nulos
        
        print("\n===== RESULTADOS DE LA ELECCIÓN =====")  # Encabezado de resultados
        print(f"Nombre: {self.nombre}")  # Muestra el nombre de la elección
        print(f"Fecha: {self.fecha}")  # Muestra la fecha de la elección
        print(f"Total de votos: {total_votos}")  # Muestra el total de votos emitidos
        
        if total_votos > 0:  # Verifica que haya votos para mostrar estadísticas
            # Calculamos el porcentaje de participación
            participacion = (total_votos / len(self.votantes)) * 100 if self.votantes else 0  # Evita división por cero
            print(f"Participación: {participacion:.2f}%")  # Muestra el porcentaje con 2 decimales
            
            print("\nRESULTADOS POR CANDIDATO:")
            # Ordenamos los candidatos por número de votos (orden descendente)
            candidatos_ordenados = sorted(self.candidatos, key=lambda c: c.votos, reverse=True)  # Ordena usando el atributo votos
            
            # Muestra cada candidato con su porcentaje de votos
            for i, candidato in enumerate(candidatos_ordenados, 1):  # Enumera empezando desde 1
                porcentaje = (candidato.votos / total_votos) * 100 if total_votos > 0 else 0  # Evita división por cero
                print(f"{i}. {candidato.nombre} ({candidato.partido}): {candidato.votos} votos ({porcentaje:.2f}%)")
            
            # Mostramos información sobre votos blancos y nulos
            porcentaje_blancos = (self.votos_blancos / total_votos) * 100 if total_votos > 0 else 0  # Evita división por cero
            porcentaje_nulos = (self.votos_nulos / total_votos) * 100 if total_votos > 0 else 0  # Evita división por cero
            
            print(f"\nVotos en blanco: {self.votos_blancos} ({porcentaje_blancos:.2f}%)")  # Muestra votos en blanco
            print(f"Votos nulos: {self.votos_nulos} ({porcentaje_nulos:.2f}%)")  # Muestra votos nulos
            
            # Determinamos el ganador si hay votos válidos
            if total_votos > self.votos_blancos + self.votos_nulos:  # Verifica que haya votos válidos
                ganador = candidatos_ordenados[0]  # El primer candidato de la lista ordenada es el ganador
                print(f"\nGANADOR: {ganador.nombre} del partido {ganador.partido} con {ganador.votos} votos.")
            else:  # Si la mayoría son votos en blanco o nulos
                print("\nNo hay un ganador claro debido a la mayoría de votos blancos o nulos.")
        else:  # No hay votos
            print("\nNo se registraron votos en esta elección.")
        
        return True  # Indica que los resultados se mostraron correctamente
    
    def __str__(self):
        """
        Retorna la representación en string de la elección.
        
        Returns:
            str: Descripción textual de la elección
        """
        return f"Elección: {self.nombre} - Fecha: {self.fecha} - Estado: {self.estado}"  # Muestra información básica de la elección


def mostrar_menu_principal():
    """
    Muestra el menú principal y retorna la opción elegida.
    
    Returns:
        int: Opción seleccionada
    """
    print("\n===== SISTEMA DE VOTACIÓN ELECTORAL =====")  # Encabezado del menú
    print("1. Registrar candidato")  # Opción para añadir candidato
    print("2. Registrar votante")  # Opción para añadir votante
    print("3. Ver candidatos registrados")  # Opción para ver candidatos
    print("4. Ver votantes registrados")  # Opción para ver votantes
    print("5. Iniciar votación")  # Opción para iniciar la votación
    print("6. Emitir voto")  # Opción para emitir un voto
    print("7. Finalizar votación")  # Opción para finalizar la votación
    print("8. Ver resultados")  # Opción para ver resultados
    print("0. Salir")  # Opción para salir del programa
    
    try:
        opcion = int(input("\nSeleccione una opción: "))  # Solicita y convierte la opción a entero
        return opcion  # Devuelve la opción seleccionada
    except ValueError:  # Captura el error si no se ingresa un número
        print("Error: Por favor ingrese un número.")
        return -1  # Devuelve -1 para indicar error


def main():
    """
    Función principal del sistema de votación.
    """
    print("¡Bienvenido al Sistema de Votación Electoral!")  # Mensaje de bienvenida
    
    nombre_eleccion = input("Introduzca el nombre o título de la elección: ")  # Solicita el nombre de la elección
    eleccion = Eleccion(nombre_eleccion)  # Crea una nueva elección con ese nombre
    print(f"Elección '{nombre_eleccion}' creada correctamente.")
    
    # Bucle principal
    while True:  # Bucle infinito hasta que se seleccione salir
        opcion = mostrar_menu_principal()  # Muestra el menú y obtiene la opción seleccionada
        
        if opcion == 0:  # Opción para salir
            print("¡Gracias por utilizar el Sistema de Votación Electoral!")
            break  # Sale del bucle principal
            
        elif opcion == 1:  # Opción para registrar candidato
            # Registrar candidato
            print("\n-- REGISTRAR CANDIDATO --")
            nombre = input("Nombre completo: ")  # Solicita el nombre
            id_documento = input("Número de documento: ")  # Solicita el ID
            partido = input("Partido político: ")  # Solicita el partido
            
            if nombre and id_documento and partido:  # Verifica que todos los campos están completos
                candidato = Candidato(nombre, id_documento, partido)  # Crea un nuevo candidato
                eleccion.registrar_candidato(candidato)  # Lo registra en la elección
            else:  # Si falta algún campo
                print("Error: Todos los campos son obligatorios.")
        
        elif opcion == 2:  # Opción para registrar votante
            # Registrar votante
            print("\n-- REGISTRAR VOTANTE --")
            nombre = input("Nombre completo: ")  # Solicita el nombre
            id_documento = input("Número de documento: ")  # Solicita el ID
            
            if nombre and id_documento:  # Verifica que los campos estén completos
                votante = Votante(nombre, id_documento)  # Crea un nuevo votante
                eleccion.registrar_votante(votante)  # Lo registra en la elección
            else:  # Si falta algún campo
                print("Error: Todos los campos son obligatorios.")
        
        elif opcion == 3:  # Opción para ver candidatos
            # Ver candidatos registrados
            print("\n-- CANDIDATOS REGISTRADOS --")
            if not eleccion.candidatos:  # Verifica si hay candidatos
                print("No hay candidatos registrados.")
            else:
                for i, candidato in enumerate(eleccion.candidatos, 1):  # Enumera desde 1
                    print(f"{i}. {candidato}")  # Muestra cada candidato
        
        elif opcion == 4:  # Opción para ver votantes
            # Ver votantes registrados
            print("\n-- VOTANTES REGISTRADOS --")
            if not eleccion.votantes:  # Verifica si hay votantes
                print("No hay votantes registrados.")
            else:
                for i, (_, votante) in enumerate(eleccion.votantes.items(), 1):  # Enumera desde 1
                    print(f"{i}. {votante}")  # Muestra cada votante
        
        elif opcion == 5:  # Opción para iniciar votación
            # Iniciar votación
            eleccion.iniciar_votacion()  # Llama al método para iniciar la votación
        
        elif opcion == 6:  # Opción para emitir voto
            # Emitir voto
            if eleccion.estado != "Votación":  # Verifica que la elección esté en fase de votación
                print("Error: La votación no está en curso.")
                continue  # Vuelve al inicio del bucle
            
            print("\n-- EMITIR VOTO --")
            id_votante = input("Número de documento del votante: ")  # Solicita el ID del votante
            
            if id_votante not in eleccion.votantes:  # Verifica que el votante exista
                print(f"Error: No existe un votante con ID {id_votante}.")
                continue  # Vuelve al inicio del bucle
            
            votante = eleccion.votantes[id_votante]  # Obtiene el objeto votante
            
            if votante.ha_votado:  # Verifica que el votante no haya votado ya
                print(f"Error: El votante {votante.nombre} ya ha emitido su voto.")
                continue  # Vuelve al inicio del bucle
            
            print("\nOpciones de voto:")  # Muestra las opciones de voto
            print("0. Voto en blanco")  # Opción para voto en blanco
            
            for i, candidato in enumerate(eleccion.candidatos, 1):  # Enumera candidatos desde 1
                print(f"{i}. {candidato}")  # Muestra cada candidato
            
            print("99. Voto nulo")  # Opción para voto nulo
            
            try:
                opcion_voto = int(input("\nSeleccione una opción: "))  # Solicita la opción de voto
                
                if opcion_voto == 0:  # Voto en blanco
                    # Voto en blanco
                    eleccion.emitir_voto(id_votante, None)  # Registra voto en blanco
                elif opcion_voto == 99:  # Voto nulo
                    # Voto nulo
                    eleccion.emitir_voto(id_votante, -1)  # Registra voto nulo
                elif 1 <= opcion_voto <= len(eleccion.candidatos):  # Voto a candidato válido
                    # Voto a candidato
                    eleccion.emitir_voto(id_votante, opcion_voto - 1)  # Registra voto al candidato (ajustando el índice)
                else:  # Opción inválida
                    print("Error: Opción de voto inválida.")
            except ValueError:  # Captura el error si no se ingresa un número
                print("Error: Por favor ingrese un número.")
        
        elif opcion == 7:  # Opción para finalizar votación
            # Finalizar votación
            eleccion.finalizar_votacion()  # Llama al método para finalizar la votación
        
        elif opcion == 8:  # Opción para ver resultados
            # Ver resultados
            eleccion.mostrar_resultados()  # Llama al método para mostrar los resultados
        
        else:  # Opción inválida
            if opcion != -1:  # No mostramos este mensaje si ya se mostró un error de formato
                print("Opción inválida. Por favor, seleccione una opción del menú.")
        
        # Pausa antes de mostrar el menú de nuevo
        input("\nPresione Enter para continuar...")  # Espera a que el usuario presione Enter


if __name__ == "__main__":  # Verifica que el script se ejecute directamente
    main()  # Ejecuta la función principal