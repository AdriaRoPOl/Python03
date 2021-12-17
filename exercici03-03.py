"""

Escribe un programa que 
reciba un número del usuario e imprima ``Bravo!'' 
si es mayor a -10 y menor a 10, ambos incluidos. (1 pt)

"""

numero=float(input("numero: "))
if numero > -10 and numero < 10:
    print ("Bravo!")
else:
    print ("Incorrecte")