
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
    print("ARREGLOS")
    print("                                                        ")
    print("23:Numeros aleatorios")
    print("24:Organizacion de elementos en inversa")
    print("25: Organizacion de numero de menor a mayor, mayor a menor y de menor a mayor ")
    print("26: En arreglo decir cual es mayor y cual es menor")
    print("27: Convertir numeros ingresados en *")
    print("28: Identificar cantidad de veces que aparece un número en un arreglo")
    print("29: Identificar si un número es impar y par")
    


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

    if choice=="19":
      def generar_cuadrados(n):
          if 2 * n <= 30:
            cuadrados = [i ** 2 for i in range(1, 31)]
      
            return cuadrados
          else:
              raise ValueError("n no debe ser mayor a 2*n")
  
              resultados = generar_cuadrados(10)  
              print(resultados)
          
              print("")
      n4 = input("ENTER para continuar")
      os.system("clear")
      



    if choice=="20":
        print("")
        print("La suma de los 100 primeros numeros cuadrados")
        print("Resultado: 338350")
        print("")
        n4 = input("ENTER para continuar")
        os.system("clear")
    if choice=="21":
          print("Digite dos numeros")
          n1=int(input('Digite el número inicial de la secuencia \n'))
          n2=int(input('Digite el número final de la secuencia \n'))  
          nums=[]
          for i in range(n1, n2 + 1):
            nums.append(i)
          print('\n La secuencia ascendente de los números es:', nums)
          n4 = input("ENTER para continuar")
          os.system("clear") 
    if choice=="22":
          print("digite digites para sumar infinitamente hasta el cero")
          nums=[]
          while True:
              n=float(input('Digite el número a sumar, para concluir la suma por favor digite 0:'))
              if n!=0:
                  nums.append(n)
              else:
                  break
          print('Los números digitados fueron:', nums)
          print('La suma de los números fue:', sum(nums))
          n4 = input("Enter para continuar")
          os.system("clear")

       #arreglos
    if choice=="23":
            nums=[]
            aux=None
            while True:
                cant=int(input('Ingrese la cantidad de números que desea ver\n'))
                for i in range(cant):
                    n=random.randint(-100,100)
                    nums.append(n)
                print(nums)
                for i in range(len(nums)-1):
                  for i in range(len(nums)-1):
                    if nums[i]>=nums[i+1]:
                      aux=nums[i+1]
                      nums[i+1]=nums[i]
                      nums[i]=aux
                print(nums)
                break
            n4 = input("ENTER para continuar")
            os.system("clear")
  
    
    if choice=="24":
        print("")
        lista = []
        print("introducir 10 elementos")
        print("elemento 1:")
        n1 = int(input())
        print("elemento 2:")
        n2 = int(input())
        print("elemento 3:")
        n3 = int(input())
        print("elemento 4:")
        n4 = int(input())
        print("elemento 5:")
        n5 = int(input())
        print("elemento 6:")
        n6 = int(input())
        print("elemento 7:")
        n7 = int(input())
        print("elemento 8:")
        n8 = int(input())
        print("elemento 9:")
        n9 = int(input())
        print("elemento 10:")
        n10 = int(input())
        lista.append(n1)
        lista.append(n2)
        lista.append(n3)
        lista.append(n4)
        lista.append(n5)
        lista.append(n6)
        lista.append(n7)
        lista.append(n8)
        lista.append(n9)
        lista.append(n10)
        lista.reverse()
        print(lista)
        n98 = input("ENTER para continuar")
        os.system("clear")
        
               
    if choice=="25":
        print("")
        n = 10
        print("Ingresar 10 numeros:")  
        lista=[]
        for x in range(n):
            valor=float(input("Ingrese un numero: ")) 
            lista.append(valor)
        
        RecorrerLista = False 
        while RecorrerLista == False: 
            RecorrerLista = True
    
            for i in range(len(lista)-1):
                if lista[i] > lista[i + 1]:
                    VariableAuxiliar = lista[i]
                    lista[i] = lista[i + 1]
                    lista[i + 1] = VariableAuxiliar
                    RecorrerLista = False

        print("Orden ASCENDENTE (de menor a mayor): ")
        for i in range(0,n,1):
            print(lista[i])

        print("Orden DESCENDENTE (de mayor a menor): ")
        longitud_lista=len(lista)
        for i in range(longitud_lista//2):
            lista[i], lista[longitud_lista-i-1] = lista[longitud_lista-i-1], lista[i]
        print(lista)
        print("Orden ASCENDENTE (de menor a mayor): ")
        lista.reverse()
        for a in range(0,n,1):
            print(lista[a])
        n4 = input("ENTER para continuar")
        os.system("clear")
    if choice=="26":
        print("")
        print("ingrese la cantidad de elementos que desea en su arreglo")
        n = int(input())
        print(f"Ingresar {n} numeros:")  
        lista=[]
        for x in range(n):
          valor=float(input("Ingrese un numero: ")) 
          lista.append(valor)



        def mayor_de_arreglo(lista):
    
            mayor = lista[0]

            for elemento in lista:
              if elemento > mayor:
                mayor = elemento
            return mayor


        def menor_de_arreglo(lista):
            menor = lista[0]
            for elemento in lista:
              if elemento < menor:
                menor = elemento
            return menor

        mayor = mayor_de_arreglo(lista)
        menor = menor_de_arreglo(lista)
        print(f"Del arreglo {lista} el mayor es {mayor} y el menor es {menor}")

        n4 = input("Enter para continuar")
        os.system("clear")
    if choice=="27":
        nums=[]
        n1 = int(input("Ingresar la cantidad de numeros de desea ingresar: "))
        for i in range(n1):
          n=int(input('Digite un numero: '))
          nums.append(n)
        for i in nums:
          print(i,'->',i*'*')
        n4 = input("Enter para continuar")
        os.system("clear")
    if choice=="28":
          counts=dict()
          nums=[]
          n3 = int(input("Ingrese el rango de numeros que desea tener en el buscador"))
          for i in range(n3):
              n=int(input('Digite un numero: '))
              nums.append(n)
          for num in nums :
              counts [num] = counts.get (num, 0) + 1
          x=int(input('Ingrese el número que desea buscar: \n'))
          try:
            print('el número {} está {} veces'.format(x, counts[x]))
          except:
            print('no se encontró el número {} en la lista'.format(x))
          n4 = input("Enter para continuar")
          os.system("clear")
    if choice=="29":
        print("Digite Sus 8 Numeros")
        valores = 8
        valor1 = 0
        impar = []
        par = []
        lista = []
        while valor1 < valores:
          print("Llevas Digitado", (valor1 + 1), "Numeros")
          enteros = int(input())
          lista.append(enteros)
          valor1 += 1
        for i in range(valores):
          if lista[i] % 2 == 0:
            par.append(lista[i])
          else:
            impar.append(lista[i])
        impar.sort()
        par.sort()
        print("El Arreglo Que Diste Fue: \n"+ str(lista),"\n""Los Numeros Impares Del Arreglo Son: \n"+ str(impar),"\n""Los Numeros Pares Del Arreglo Son: \n"+ str(par))
        n4 = input("ENTER para continuar")
        os.system("clear")
      
    if choice=="99":
      print("Gracias por participar, Creado por fabian carvajal")


       
      