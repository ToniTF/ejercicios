class CuentaBancaria:
    """
    Clase que simula una cuenta bancaria con funcionalidades básicas.
    """
    
    def __init__(self, titular, numero_cuenta, saldo_inicial=0.0):
        """
        Inicializa una nueva cuenta bancaria.
        
        Args:
            titular (str): Nombre del titular de la cuenta
            numero_cuenta (str): Número único de la cuenta
            saldo_inicial (float, opcional): Saldo inicial de la cuenta. Por defecto 0.0
        """
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial
        self.activa = True
        self.movimientos = []
        
        # Registramos el depósito inicial si es mayor que cero
        if saldo_inicial > 0:
            self.movimientos.append({
                'tipo': 'Depósito inicial',
                'cantidad': saldo_inicial,
                'saldo_resultante': saldo_inicial
            })
    
    def depositar(self, cantidad):
        """
        Deposita una cantidad en la cuenta.
        
        Args:
            cantidad (float): Cantidad a depositar
            
        Returns:
            bool: True si la operación fue exitosa, False en caso contrario
        """
        if not self.activa:
            print("Error: La cuenta está inactiva.")
            return False
            
        if cantidad <= 0:
            print("Error: La cantidad a depositar debe ser positiva.")
            return False
            
        self.saldo += cantidad
        
        # Registramos la operación en el historial
        self.movimientos.append({
            'tipo': 'Depósito',
            'cantidad': cantidad,
            'saldo_resultante': self.saldo
        })
        
        print(f"Depósito realizado con éxito. Nuevo saldo: {self.saldo:.2f} €")
        return True
    
    def retirar(self, cantidad):
        """
        Retira una cantidad de la cuenta.
        
        Args:
            cantidad (float): Cantidad a retirar
            
        Returns:
            bool: True si la operación fue exitosa, False en caso contrario
        """
        if not self.activa:
            print("Error: La cuenta está inactiva.")
            return False
            
        if cantidad <= 0:
            print("Error: La cantidad a retirar debe ser positiva.")
            return False
            
        if cantidad > self.saldo:
            print("Error: Fondos insuficientes.")
            return False
            
        self.saldo -= cantidad
        
        # Registramos la operación en el historial
        self.movimientos.append({
            'tipo': 'Retiro',
            'cantidad': cantidad,
            'saldo_resultante': self.saldo
        })
        
        print(f"Retiro realizado con éxito. Nuevo saldo: {self.saldo:.2f} €")
        return True
    
    def consultar_saldo(self):
        """
        Consulta el saldo actual de la cuenta.
        
        Returns:
            float: Saldo actual de la cuenta o None si la cuenta está inactiva
        """
        if not self.activa:
            print("Error: La cuenta está inactiva.")
            return None
            
        print(f"Saldo actual: {self.saldo:.2f} €")
        return self.saldo
    
    def transferir(self, cuenta_destino, cantidad):
        """
        Transfiere una cantidad a otra cuenta.
        
        Args:
            cuenta_destino (CuentaBancaria): Cuenta a la que transferir el dinero
            cantidad (float): Cantidad a transferir
            
        Returns:
            bool: True si la operación fue exitosa, False en caso contrario
        """
        if not self.activa:
            print("Error: La cuenta origen está inactiva.")
            return False
            
        if not cuenta_destino.activa:
            print("Error: La cuenta destino está inactiva.")
            return False
            
        if cantidad <= 0:
            print("Error: La cantidad a transferir debe ser positiva.")
            return False
            
        if cantidad > self.saldo:
            print("Error: Fondos insuficientes para realizar la transferencia.")
            return False
            
        # Realizamos la transferencia
        self.saldo -= cantidad
        cuenta_destino.saldo += cantidad
        
        # Registramos la operación en ambas cuentas
        self.movimientos.append({
            'tipo': 'Transferencia enviada',
            'cantidad': cantidad,
            'destinatario': cuenta_destino.numero_cuenta,
            'saldo_resultante': self.saldo
        })
        
        cuenta_destino.movimientos.append({
            'tipo': 'Transferencia recibida',
            'cantidad': cantidad,
            'remitente': self.numero_cuenta,
            'saldo_resultante': cuenta_destino.saldo
        })
        
        print(f"Transferencia realizada con éxito a la cuenta {cuenta_destino.numero_cuenta}.")
        print(f"Tu nuevo saldo es: {self.saldo:.2f} €")
        return True
    
    def ver_historial(self, ultimos_n=None):
        """
        Muestra el historial de movimientos de la cuenta.
        
        Args:
            ultimos_n (int, opcional): Número de últimos movimientos a mostrar.
                                     Si es None, muestra todos los movimientos.
        """
        if not self.activa:
            print("Error: La cuenta está inactiva.")
            return
            
        if not self.movimientos:
            print("No hay movimientos en esta cuenta.")
            return
            
        print("\n=== HISTORIAL DE MOVIMIENTOS ===")
        print(f"Cuenta: {self.numero_cuenta}")
        print(f"Titular: {self.titular}")
        print("---------------------------------")
        
        # Determinamos cuántos movimientos mostrar
        movimientos_a_mostrar = self.movimientos
        if ultimos_n is not None and ultimos_n > 0 and ultimos_n < len(self.movimientos):
            movimientos_a_mostrar = self.movimientos[-ultimos_n:]
            print(f"Mostrando los últimos {ultimos_n} movimientos:")
        else:
            print("Mostrando todos los movimientos:")
            
        # Mostramos los movimientos
        for i, mov in enumerate(movimientos_a_mostrar, 1):
            print(f"\nMovimiento #{i}:")
            print(f"  Tipo: {mov['tipo']}")
            print(f"  Cantidad: {mov['cantidad']:.2f} €")
            if 'remitente' in mov:
                print(f"  Remitente: Cuenta {mov['remitente']}")
            if 'destinatario' in mov:
                print(f"  Destinatario: Cuenta {mov['destinatario']}")
            print(f"  Saldo resultante: {mov['saldo_resultante']:.2f} €")
    
    def __str__(self):
        """
        Representación en cadena de texto de la cuenta bancaria.
        
        Returns:
            str: Información formateada sobre la cuenta
        """
        estado = "Activa" if self.activa else "Inactiva"
        return f"Cuenta {self.numero_cuenta} - Titular: {self.titular} - Saldo: {self.saldo:.2f} € - Estado: {estado}"


