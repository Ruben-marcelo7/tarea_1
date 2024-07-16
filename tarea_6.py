def is_eligible_purchase(age, items_purchased):

  return age > 18 and items_purchased > 1

edad = int(input("tu edad: "))
CosasCompradas = int(input("cosas compradas: "))

Resultado = is_eligible_purchase(edad, CosasCompradas)
print(Resultado)