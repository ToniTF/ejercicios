class Contacto:
    """
    Clase que representa un contacto en la agenda.
    """
    
    def __init__(self, nombre, telefono, email=""):
        """
        Inicializa un nuevo contacto.
        
        Args:
            nombre (str): Nombre del contacto
            telefono (str): Número de teléfono del contacto
            email (str, opcional): Correo electrónico del contacto
        """
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    def actualizar(self, telefono=None, email=None):
        """
        Actualiza la información del contacto.
        
        Args:
            telefono (str, opcional): Nuevo número de teléfono
            email (str, opcional): Nuevo correo electrónico
        """
        if telefono is not None:
            self.telefono = telefono
        if email is not None:
            self.email = email
    
    def __str__(self):
        """
        Representación en cadena de texto del contacto.
        
        Returns:
            str: Información formateada del contacto
        """
        return f"Nombre: {self.nombre}\nTeléfono: {self.telefono}\nEmail: {self.email}"


class Agenda:
    """
    Clase que gestiona una colección de contactos.
    """
    
    def __init__(self):
        """
        Inicializa una nueva agenda vacía.
        """
        self.contactos = []
    
    def agregar_contacto(self, contacto):
        """
        Agrega un nuevo contacto a la agenda.
        
        Args:
            contacto (Contacto): El contacto a agregar
            
        Returns:
            bool: True si se agregó correctamente, False si ya existe un contacto con ese nombre
        """
        # Verificamos si ya existe un contacto con el mismo nombre
        if self.buscar_contacto(contacto.nombre) is not None:
            print(f"Error: Ya existe un contacto con el nombre '{contacto.nombre}'.")
            return False
        
        # Agregamos el contacto a la lista
        self.contactos.append(contacto)
        print(f"Contacto '{contacto.nombre}' agregado correctamente.")
        return True
    
    def buscar_contacto(self, nombre):
        """
        Busca un contacto por su nombre.
        
        Args:
            nombre (str): El nombre del contacto a buscar
            
        Returns:
            Contacto o None: El contacto encontrado o None si no existe
        """
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                return contacto
        return None
    
    def eliminar_contacto(self, nombre):
        """
        Elimina un contacto de la agenda por su nombre.
        
        Args:
            nombre (str): El nombre del contacto a eliminar
            
        Returns:
            bool: True si se eliminó correctamente, False si no se encontró el contacto
        """
        contacto = self.buscar_contacto(nombre)
        if contacto is not None:
            self.contactos.remove(contacto)
            print(f"Contacto '{nombre}' eliminado correctamente.")
            return True
        else:
            print(f"Error: No se encontró un contacto con el nombre '{nombre}'.")
            return False
    
    def mostrar_contactos(self):
        """
        Muestra todos los contactos de la agenda.
        
        Returns:
            int: El número de contactos mostrados
        """
        if not self.contactos:
            print("La agenda está vacía.")
            return 0
        
        print("\n=== AGENDA DE CONTACTOS ===")
        print(f"Total de contactos: {len(self.contactos)}")
        print("---------------------------")
        
        for i, contacto in enumerate(self.contactos, 1):
            print(f"\nContacto #{i}:")
            print(contacto)
            print("---------------------------")
        
        return len(self.contactos)
    
    def buscar_por_termino(self, termino):
        """
        Busca contactos que contengan un término específico en cualquier campo.
        
        Args:
            termino (str): El término a buscar
            
        Returns:
            list: Lista de contactos que coinciden con el término
        """
        termino = termino.lower()
        resultados = []
        
        for contacto in self.contactos:
            if (termino in contacto.nombre.lower() or
                termino in contacto.telefono.lower() or
                termino in contacto.email.lower()):
                resultados.append(contacto)
        
        return resultados


