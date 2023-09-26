# El input recoge el dato y lo guarda en nombre.
nombre = input("Intruduce tu nombre: ")
print ("Hola " + nombre)

# Existen dos tipos de =s en programación:
#   =   -> Asigna lo que hay a la izquierda a
#          lo que hay a la derecha.
#          Ej. numero = 5
#   ==   -> Es un igual LÓGICO. ¡Compara los
#           valores que tiene a izq y der!
#           Devuelve true, si son iguales; o
#           false, si son distintas.

# 1. Entrada: Numero. Salida: True si es mayor
#    de edad.
# input siempre guarda el valor introducido como
#   str. Si queremos que sea un int hay que
#   transformarlo. int(input)...))
numero = int(input("Introduce tu edad: "))
# Para saber el tipo -> print(type(numero))
print ("¿Es mayor de edad? ")
print (numero >= 18)
# 2. Entrada: Dia semana. Salida: True si fin
#    de semana.
diaSemana = input("Introduce un dia de la semana: ")
print ("¿Es fin de semana? ")
print (diaSemana == "sabado" or diaSemana == "domingo")
# 3. Entrada: Numero. Salida: True si es positivo.
numero = int(input("Introduce un número: "))
print ("¿Es positivo? ")
print (numero >= 0)
# 4. Entrada: Letra. Salida: True si es vocal.
letra = input("Introduce una letra: ")
print ("¿Es vocal? ")
print (letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u")
# 5. Entrada: Numero. Salida: True si tá aprobado.
numero = int(input("Introduce tu nota: "))
print ("¿Está aprobado? ")
print (numero >= 5 and numero <=10)



