# 1. Entrada: Numero. Salida: True si es mayor
#    de edad.
edad = int(input("Introduce tu edad: "))
print ("¿Es mayor de edad? ")
# Se puede escribir 'esMayorEdad = edad >= 18'
esMayorEdad = (edad >= 18)
print(esMayorEdad)
# esMayorEdad es de tipo bool.
print(type(esMayorEdad))
if esMayorEdad:
    # Ojo con la tabulación.
    print("Es mayor de edad")
# Else siempre debajo de if. No obligatorio.
else:
    print("Es menor de edad")
print ("Se imprime siempre")
# Sin la variable bool esMayorEdad.
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# 3. Entrada: Numero. Salida: True si es positivo.
numero = int(input("Introduce un número: "))
print ("¿Es positivo? ")
esPositivo = (numero > 0)
if esPositivo:
    print("Es positivo")
elif numero == 0:
    print("Es 0")
else:
    print("Es negativo")

# 5. Entrada: Numero. Salida: True si tá aprobado.
nota = int(input("Introduce tu nota: "))
print ("¿Qué nota tiene? ")
# Si no asumimos una nota válida.
if nota > 10 or nota < 0:
    print ("No es una nota válida")
# Si asumimos una nota válida:
#       'if nota <= 10 and nota >= 9:'
elif nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print ("Notable")
elif nota >= 6:
    print ("Bien")
elif nota >= 5:
    print ("Suficiente")
else:
    print ("Suspenso")