class SistemaBancario:
    """
    Clase que gestiona múltiples cuentas bancarias.
    """
    
    def __init__(self, nombre_banco):
        """
        Inicializa un nuevo sistema bancario.
        
        Args:
            nombre_banco (str): Nombre del banco
        """
        self.nombre_banco = nombre_banco
        self.cuentas = {}  # Diccionario para almacenar las cuentas (clave: número de cuenta)
        self.ultimo_numero = 1000  # Número inicial para generar números de cuenta
        
    def crear_cuenta(self, titular, saldo_inicial=0.0):
        """
        Crea una nueva cuenta bancaria.
        
        Args:
            titular (str): Nombre del titular de la cuenta
            saldo_inicial (float, opcional): Saldo inicial de la cuenta
            
        Returns:
            CuentaBancaria: La cuenta creada
        """
        # Generamos un número de cuenta único
        numero_cuenta = f"{self.nombre_banco[:3].upper()}{self.ultimo_numero}"
        self.ultimo_numero += 1
        
        # Creamos la cuenta
        nueva_cuenta = CuentaBancaria(titular, numero_cuenta, saldo_inicial)
        
        # Almacenamos la cuenta en nuestro diccionario
        self.cuentas[numero_cuenta] = nueva_cuenta
        
        print(f"Cuenta {numero_cuenta} creada con éxito para {titular}.")
        return nueva_cuenta
    
    def buscar_cuenta(self, numero_cuenta):
        """
        Busca una cuenta por su número.
        
        Args:
            numero_cuenta (str): Número de la cuenta a buscar
            
        Returns:
            CuentaBancaria o None: La cuenta encontrada o None si no existe
        """
        if numero_cuenta in self.cuentas:
            return self.cuentas[numero_cuenta]
        else:
            print(f"Error: No se encontró la cuenta {numero_cuenta}.")
            return None
            
    def listar_cuentas(self):
        """
        Muestra la lista de todas las cuentas en el sistema.
        """
        print(f"\n=== CUENTAS DEL BANCO {self.nombre_banco} ===")
        
        if not self.cuentas:
            print("No hay cuentas registradas en el sistema.")
            return
            
        for numero, cuenta in self.cuentas.items():
            print(cuenta)
    
    def realizar_transferencia(self, origen, destino, cantidad):
        """
        Realiza una transferencia entre dos cuentas.
        
        Args:
            origen (str): Número de la cuenta origen
            destino (str): Número de la cuenta destino
            cantidad (float): Cantidad a transferir
            
        Returns:
            bool: True si la operación fue exitosa, False en caso contrario
        """
        # Buscamos las cuentas
        cuenta_origen = self.buscar_cuenta(origen)
        cuenta_destino = self.buscar_cuenta(destino)
        
        # Verificamos que ambas cuentas existan
        if not cuenta_origen or not cuenta_destino:
            return False
            
        # Realizamos la transferencia
        return cuenta_origen.transferir(cuenta_destino, cantidad)


