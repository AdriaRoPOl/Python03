"""

Escribe un programa que reciba un número del usuario e imprima si es positivo, 
negativo o cero. Utiliza la cadena if/elif/else apropiada, 
no vayas a emplear tres if consecutivos.

"""

numero=int(input("numero: "))
if numero > 0:
    print ("Es un numero positiu")
elif numero < 0:
    print ("Es un numero negatiu")
else:
    print ("Es zero")