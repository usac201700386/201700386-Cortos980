#en esta parte se define la funcion que calcula la secuecia de Collataz de un numero N
def Collatz (N):
    listaC=[]               #se crea na lista donde se almacena la secuencia de un numero
    listaC.append(int(N))   #se tiene que agregar el primer termino de la secuecnia
    while True:             #este codigo se ejecuta hasta que halla finalizado la secuencia osea en 1
        if (N!=1):          #se evalua si el numero es mayor que 1 para poder ejecutar el cilo
            if (N%2==0):
                N=N/2       #estas condicionales evaluan si el numero es para o en caso contrario impar
            else:
                N=3*N+1
            listaC.append(int(N))
        else:
            break           #cuando la secucia termina se rompe el cicli y se procede a retornar la lista
    return listaC

#esta funcion lo que hace es crear un archivo en el cua se van a ecribir
#todas las secuencia de Collatz que se van a generar dadas las instrucciones

#se reciben dos parametros, el nombre del archivo , el numero maximo al que se desea llegar
def CrearArchivo(Nombre = 'collatz.txt',Collatz_Numero = 2):
    
    
    archivo = open(Nombre,'w')                      #el primer paso es abrir o crear un archivo por eso se utliza W
    print('Espere mientras se crea el archivo')
    # Este ciclo es el que ejecuta cuatas listas o secuencias de collatz se desean crear
    for i in range(2,Collatz_Numero+1):
    #durante cada iteracion se genera una secuencia de collaz hasta el numero i
    #luego se escribe en el archivo y se deja un espacio por cada lista por eso el '\n'
        archivo.write(str(Collatz(i)))
        archivo.write(str('\n'))
    # al finalizar se cierra el archivo y se indica en consola que ha finalizado
    archivo.close() #Siempre cerrar el archivo al finalizar la escritura
    print('\n el archivo se ha creado y esta finalizado')


#este es el numero maximo al que llegara por mi carner: 201700386
Collatz_Maximo=386
#se ejecutan la funcion que contiene los parametros indicados anterior mente
CrearArchivo('collatz.txt',Collatz_Maximo)
