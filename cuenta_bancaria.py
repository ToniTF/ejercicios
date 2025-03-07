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
            saldo_inicial (float, opcional): Saldo inicial de la cuenta. Valor por defecto: 0.0
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
            float: Saldo actual de la cuenta
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
    
    def cerrar_cuenta(self):
        """
        Cierra la cuenta bancaria.
        
        Returns:
            float: El saldo retirado al cerrar la cuenta, o None si la operación falló
        """
        if not self.activa:
            print("Error: La cuenta ya está inactiva.")
            return None
            
        saldo_final = self.saldo
        self.saldo = 0
        self.activa = False
        
        # Registramos el cierre en el historial
        self.movimientos.append({
            'tipo': 'Cierre de cuenta',
            'cantidad': saldo_final,
            'saldo_resultante': 0
        })
        
        print(f"Cuenta cerrada correctamente. Se ha retirado el saldo de {saldo_final:.2f} €")
        return saldo_final


# Ejemplo de uso de la clase
def main():
    # Creamos una cuenta
    mi_cuenta = CuentaBancaria("Juan Pérez", "ES123456789", 1000)
    print(f"Cuenta creada para {mi_cuenta.titular} con número {mi_cuenta.numero_cuenta}")
    
    # Realizamos algunas operaciones
    mi_cuenta.consultar_saldo()
    mi_cuenta.depositar(500)
    mi_cuenta.retirar(200)
    
    # Creamos otra cuenta para probar transferencias
    otra_cuenta = CuentaBancaria("Ana García", "ES987654321", 500)
    
    # Realizamos una transferencia entre cuentas
    mi_cuenta.transferir(otra_cuenta, 300)
    
    # Consultamos el historial de movimientos
    mi_cuenta.ver_historial()
    print("\n")
    otra_cuenta.ver_historial()
    
    # Cerramos una cuenta
    mi_cuenta.cerrar_cuenta()
    
    # Intentamos realizar una operación en una cuenta cerrada
    resultado = mi_cuenta.depositar(100)
    print(f"¿Operación exitosa?: {resultado}")


if __name__ == "__main__":
    main()