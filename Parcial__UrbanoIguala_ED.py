#*Urbano Iguala, 9-744-1120*
#*Estructura de Datos 1*
#*Parcial 1*

import array
import pprint
import numpy as np
import queue
import random

#* Se crea el Array A1, el cual tomara valores random entre 1 y 20 minutos* 
A1= []
for i in range (60):
    A1.append(random.randint (1,20))

#*Ordenamos el Array, simulando que los clientes con menor tiempo de espera seran atendidos primero*
B1=np.sort(A1)[::]


#* Colocamos una estructura FIFO. First In First Out*
q1 = queue.Queue()
for i in range (60):
    c=B1[i]
    q1.put (c)

#* Inicializamos todos los metodos de las 3 taquillas en operacion, con el fin de llevar el control de los clientes atendidos y el total de tiempo en cada taquilla*   
A0=0
A1=0
A2=0
A4=0
B0=0
B1=0
B2=0
B4=0
C0=0
C1=0
C2=0
C4=0

#* Iniciamos un While que se ejecutara hasta que la fila este vacia*
while not q1.empty ():

#*Ya que en la estructura FIFO tenemos guardado el tiempo que lleva el cliente por ser atendido esperando en la fila, Solo se le asigna el tiempo a la taquilla que lo atendera*
#*Desde la taquilla asignada se leera el valor del tiempo que tiene esperando el cliente. Siendo A4, B4 y C4 el atributo que indica si la taquilla esta disponible para recibir clientes*
    if A4==0:
        T= q1.get()
    else:
        if B4==0:
            T= q1.get()
        else:
            if C4==0:
                T= q1.get()

#*Creamos la clase Taquilla 1. Si el se le es asigando el cliente. Self.cliente tomara el tiempo de espera del cliente*          
    class Taquilla1 :
        def __init__(self, T_Val=T):
            self.cliente= T_Val

#*Cada clase tiene un metodo de temporizador el cual indicara si la taquilla esta libre para tomar un nuevo cliente*
        def temporizador (self):
            if (A4>0):
                self.temporizador =A4
                return self.temporizador
            else:
                self.temporizador =0
                return self.temporizador
            
#* Cada clase, va ir acumulando el tiempo de atencion de los clientes atendidos y sumando el tiempo del nuevo cliente*
        def tiempo (self,TT=A1):
            tiempo=self.cliente
            TT += tiempo
            self.tiempo = TT
            return self.tiempo
#*Se va ir acumulando la cantidad de clientes que se llevan atendidos hasta ese momento
        def cont_Clientes (self, c=A2):
            c+=1
            self.cont_Clientes =c
            return self.cont_Clientes
        
#*Mientras se va atendiendo un nuevo cliente se muestra la cantidad de clientes atendidos hasta el momento y el tiempo acumulado en cada taquilla*
        def ArqueoTaq_1 (self):
            ArqueoTaq_1 = ("Taquilla1:  Clientes:{} Tiempo Acumulado:{} Minutos")
            print (ArqueoTaq_1.format (self.cont_Clientes,(round(self.tiempo,1))))

