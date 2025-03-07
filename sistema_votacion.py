import datetime
import random
import string
from collections import Counter

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
        self.nombre = nombre
        self.id_documento = id_documento

    def __str__(self):
        """
        Retorna la representación en string de la persona.
        
        Returns:
            str: Descripción textual de la persona
        """
        return f"{self.nombre} (ID: {self.id_documento})"


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
        super().__init__(nombre, id_documento)
        self.partido = partido
        self.votos = 0
    
    def incrementar_voto(self):
        """
        Incrementa en uno el contador de votos del candidato.
        """
        self.votos += 1
    
    def __str__(self):
        """
        Retorna la representación en string del candidato.
        
        Returns:
            str: Descripción textual del candidato
        """
        return f"{self.nombre} - Partido: {self.partido} (ID: {self.id_documento})"


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
        super().__init__(nombre, id_documento)
        self.ha_votado = False
        self.codigo_verificacion = None
    
    def emitir_voto(self, candidato):
        """
        Registra el voto del votante para un candidato específico.
        
        Args:
            candidato (Candidato): Candidato seleccionado por el votante
            
        Returns:
            bool: True si el voto se emitió correctamente, False si el votante ya había votado
        """
        if self.ha_votado:
            return False
        
        # Generamos un código de verificación aleatorio
        self.codigo_verificacion = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        self.ha_votado = True
        candidato.incrementar_voto()
        return True
    
    def __str__(self):
        """
        Retorna la representación en string del votante.
        
        Returns:
            str: Descripción textual del votante
        """
        status = "Ha votado" if self.ha_votado else "No ha votado"
        return f"{self.nombre} (ID: {self.id_documento}) - {status}"


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
        self.nombre = nombre
        self.fecha = fecha or datetime.date.today()
        self.candidatos = []
        self.votantes = {}  # Diccionario con id_documento como clave
        self.estado = "Preparación"  # Estados: Preparación, Votación, Finalizada
        self.votos_blancos = 0
        self.votos_nulos = 0
    
    def registrar_candidato(self, candidato):
        """
        Añade un candidato a la elección.
        
        Args:
            candidato (Candidato): El candidato a añadir
            
        Returns:
            bool: True si se añadió correctamente, False si ya existe o la elección está cerrada
        """
        if self.estado != "Preparación":
            print("Error: No se pueden añadir candidatos una vez iniciada la votación.")
            return False
        
        # Comprobamos si ya existe un candidato con el mismo ID
        for c in self.candidatos:
            if c.id_documento == candidato.id_documento:
                print(f"Error: Ya existe un candidato con ID {candidato.id_documento}.")
                return False
        
        self.candidatos.append(candidato)
        print(f"Candidato {candidato.nombre} registrado correctamente.")
        return True
    
    def registrar_votante(self, votante):
        """
        Añade un votante a la elección.
        
        Args:
            votante (Votante): El votante a añadir
            
        Returns:
            bool: True si se añadió correctamente, False si ya existe
        """
        if votante.id_documento in self.votantes:
            print(f"Error: Ya existe un votante con ID {votante.id_documento}.")
            return False
        
        self.votantes[votante.id_documento] = votante
        print(f"Votante {votante.nombre} registrado correctamente.")
        return True
    
    def iniciar_votacion(self):
        """
        Inicia el proceso de votación.
        
        Returns:
            bool: True si se inició correctamente, False si no hay candidatos o ya estaba iniciada
        """
        if self.estado != "Preparación":
            print("Error: La votación ya ha sido iniciada o finalizada.")
            return False
        
        if len(self.candidatos) == 0:
            print("Error: No se puede iniciar la votación sin candidatos.")
            return False
        
        self.estado = "Votación"
        print(f"Votación '{self.nombre}' iniciada correctamente.")
        return True
    
    def finalizar_votacion(self):
        """
        Finaliza el proceso de votación.
        
        Returns:
            bool: True si se finalizó correctamente, False si no estaba en fase de votación
        """
        if self.estado != "Votación":
            print("Error: No se puede finalizar una votación que no está en curso.")
            return False
        
        self.estado = "Finalizada"
        print(f"Votación '{self.nombre}' finalizada correctamente.")
        return True
    
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
        if self.estado != "Votación":
            print("Error: La votación no está en curso.")
            return False
        
        if id_votante not in self.votantes:
            print(f"Error: No existe un votante con ID {id_votante}.")
            return False
        
        votante = self.votantes[id_votante]
        
        if votante.ha_votado:
            print(f"Error: El votante {votante.nombre} ya ha emitido su voto.")
            return False
        
        # Procesamos el voto según la opción seleccionada
        if indice_candidato is None:
            # Voto en blanco
            self.votos_blancos += 1
            votante.ha_votado = True
            votante.codigo_verificacion = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            print("Voto en blanco registrado correctamente.")
            print(f"Código de verificación: {votante.codigo_verificacion}")
        
        elif indice_candidato == -1:
            # Voto nulo
            self.votos_nulos += 1
            votante.ha_votado = True
            votante.codigo_verificacion = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            print("Voto nulo registrado correctamente.")
            print(f"Código de verificación: {votante.codigo_verificacion}")
        
        elif 0 <= indice_candidato < len(self.candidatos):
            # Voto a candidato
            candidato = self.candidatos[indice_candidato]
            votante.emitir_voto(candidato)
            print(f"Voto para {candidato.nombre} registrado correctamente.")
            print(f"Código de verificación: {votante.codigo_verificacion}")
        
        else:
            print("Error: Opción de voto inválida.")
            return False
        
        return True
    
    def mostrar_resultados(self):
        """
        Muestra los resultados de la votación.
        
        Returns:
            bool: True si los resultados se mostraron correctamente, False si la elección no ha finalizado
        """
        if self.estado != "Finalizada":
            print("Error: No se pueden mostrar los resultados hasta que la elección finalice.")
            return False
        
        total_votos = sum(c.votos for c in self.candidatos) + self.votos_blancos + self.votos_nulos
        
        print("\n===== RESULTADOS DE LA ELECCIÓN =====")
        print(f"Nombre: {self.nombre}")
        print(f"Fecha: {self.fecha}")
        print(f"Total de votos: {total_votos}")
        
        if total_votos > 0:
            # Calculamos el porcentaje de participación
            participacion = (total_votos / len(self.votantes)) * 100 if self.votantes else 0
            print(f"Participación: {participacion:.2f}%")
            
            print("\nRESULTADOS POR CANDIDATO:")
            # Ordenamos los candidatos por número de votos (orden descendente)
            candidatos_ordenados = sorted(self.candidatos, key=lambda c: c.votos, reverse=True)
            
            for i, candidato in enumerate(candidatos_ordenados, 1):
                porcentaje = (candidato.votos / total_votos) * 100 if total_votos > 0 else 0
                print(f"{i}. {candidato.nombre} ({candidato.partido}): {candidato.votos} votos ({porcentaje:.2f}%)")
            
            # Mostramos información sobre votos blancos y nulos
            porcentaje_blancos = (self.votos_blancos / total_votos) * 100 if total_votos > 0 else 0
            porcentaje_nulos = (self.votos_nulos / total_votos) * 100 if total_votos > 0 else 0
            
            print(f"\nVotos en blanco: {self.votos_blancos} ({porcentaje_blancos:.2f}%)")
            print(f"Votos nulos: {self.votos_nulos} ({porcentaje_nulos:.2f}%)")
            
            # Determinamos el ganador si hay votos válidos
            if total_votos > self.votos_blancos + self.votos_nulos:
                ganador = candidatos_ordenados[0]
                print(f"\nGANADOR: {ganador.nombre} del partido {ganador.partido} con {ganador.votos} votos.")
            else:
                print("\nNo hay un ganador claro debido a la mayoría de votos blancos o nulos.")
        else:
            print("\nNo se registraron votos en esta elección.")
        
        return True
    
    def __str__(self):
        """
        Retorna la representación en string de la elección.
        
        Returns:
            str: Descripción textual de la elección
        """
        return f"Elección: {self.nombre} - Fecha: {self.fecha} - Estado: {self.estado}"


