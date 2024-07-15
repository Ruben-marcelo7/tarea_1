def convertir_fahrenheit_a_celsius():
  
  fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))

  celsius = (5 / 9) * (fahrenheit - 32)

  print(f"La temperatura en Celsius es: {celsius:.2f}")

convertir_fahrenheit_a_celsius()