def mostrar_menu():
    """
    Muestra el menú principal.
    
    Returns:
        int: Opción seleccionada
    """
    print("\n=== SISTEMA BANCARIO ===")
    print("1. Crear nueva cuenta")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Consultar saldo")
    print("5. Realizar transferencia")
    print("6. Ver historial de movimientos")
    print("7. Listar todas las cuentas")
    print("0. Salir")
    
    try:
        return int(input("\nSeleccione una opción: "))
    except ValueError:
        print("Error: Por favor ingrese un número.")
        return -1


def main():
    """
    Función principal que ejecuta la aplicación bancaria.
    """
    # Creamos un sistema bancario
    banco = SistemaBancario("Banco Python")
    print(f"Bienvenido al {banco.nombre_banco}")
    
    # Bucle principal del programa
    while True:
        opcion = mostrar_menu()
        
        if opcion == 0:
            print("¡Gracias por utilizar nuestros servicios!")
            break
            
        elif opcion == 1:
            # Crear cuenta
            titular = input("Nombre del titular: ")
            try:
                saldo = float(input("Saldo inicial (0.0 por defecto): ") or "0.0")
                banco.crear_cuenta(titular, saldo)
            except ValueError:
                print("Error: El saldo debe ser un número.")
        
        elif opcion == 2:
            # Depositar dinero
            numero = input("Número de cuenta: ")
            cuenta = banco.buscar_cuenta(numero)
            if cuenta:
                try:
                    cantidad = float(input("Cantidad a depositar: "))
                    cuenta.depositar(cantidad)
                except ValueError:
                    print("Error: La cantidad debe ser un número.")
        
        elif opcion == 3:
            # Retirar dinero
            numero = input("Número de cuenta: ")
            cuenta = banco.buscar_cuenta(numero)
            if cuenta:
                try:
                    cantidad = float(input("Cantidad a retirar: "))
                    cuenta.retirar(cantidad)
                except ValueError:
                    print("Error: La cantidad debe ser un número.")
        
        elif opcion == 4:
            # Consultar saldo
            numero = input("Número de cuenta: ")
            cuenta = banco.buscar_cuenta(numero)
            if cuenta:
                cuenta.consultar_saldo()
        
        elif opcion == 5:
            # Realizar transferencia
            origen = input("Número de cuenta origen: ")
            destino = input("Número de cuenta destino: ")
            try:
                cantidad = float(input("Cantidad a transferir: "))
                banco.realizar_transferencia(origen, destino, cantidad)
            except ValueError:
                print("Error: La cantidad debe ser un número.")
        
        elif opcion == 6:
            # Ver historial
            numero = input("Número de cuenta: ")
            cuenta = banco.buscar_cuenta(numero)
            if cuenta:
                try:
                    ultimos = input("Número de movimientos a mostrar (Enter para todos): ")
                    if ultimos:
                        ultimos = int(ultimos)
                        cuenta.ver_historial(ultimos)
                    else:
                        cuenta.ver_historial()
                except ValueError:
                    print("Error: Debe ingresar un número entero.")
        
        elif opcion == 7:
            # Listar cuentas
            banco.listar_cuentas()
        
        else:
            if opcion != -1:  # No mostramos este mensaje si ya se mostró un error de formato
                print("Opción inválida. Por favor, seleccione una opción del menú.")
        
        # Pausa antes de mostrar el menú de nuevo
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()