def mostrar_menu_principal():
    """
    Muestra el menú principal y retorna la opción elegida.
    
    Returns:
        int: Opción seleccionada
    """
    print("\n===== SISTEMA DE VOTACIÓN ELECTORAL =====")
    print("1. Registrar candidato")
    print("2. Registrar votante")
    print("3. Ver candidatos registrados")
    print("4. Ver votantes registrados")
    print("5. Iniciar votación")
    print("6. Emitir voto")
    print("7. Finalizar votación")
    print("8. Ver resultados")
    print("0. Salir")
    
    try:
        opcion = int(input("\nSeleccione una opción: "))
        return opcion
    except ValueError:
        print("Error: Por favor ingrese un número.")
        return -1


def main():
    """
    Función principal del sistema de votación.
    """
    print("¡Bienvenido al Sistema de Votación Electoral!")
    
    nombre_eleccion = input("Introduzca el nombre o título de la elección: ")
    eleccion = Eleccion(nombre_eleccion)
    print(f"Elección '{nombre_eleccion}' creada correctamente.")
    
    # Bucle principal
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == 0:
            print("¡Gracias por utilizar el Sistema de Votación Electoral!")
            break
            
        elif opcion == 1:
            # Registrar candidato
            print("\n-- REGISTRAR CANDIDATO --")
            nombre = input("Nombre completo: ")
            id_documento = input("Número de documento: ")
            partido = input("Partido político: ")
            
            if nombre and id_documento and partido:
                candidato = Candidato(nombre, id_documento, partido)
                eleccion.registrar_candidato(candidato)
            else:
                print("Error: Todos los campos son obligatorios.")
        
        elif opcion == 2:
            # Registrar votante
            print("\n-- REGISTRAR VOTANTE --")
            nombre = input("Nombre completo: ")
            id_documento = input("Número de documento: ")
            
            if nombre and id_documento:
                votante = Votante(nombre, id_documento)
                eleccion.registrar_votante(votante)
            else:
                print("Error: Todos los campos son obligatorios.")
        
        elif opcion == 3:
            # Ver candidatos registrados
            print("\n-- CANDIDATOS REGISTRADOS --")
            if not eleccion.candidatos:
                print("No hay candidatos registrados.")
            else:
                for i, candidato in enumerate(eleccion.candidatos, 1):
                    print(f"{i}. {candidato}")
        
        elif opcion == 4:
            # Ver votantes registrados
            print("\n-- VOTANTES REGISTRADOS --")
            if not eleccion.votantes:
                print("No hay votantes registrados.")
            else:
                for i, (_, votante) in enumerate(eleccion.votantes.items(), 1):
                    print(f"{i}. {votante}")
        
        elif opcion == 5:
            # Iniciar votación
            eleccion.iniciar_votacion()
        
        elif opcion == 6:
            # Emitir voto
            if eleccion.estado != "Votación":
                print("Error: La votación no está en curso.")
                continue
            
            print("\n-- EMITIR VOTO --")
            id_votante = input("Número de documento del votante: ")
            
            if id_votante not in eleccion.votantes:
                print(f"Error: No existe un votante con ID {id_votante}.")
                continue
            
            votante = eleccion.votantes[id_votante]
            
            if votante.ha_votado:
                print(f"Error: El votante {votante.nombre} ya ha emitido su voto.")
                continue
            
            print("\nOpciones de voto:")
            print("0. Voto en blanco")
            
            for i, candidato in enumerate(eleccion.candidatos, 1):
                print(f"{i}. {candidato}")
            
            print("99. Voto nulo")
            
            try:
                opcion_voto = int(input("\nSeleccione una opción: "))
                
                if opcion_voto == 0:
                    # Voto en blanco
                    eleccion.emitir_voto(id_votante, None)
                elif opcion_voto == 99:
                    # Voto nulo
                    eleccion.emitir_voto(id_votante, -1)
                elif 1 <= opcion_voto <= len(eleccion.candidatos):
                    # Voto a candidato
                    eleccion.emitir_voto(id_votante, opcion_voto - 1)
                else:
                    print("Error: Opción de voto inválida.")
            except ValueError:
                print("Error: Por favor ingrese un número.")
        
        elif opcion == 7:
            # Finalizar votación
            eleccion.finalizar_votacion()
        
        elif opcion == 8:
            # Ver resultados
            eleccion.mostrar_resultados()
        
        else:
            if opcion != -1:  # No mostramos este mensaje si ya se mostró un error de formato
                print("Opción inválida. Por favor, seleccione una opción del menú.")
        
        # Pausa antes de mostrar el menú de nuevo
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()