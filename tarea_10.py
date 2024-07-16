def fibonacci_con_for(n):

  if n == 0:
    return []  
  elif n == 1:
    return [0]  
  else:
    secuencia = [0, 1] 
    for i in range(2, n): 
      siguiente = secuencia[i - 1] + secuencia[i - 2] 
      secuencia.append(siguiente)
    return secuencia

secuencia_fibonacci = fibonacci_con_for(50)
print(secuencia_fibonacci)
