def find_smallest(num1, num2):

  return min(num1, num2)

PrimerNumero = int(input("Primer Numero: "))
SegundoNumero = int(input("Segundo Numero: "))

menor = find_smallest(PrimerNumero, SegundoNumero)

print(f"El numero menor es: {menor}")
