def calcular_iva():
  """
  Calcula el IVA de un valor decimal y muestra el total con IVA.
  """
  valor_decimal = float(input("Ingrese el valor decimal: "))

  porcentaje_iva = 15

  iva = valor_decimal * (porcentaje_iva / 100)

  total_con_iva = valor_decimal + iva

  print(f"El valor del IVA es: {iva:.2f}")
  print(f"El total con IVA es: {total_con_iva:.2f}")

calcular_iva()
