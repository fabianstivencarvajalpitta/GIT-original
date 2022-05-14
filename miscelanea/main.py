while(True):
    print(" bienvenido a mi proyecto: fabian carvajal")
    print("                                                ")
    print("OPERADORES")
    print("                                                ")
    print("1: area de un triangulo ")
    print("2: suma de numeros")
    print("3: ingresar un numero y visualizar el numero elevado al    cuadrado")
    print("4: convertidoreuros a dolares")
    print("5: digite el area de un triangulo  ")
    print("6: determine el área y el volúmen de un cilindro ")
    print("7: calcular el area y logitud de un circulo.")
    print("8: Calcular el promedio de tres  números ")
    print("                                                         ")
    print("CONDICIONALES")
    print("                                                         ")
    print("9: numeros positivos o negativos")
    print("10: cual numero es mayor y cual es menor")
    print("11: 3 numeros positivos o negativos y cual es el mayor y el menor")
    print("12: eliaj 2 numeros y sumelos si el primer numero es menor que el segundo se restaran")
    print("13: encontrar el cociente entre el primer numero y el segundo numero ")
    print("14: sumar  2 numeros y si alguno de ellos es negativo se debe multiplicar ")
    print("15: digite un año para saber si es bisesto")
    print("                                                        ")
    print("CICLOS:")
    print("                                                        ")
    print("16: imprimir multiplos de 3 a 100 ")
    print("17: numero impares del 0 a 100")
    print("18: numeros pares del 0 a 100")
    print("19: numeros cuadrados del 1 al 30")
    print("20: suma de cuadrados de 100 numeros naturales")
    print("21: 2 numeros naturales ")
    print("22: sumar todos los numeros")
    print("99: FIN ")
    print("                                                        ")
    print("ingrese el numero del ejercicio")
    


    choice=input("ingrese numero:")
    import os 


    if choice=="1":
      print("digite los datos")
      print("base:")
      d1= int(input())
      print("altura:")
      d2= int(input())
      result= d1 * d2 
      result= result /2
      print("el area del triangulo es:" + str(result))
      n4 = input("ENTER para continuar")
      os.system("clear")





    if choice=="2":
      print("Digite los numeros")
      n1 = float(input("escriba el primer numero: \n"))
      n2 = float(input("escriba el segundo numero: \n"))
      result = n1 + n2 
      print("la suma es de:" + str(result))
      n4 = input("ENTER para continuar")
      os.system("clear")



    if choice=="3":
      print("ingresar un numero y visualizar el numero elevado al cuadrado")
      s1 = float(input("ingrese el numero \n"))
      s1 = float(input("ingrese el numero \n"))
      result = s1 ** s1 
      print("resultado:" + str (result))
      n4 = input("ENTER para continuar")
      os.system("clear")



    if choice=="4":
      print("escribir un algoritmo que convierta de euros a dolares")
      print("Euro")
      n1 = int(input())
      result = 1.05 * n1
      print("dolar:" + str(result))
      n4 = input("ENTER para continuar")
      os.system("clear")



    if choice=="5":
      print("escribir un algoritmo que pida el lado de un cuadrado y   muestre el valor")
      print("digete la medida de un lado de un cuadrado para")
      print("obtener su Area y Perimetro")
      n1 = int(input())
      medidaarea = n1 * n1
      medidaperimetro = n1 + n1 + n1 + n1
      print("Area")
      print(medidaarea)
      print("Perimetro")
      print(medidaperimetro)
      n4 = input("ENTER para continuar")
      os.system("clear")



    if choice=="6":
      print("calcular el area y perimetro de un cilindro")
      print("ingresar radio y altura del cilindro")
      print("radio:")
      n1 = int(input())
      print("altura:")
      n2 = int(input())
      Volumen = (3.1416 * (n1 * n1)) * (n2)
      Area = (2 * 3.1416 * (n1 * n1)) + (2 * 3.1416 * (n1 * n2))
      print("Area")
      print(Area)
      print("Volumen")
      print(Volumen)
      n4 = input("ENTER para continuar")
      os.system("clear")

    if choice=="7":
      print("calcular el area y longitud de un circul")
      print("ingresar el radio del circulo:")
      n1 = int(input())
      print("longitud del circulo es:")
      longitud = (2 * n1) * (3.1416)
      print(longitud)
      print("la area es:")
      n8 = (3.1416 * n1) ** 2
      print(n8)
      print(n8)
      n4 = input("ENTER para continuar")
      os.system("clear")



      
    if choice=="8":
      print("calcular el promedio de tres numeros")
      print("ingresa los numeros:")
      n1 = int(input())
      n2 = int(input())
      n3 = int(input())
      Promedio = (n1 + n2 + n3) /3
      print("El promedio e:")
      print(Promedio)
      n4 = input("ENTER para continuar")
      os.system("clear")



    if choice=="9":
      numero=input("escribir el digito")
      numero = float (numero)
      if numero ==0:
        print("Neutro")
      elif numero < 0:
        print("Negativo")
      else:
        print("Positivo")
      n4 = input("ENTER para continuar") 
      os.system("clear")



    if choice=="10":
      print("digite los numero para saber cual es el numero menor y el mayor")
      print("primer numero")
      n1 = int(input())
      print("ingrese el segundo numero")
      n2 = int(input())
      if n1==n2:
        print("los numeros son iguales")
      elif n1 > n2:
        rint(f"el numero {n1} es mayo que el num {n2}")
      elif n2 > n1:
        print(f"el numero {n2} es mayor que el numero {n1}")
        n4 = input("ENTER para continuar") 
        os.system("clear")



    if choice=="11":
      print("calcular entre 3 numeros cual es el mayor y cual es el menor")
      n1 = int(input("primero numero"))
      n2 = int(input("segundo numero"))
      n3 = int(input("tercer numero"))
      if n2 < n1 > n3:
        print(f"el numero mayor es: {n1}")     
      if n1 < n2 > n3:
        print(f"el numero mayor es: {n2}")     
      if n1 < n3 > n2:
        print(f"el numero mayor es: {n3}")     
      if n1 > n2 < n3:
        print(f"el numero menor es: {n2}")     
      if n2 > n1 < n3:
        print(f"el numero menor es: {n1}")    
      if n1 > n3 < n2:
        print(f"el numero menor es: {n3}")    
      if n1 == n2:
        print(f"el numero {n1} y {n2} son iguales")    
      if n1 == n3:
        print(f"el numero {n1} y {n3} son iguales")     
      if n2 == n3:
        print(f"el numero {n2} y {n3} son iguales")
        print("")
      n4 = input("Enter para continuar")
      os.system("clear")


    if choice=="12":
      print("Calcular entre tres numeros cual es y cual es menor")
      n1 = int(input("ingrese el primer numero:"))
      n2 = int(input("ingrese el segundo numero:"))  
      if n1 < n2:
        print(f"el numero mayor es: {n2}")
        result = n1 + n2
        print("Resultado de la suma")
        print(result)
      if n2 < n1:
        print(f"el numero menor es:{n1}")
        result = n1 - n2
        print("Resultado de la resta:")
        print(result)
        print("")
      n4 = input("Enter para continuar")  
      os.system("clear")



    if choice=="13":
      print("ingrese el dividiendo y un divisor para obtener el   cociente") 
    
      print("dividiendo")
      a = int(input())
      print("divisor")
      b = int(input())
      if b==0:
        print("El divisor no puede ser 0")
      else:     
        print("El cociente de la división es",str(a/b))
        print("")
      n4 = input("Enter para continuar")
      os.system("clear")

    if choice=="14":
      print("Ingresar primer numero:")
      n1 = int(input())
      print("Ingresar segundo numero:")
      n2 = int(input())   
      if n1 < 0 and n2 > 0:
        print(f"El numero {n1} es negativo")
        result1 = n1 + n2
        print("El resultado es:")
        print(result1)   
      if n2 < 0 and n1 >0:
        print(f"el numero {n2} es negativo")
        result1 = n1 + n2
        print("El resultado es:")
        print(result1)      
      if n1 > 0 and n2 > 0:
        print("Los dos son positivos")
        result2 = n1 * n2
        print("El resultado es:")
        print(result2)
      
      if n2 < 0 and n1 <0:
        print(f"el numero {n2} y {n1} es negativo")
        result1 = n1 + n2
        print("El resultado es:")
        print(result1)
        print("")
      n4 = input("Enter para continuar")
      os.system("clear")

    if choice=="15":
      año = int(input('Introduce un año para saber si es bisiesto: '))
      if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
              print('El año es bisiesto')
            else:
              print('El año no es bisiesto')
        else:
            print('El año es bisiesto.')
      else:
            print('El año no es bisiesto.')
      print("")
      n4 = input("ENTER para continuar")
      os.system("clear")


    if choice=="16":
      print("Todos los multiplos de 3")
      num = 100
      odd_numbers = [i for i in range(num) if i % 2 != 0]
      print("Los multiplos de 3 hasta el 100:")
      print(odd_numbers)
      print("")
      n4 = input("ENTER para continuar")
      os.system("clear")



    if choice=="17":
      print("                                         ")
      print("digete un numero para mostrar todos los impares hasta ese numero")
      num = int(input())
      odd_numbers = [i for i in range(num) if i % 2 != 0]
      print(f"Todos los numeros impares hasta {num}:")
      print(odd_numbers)
      print("")
      n4 = input("ENTER para continuar") 
      os.system("clear")


    if choice=="18":
      print("")
      print("digete un numero para mostrar todos los pares hasta ese numero")
      num = int(input())
      odd_numbers = [i for i in range(num) if i % 2 != 1]
      print(f"Todos los numeros pares hasta {num} son:")
      print(odd_numbers)
      print("")
      n4 = input("ENTER para continuar")
      os.system("clear")



    if choice=="99":
      break