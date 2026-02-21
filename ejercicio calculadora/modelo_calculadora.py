class calculadora:
    def __init__(self, numero1, numero2, fecha):
        self.numero1 = numero1
        self.numero2 = numero2
        self.fecha = fecha
        
    def calculo(self, operacion):
        if operacion == "suma":
            return self.numero1 + self.numero2
        elif operacion == "resta":
            return self.numero1 - self.numero2
        elif operacion == "multiplicacion":
            return self.numero1 * self.numero2
        elif operacion == "division":
            if self.numero2 != 0:
                return self.numero1 / self.numero2
            else:
                return "Error: Division por cero no permitido"
        else:
            return "operacion no valida"
        
    def get_numero1(self):
        return self.numero1
    
    def set_numero1(self, nuevo_numero1):
        self.numero1 = nuevo_numero1
        
    def get_numero2 (self):
        return self.numero2
    
    def set_numero2(self,nuevo_numero2):
        self.numero2 = nuevo_numero2
        
    def get_fecha(self):
        return self.fecha
    
    def set_fecha(self, nueva_fecha):
        self.fecha = nueva_fecha
        
    def mostrar_info(self):
        print(f"numero1: {self.numero1}, numero2: {self.numero2}, fecha: {self.fecha}")
        
    