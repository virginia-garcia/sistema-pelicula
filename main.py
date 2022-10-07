from modulo import *
import random
import pickle
import os.path

#funciones auxiliares
#carga el vector 
def cargar_vector(n,vec):
    for i in range(n):
         num_identi=random.randint(1,100)
         titulo= "Pelcula" + str(num_identi)
         importe=round(random.uniform(100,1000), 2)
         tipo=random.randint(0,9)
         num_origen=random.randint(0,19)
         pelicula=Pelicula(num_identi,titulo,importe,tipo,num_origen)
         insertar_ordenado(vec,pelicula)
        
   
   

#muestra el  vector cargado
def mostrar_vector(vec):
    for pelicula in vec:
        print(pelicula)
#muestra el vector en el cual el numero de origen d ela pelicula sea igual a un valor ingresado 
def mostrar_vector_origen(vec,p):
    busqueda= False
    for pelicula in vec:
        if pelicula.num_origen == p:
            print(pelicula)
            busqueda= True
    if not busqueda:
        print("No se encontró una pelicula igual que "+str(p))

#crea  un archivo en el cual en numero de origen sea distinto de 10 y el importe de la pelicula sea menor a un valor ingresado por teclado
def crear_archivo(vec,x,archivo):
    m= open(archivo, "wb")
    for pelicula in vec:
        if pelicula.num_origen != 10 and pelicula.importe < x:
            pickle.dump(pelicula, m)
    m.close()
    
#muestra el archivo generado
def mostrar_archivo(archivo):
    #verificar si el archivo existe
    if not os.path.exists(archivo):
        print("No existe el archivo")
    else:
        #abrir el archivo para leer
        m= open(archivo, "rb")
        #recorrer obteniendo el tamaño
        t= os.path.getsize(archivo)
        while m.tell() < t:
            pelicula = pickle.load(m)
            print(pelicula)
            
        m.close()


#busca un num ingresado por teclado y muestra si ese valor es igual a un numero de dentifiacion de la pelicula,sino es asi, informa con un mensaje
def buscar_num(vec,num):
    busqueda=None
    for i in range(len(vec)):
        if vec[i].num_identi == num:
            busqueda= vec[i]
            break
    return busqueda
#genera matriz por cada posible tipo y numero de origen 
    m = [[0] * 10 for fila in range(20)]

    for i in range(len(vec)):
        f = vec[i].num_origen
        c = vec[i].tipo
        m[f][c] += 1

    return m

#muetra los distintos de 0
def mostrar_matriz(m):
    for f in range(len(m)):
        for c in range(len(m[f])):
            if m[f][c] != 0:
                print('Para el tipo ', c, 'y el numero de orginen', f, 'hay',
                      m[f][c], 'peliculas')

def menu():
    print("*************************************************")
    print("Opción 1: Cargar Vector ")
    print("Opción 2: Mostrar vector sin condición ")
    print("Opcion 3: Mostrar vector segun un valor cargado")
    print("Opción 4: Crear Archivo ")
    print("Opción 5: Mostrar Archivo ")
    print("Opción 6: Busqueda binaria")
    print("Opción 7: Matriz ")
    print("Opción 8: Salir ")
    print("***********************************************")

#función principal
def main():
    vec=[]
    op=0
    archivo="Pelicula.dat"
    while op != 8:
        menu()
        op=int(input("Ingrese una opción: "))
        if op ==1:
            n=validar_n()
            cargar_vector(n,vec)
            
        elif vec != []:
            if 2 <= op <= 8:
                if op == 2:
                    mostrar_vector(vec)
                    
                elif op == 3:
                    p=int(input("Ingrese un numero de origen: "))
                    mostrar_vector_origen(vec,p)
                elif op == 4:
                    x=float(input("Ingrese un importe: "))
                    crear_archivo(vec,x,archivo)
                elif op == 5:
                    mostrar_archivo(archivo)
               
                elif op == 6:
                    num=int(input("Ingrese el numero a buscar: "))
                    pelicula=buscar_num(vec,num)
                    if pelicula is None:
                        print("No se encontró la pelicula ")
                    else:
                        print(pelicula)
               
                elif op == 7:
                    m=generar_matriz(vec)
                    mostrar_matriz(m)
                elif op == 8:
                    print("Programa Finalizado... vuelva pronto :) ")
                else:
                    print("Ingrese una opcion valida,entre 1 y 8")
                
          
        else:
            print("El vector no está cargado,ejecute la opcion 1 para continuar")
        
        
       
if __name__ == "__main__":
    main()
