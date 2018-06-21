lista=[]

for i in range(20):
    a = int(input("Digite um número : "))
    lista.append(a)


print(lista)

contador1=0
contador2=19
cl=0

while cl<10:
    aux=lista[contador1]
    lista[contador1]=lista[contador2]
    lista[contador2]=aux
    contador1=contador1+1
    contador2=contador2-1
    cl=cl+1
    
lista2=[]
for i in range(len(lista)):
    lista2.append(lista[i])
print (lista2)
