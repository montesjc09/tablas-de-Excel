from modelo_usuario import usuario
from modelo_numeros import numero
from modelo_calculadora import calculadora

usuario1 = usuario("camilo", 12345)
usuario1.mostrar_info()
print()

numero1 = numero(10)
numero2 = numero(5)

numero1.mostrar_info()
numero2.mostrar_info()
print()

calc = calculadora(numero1.get_numero(), numero2.get_numero(), "2026-06-02")

print("suma:", calc.calculo("suma"))
print("resta:", calc.calculo("resta"))
print("multiplicacion:", calc.calculo("multiplicacion"))
print("division:", calc.calculo("division"))