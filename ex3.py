while True:
    print("=======================================")
    print("           MENU DE INTERAÇÃO          ")
    print("=======================================")

    print("opção 1: maior e menor entre 10 números")
    print("-----------------------------------------")
    print("opção 2: lista de pares e impares")
    print("-----------------------------------------")
    print("opção 3: ler 8 números e verificar se o numero pedido existe na lista")
    print("-----------------------------------------")
    print("opção 4: ler 10 números e pedir ao usuario para remover algum numero da lista")
    print("-----------------------------------------")
    print("opção 5: ler 20 números e contar qunatos são positivos, negativos e zeros")
    print("-----------------------------------------")
    print("opção 6: criar duas listas e informar quais valores estão presentes em ambas as listas e quais valores estão presentes apenas em uma das listas")
    print("-----------------------------------------")
    print("opção 7: cadastrar nome, preço e quantidade de 5 produtos e depois mostrar o produto mais caro e o que tem quantidade abaixo de 10")
    print("-----------------------------------------")    
    print("opção 8: ler 12 números e armazene-os em uma lista, exiba os números em ordem crescente e decrescente, informe quantos números são pares e quantos são ímpares")
    print("-----------------------------------------")
    print("\n")
    opcao = int(input("Digite a opção desejada: "))

    #casos do menu
    match opcao:
        case 1:
            numeros = []
            for i in range(1, 11):
                numeros.append(int(input(f"digite o numero {i}: ")))

            print(f"os números digitados foram {numeros}")
            print(f"o maior valor da lista é {max(numeros)}")
            print(f"o menor valor da lista é {min(numeros)}")
        
        case 2:
            lista_par = []
            lista_impar = []
            for j in range(1, 16):
                valor = int(input(f"digite o valor {j}: "))
                if valor % 2 == 0:
                    lista_par.append(valor)
                else:
                    lista_impar.append(valor)
                
                print(f"lista dos números pares {lista_par}")
                print(f"lista dos números impares {lista_impar}")
        
        case 3:
            lista = []
            for k in range(1, 9):
                lista.append(int(input(f"digite o número {k}: ")))

            valor_pedido = int(input("qual valor deseja verificar se está na lista? "))

            print(lista)
            if valor_pedido in lista:
                print(f"{valor_pedido} está presente na lista")
            else:
                print(f"{valor_pedido} não está presente na lista")

        case 4:
            lista_numero = []
            for v in range(1, 11):
                lista_numero.append(int(input(f"digite o número {v}: ")))

            print(lista_numero)
            remover = int(input("digite um número para remover da lista: "))

            if remover in lista_numero:
                for z in lista_numero:
                    if z == remover:
                        lista_numero.remove(z)
                print(f"após a remoção a lista ficou assim: {lista_numero}")
            else:
                print(f"{remover} não está presente na lista")


        case 5:
            valores = []
            positivo = 0
            negativo = 0
            zero = 0
            for p in range(1, 21):
                valores.append(int(input(f"digite o valor {p}: ")))
            
            print(valores)
            for x in valores:
                if x > 0:
                    positivo += 1
                elif x == 0:
                    zero += 1
                else:
                    negativo += 1

            print(f"a quantidade de números positivos na lista é {positivo}")
            print(f"a quantidade de números negativos na lista é {negativo}")
            print(f"a quantidade de números zeros na lista é {zero}")

        case 6:
            lista1 = [2, 4, 28, 7, 19]
            lista2 = [8, 12, 4, 20, 7]
            lista_tot = []

            print(lista1)
            print(lista2)
            for h in lista1:
                for s in lista2:
                    if h == s:
                        lista_tot.append(h)
                        lista1.remove(h)
                        lista2.remove(s)


            print(f"os números que aparecem nas duas lista são {lista_tot}")
            print(f"os numeros que aparecem apenas na primeira lista são {lista1}")
            print(f"os números que aparecem apenas na segunda lista são {lista2}")

        case 7:
            historico = []
            cadastro = []
            caro = 0
            nome_caro = ''
            for l in range(1, 6):
                cadastro.append(input(f"digite o nome do produto {l}: "))
                cadastro.append(int(input(f"digite o preço do produto {l}: ")))
                cadastro.append(int(input(f"digite a quantidade do produto {l}: ")))
                historico.append(cadastro[:])
                cadastro.clear()

            # procura o produto mais caro
            for n in historico:
                if n[1] > caro:
                    caro = n[1]
                    nome_caro = n[0]

            print(f"a lista de produto é {historico}")
            menor_quantidade = []
            for m in historico:
                if m[2] < 10:
                    menor_quantidade.append(m[0])

            print(f"os produtos com quantidade menor que 10 são: {menor_quantidade}")
            print(f"o produto mais caro é {nome_caro}")

        case 8:
            contador_par = 0
            contador_impar = 0
            lista3 = []
            for c in range(1, 13):
                numero_lista = int(input(f"digite o número {c}: "))
                lista3.append(numero_lista)

                if numero_lista % 2 == 0:
                    contador_par += 1
                else:
                    contador_impar += 1

            print(f"lista completa {lista3}")
            print(f"lista ordenada {lista3.sort()}")
            print(f"lista em ordem decrescente {lista3.sort(reverse=True)}")
            print(f"quantidade de números pares {contador_par}")
            print(f"quantidade de números impares {contador_impar}")
    
    #continuar
    continuar = input("quer continuar? [S/N]").upper().strip()
    if continuar == 'N':
        break
    elif continuar != "S":
        while True:
            continuar = input("quer continuar? [S/N] ").upper().strip()
            if 'S' in continuar or 'N' in continuar:
                break
    if 'N' in continuar:
        break    