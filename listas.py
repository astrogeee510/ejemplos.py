import os
os.system("cls")

milista=[1,2,3,4]
print("toda la lista:", milista)
print("tercer  elemento:", milista[2])
print("total de elementos (largos)", len (milista))

milista.append(70)
print("la lista ahora:", milista)
#append agrega los numeros al final
#insert lo agrega en la posicion que se indica moviendo el numero que estaba en esa posicion
milista.insert(3,100)
print("la lista ahora:", milista)

#este lo pne donde se indica le vale caca lo que alla
milista[5]=22
print("la lista ahora:", milista)


'''try:
    num=int(input("ingrese un numero "))
except:
    num=0
    
milista.append(num)
print("la lista ahora:", milista)'''

'''i=0
while i < len(milista):
    print("pos:" ,i,"valor:",milista[i])
    i = i + 1'''



for j in range( len(milista)  ):
    print("pos:" ,j,"valor:",milista[j])
    j = j + 1
    
print("----")
    
for elemento in milista:
    print("valor:" ,elemento)