#* Se calcula el promedio de tiempo de atención de cada taquilla por cliente*
        def Mens_Final (self, CLI=A2, TMP=A1):
            prom=(float(TMP/CLI))
            Mens_Final= ("Taquilla1:  C. Atendidos:{}   Tiempo Promedio:{} Minutos")
            print (Mens_Final.format (CLI,(round(prom,1))))

       
    class Taquilla2:
        def __init__(self,tiempo=0, tiemp=0, contador=0, T_Val=T):
            self.cliente=T_Val
            self.contador=contador
        def temporizador (self):
            if (B4>0):
                self.temporizador =B4
                return self.temporizador
            else:
                self.temporizador =0
                return self.temporizador
        def tiempo (self,TT=B1):
            tiempo=self.cliente
            TT += tiempo
            self.tiempo = TT
            return self.tiempo
        def cont_Clientes (self, c=B2):
            c+=1
            self.cont_Clientes =c
            return self.cont_Clientes
        def ArqueoTaq_2 (self):
            ArqueoTaq_2 = ("Taquilla2:  Clientes:{} Tiempo Acumulado:{} Minutos")
            print (ArqueoTaq_2.format (self.cont_Clientes,(round(self.tiempo,1))))
        def Mens_Final (self, CLI=B2, TMP=B1):
            prom=(float(TMP/CLI))
            Mens_Final= ("Taquilla2:  C. Atendidos:{}   Tiempo Promedio:{} Minutos")
            print (Mens_Final.format (CLI,(round(prom,1))))
            
    class Taquilla3 :
        def __init__(self,tiempo=0, tiemp=0, contador=0, T_Val=T):
            self.cliente= T_Val
            self.contador=contador
        def temporizador (self):
            if (C4>0):
                self.temporizador =C4
                return self.temporizador
            else:
                self.temporizador =0
                return self.temporizador
        def tiempo (self,TT=C1):
            tiempo=self.cliente
            TT += tiempo
            self.tiempo = TT
            return self.tiempo
        def cont_Clientes (self, c=C2):
            c+=1
            self.cont_Clientes =c
            return self.cont_Clientes
        def ArqueoTaq_3 (self):
            ArqueoTaq_3 = ("Taquilla3:  Clientes:{} Tiempo Acumulado:{} Minutos")
            print (ArqueoTaq_3.format (self.cont_Clientes,(round(self.tiempo,1))))
        def Mens_Final (self, CLI=C2, TMP=C1):
            prom=(float(TMP/CLI))
            Mens_Final= ("Taquilla3:  C. Atendidos:{}   Tiempo Promedio:{} Minutos")
            print (Mens_Final.format (self.cont_Clientes,(round(prom,1))))


#* Se inicializan las instancias de las 3 clases (Taquillas)
    Taquilla1=Taquilla1 ()
    Taquilla2=Taquilla2 ()
    Taquilla3=Taquilla3 ()
    Taquilla1.temporizador ()
    Taquilla2.temporizador ()
    Taquilla3.temporizador ()

#* Si el temporizador de la taquilla es 0, es decir esta disponible, se ejecutan los metodos de esa taquilla, para acumular el nuevo cliente y el tiempo de atención*
    if A4 == 0:
        A0=Taquilla1.__init__()
        A1=Taquilla1.tiempo()
        A2=Taquilla1.cont_Clientes()
        A3=Taquilla1.ArqueoTaq_1 ()
        A4=T  
    else :
        if B4== 0:
            B0=Taquilla2.__init__
            B1=Taquilla2.tiempo()
            B2=Taquilla2.cont_Clientes()
            B3=Taquilla2. ArqueoTaq_2 ()
            B4=T
        else:
            if C4== 0:
                C0=Taquilla3.__init__
                C1=Taquilla3.tiempo()
                C2=Taquilla3.cont_Clientes()
                C3=Taquilla3. ArqueoTaq_3 ()
                C4=T
#* Si las tres taquillas estan ocupadas, la cola se mantiene en espera y se va descontando en cada una de las taquillas 1 minuto a la vez en cada una, hasta que una de ellas llegue a cero*
#*Esto indicaria que la taquilla esta disponible para atender un nuevo cliente*
    if A4<B4:
        if A4<C4:
            for i in range (A4):  
                if A4>0:
                    A4=A4-1
                else:
                    A4=0
                if B4>0:
                    B4=B4-1
                else:
                    B4=0
                if C4>0:
                    C4=C4-1
                else:
                    C4=0
        else:
            if B4<C4:
                for i in range (B4):  
                    if A4>0:
                        A4=A4-1
                    else:
                        A4=0
                    if B4>0:
                        B4=B4-1
                    else:
                        B4=0
                    if C4>0:
                        C4=C4-1
                    else:
                        C4=0
    else:
        for i in range (C4):  
            if A4>0:
                A4=A4-1
            else:
                A4=0
            if B4>0:
                B4=B4-1
            else:
                B4=0
            if C4>0:
                C4=C4-1
            else:
                C4=0
                
#* Se imprimen el total de clientes atendidos y el promedio de espera de los clientes en cada taquilla*
print ("\n\nArqueo de Taquilla Estadio RodCarew\n")               
Taquilla1.Mens_Final ()
Taquilla3.Mens_Final ()
Taquilla2.Mens_Final ()


        
            





              




   