def mostrar_menu():
    """
    Muestra el menú principal de la aplicación.
    
    Returns:
        int: La opción seleccionada
    """
    print("\n=== AGENDA DE CONTACTOS ===")
    print("1. Agregar nuevo contacto")
    print("2. Buscar contacto por nombre")
    print("3. Buscar por término")
    print("4. Actualizar contacto")
    print("5. Eliminar contacto")
    print("6. Mostrar todos los contactos")
    print("0. Salir")
    
    try:
        return int(input("\nSeleccione una opción: "))
    except ValueError:
        print("Error: Por favor ingrese un número.")
        return -1


def main():
    """
    Función principal que ejecuta la aplicación de agenda de contactos.
    """
    agenda = Agenda()
    
    # Agregamos algunos contactos de ejemplo
    agenda.agregar_contacto(Contacto("Ana García", "666111222", "ana@example.com"))
    agenda.agregar_contacto(Contacto("Luis Pérez", "644555666", "luis@example.com"))
    agenda.agregar_contacto(Contacto("María Sánchez", "677888999"))
    
    print("¡Bienvenido a tu Agenda de Contactos!")
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == 0:
            print("¡Gracias por usar la Agenda de Contactos!")
            break
            
        elif opcion == 1:
            # Agregar nuevo contacto
            print("\n-- AGREGAR NUEVO CONTACTO --")
            nombre = input("Nombre: ")
            if not nombre:
                print("Error: El nombre es obligatorio.")
                continue
                
            telefono = input("Teléfono: ")
            if not telefono:
                print("Error: El teléfono es obligatorio.")
                continue
                
            email = input("Email (opcional): ")
            
            nuevo_contacto = Contacto(nombre, telefono, email)
            agenda.agregar_contacto(nuevo_contacto)
        
        elif opcion == 2:
            # Buscar contacto por nombre
            print("\n-- BUSCAR CONTACTO --")
            nombre = input("Nombre del contacto a buscar: ")
            contacto = agenda.buscar_contacto(nombre)
            
            if contacto:
                print("\nContacto encontrado:")
                print("---------------------------")
                print(contacto)
            else:
                print(f"No se encontró un contacto con el nombre '{nombre}'.")
        
        elif opcion == 3:
            # Buscar por término
            print("\n-- BUSCAR POR TÉRMINO --")
            termino = input("Introduce el término de búsqueda: ")
            resultados = agenda.buscar_por_termino(termino)
            
            if resultados:
                print(f"\nSe encontraron {len(resultados)} contacto(s):")
                print("---------------------------")
                for i, contacto in enumerate(resultados, 1):
                    print(f"\nResultado #{i}:")
                    print(contacto)
                    print("---------------------------")
            else:
                print(f"No se encontraron contactos que contengan '{termino}'.")
        
        elif opcion == 4:
            # Actualizar contacto
            print("\n-- ACTUALIZAR CONTACTO --")
            nombre = input("Nombre del contacto a actualizar: ")
            contacto = agenda.buscar_contacto(nombre)
            
            if contacto:
                print("\nContacto encontrado. Información actual:")
                print(contacto)
                print("\nIntroduce los nuevos datos (deja en blanco para mantener el actual):")
                
                telefono = input(f"Teléfono [{contacto.telefono}]: ")
                email = input(f"Email [{contacto.email}]: ")
                
                contacto.actualizar(
                    telefono=telefono if telefono else None,
                    email=email if email else None
                )
                print("Contacto actualizado correctamente.")
            else:
                print(f"No se encontró un contacto con el nombre '{nombre}'.")
        
        elif opcion == 5:
            # Eliminar contacto
            print("\n-- ELIMINAR CONTACTO --")
            nombre = input("Nombre del contacto a eliminar: ")
            agenda.eliminar_contacto(nombre)
        
        elif opcion == 6:
            # Mostrar todos los contactos
            agenda.mostrar_contactos()
        
        else:
            if opcion != -1:  # No mostramos este mensaje si ya se mostró un error de formato
                print("Opción inválida. Por favor, seleccione una opción del menú.")
        
        # Pausa antes de mostrar el menú de nuevo
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()