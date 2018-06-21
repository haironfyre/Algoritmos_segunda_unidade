def main():
    i = 0
    lista = []
    while (i < 25):
        num = int(input("Digite o elemento do vetor : "))
        lista.append(num)
        i += 1
    print (lista)
    soma = soma_lista(lista)
    maior_elemento = maior(lista)
    menor_elemento = menor(lista)
    media = med(lista)
    desvio_padrao = desvio(lista)
    print ("A soma da lista é : " + str(soma))
    print ("O maior elemento é : " +str(maior_elemento))
    print ("O menor elemento é : " + str(menor_elemento))
    print ("A média dos elementos é : " + str(media))
    print ("O desvio padrão é : " + str(desvio_padrao))
    
def soma_lista(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma

def maior(lista):
    sorted(lista)
    return(lista[-1])

def menor(lista):
    sorted(lista)
    return lista[0]

def med(lista):
    soma = soma_lista(lista)
    media = (soma/len(lista))
    return media

def desvio(lista):
    media = med(lista)
    x = 0
    for elemento in lista:
        x = float(x) + float((float(elemento) - float(media))**2)
        variancia = x/len(lista)
    desvio = variancia**(0.5)
    return (desvio)
main()
