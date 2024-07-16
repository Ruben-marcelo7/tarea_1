def identificar_vocal(letra):
  
  longitud_letra = len(letra)

  if longitud_letra == 1:

    letra_minuscula = letra.lower()

    if letra_minuscula in "aeiou":
      print("Es vocal")
    else:
      print("No es vocal")
  else:
    print("Sólo debe ingresar una letra")

letra_usuario = input("Ingrese una letra: ")
identificar_vocal(letra_usuario)

