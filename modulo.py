class Pelicula :
    def __init__(self,num_identi,titulo,importe,tipo,num_origen):
        self.num_identi=num_identi
        self.titulo=titulo
        self.importe=importe
        self.tipo=tipo
        self.num_origen=num_origen
        
    def __str__(self):
        return "Numero de Indentificación: " + str(self.num_identi) + "-Titulo: " + str(self.titulo) + \
               "-Importe: " + str(self.importe) + "-Tipo: " + str(self.tipo) + "-Numero de origen: " + str(self.num_origen)
               
#.............................funciones de soporte............................ ............................
def validar_n():
    n=int(input("Ingrese la cantidad de Elementos a cargar: "))
    while n <= 0:
        n=int(input("Errooor,Ingrese nuevamente la cantidad: "))
    return n

#inserción ordenada binaria
#menor a mayor segun titulo
def insertar_ordenado(vec,pelicula):
    n=len(vec)
    pos= n
    iz= 0 
    de = n-1 
    while iz <= de:
       
        c= (iz + de ) // 2
        if vec[c].titulo == pelicula.titulo:
            pos=c
            break
        elif pelicula.titulo < vec[c].titulo:
            
            de = c-1
        else:
           
            iz = c + 1
          
    if iz > de:
        pos= iz
   
    vec[pos:pos]= [pelicula]
