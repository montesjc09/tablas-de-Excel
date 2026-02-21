from Modelo_parqueadero import parqueadero
from usuario import Usuario
from Modelo_carro import carro

usuario1 = Usuario("1020345678", "Juan Garcia", "Administrador")
usuario2 = Usuario("1020345679", "Maria Lopez", "Cliente")
usuario3 = Usuario("1020345680", "Carlos Rodriguez", "Ciente")
usuario4 = Usuario("1020345681", "Ana Martinez", "cliente")

carro1 = carro("ABC123", "Sedan", "Negro")
carro2 = carro("XYZ789", "SUV", "Blanco")
carro3 = carro("KLM456", "Pickup", "Azul")
carro4 = carro("DEF321", "Hatchback", "Rojo")

registro1 = parqueadero("ABC123", "A-01", "2026-02-16", "08:30", None, "entrada")
resgistro2 = parqueadero("XYZ789", "B-05", "2026-02-16","9:15", None, "entrada" )
registro3 = parqueadero("KLM456", "C-12", "2026-02-16", "10:00", "11:45", "Salida" )
registro4 = parqueadero("DEF321", "A-03", "2026-02-16", "11:20", None, "entrada" )

print(usuario1.mostrar_informacion())
print(usuario2.mostrar_informacion())
print(usuario3.mostrar_informacion())
print(usuario4.mostrar_informacion())

print(carro1.mostrar_info())
print(carro2.mostrar_info())
print(carro3.mostrar_info())
print(carro4.mostrar_info())

print(registro1.mostrar_info())
print(resgistro2.mostrar_info())
print(registro3.mostrar_info())
print(registro4.mostrar_info())