#*Urbano Iguala, 9-744-1120*
#*Estructura de Datos 1*
#*LIFO y FIFO*

import array
import pprint
import numpy as np
import queue
import random

A1= []
A2= []
A3= []

for i in range (20):
    A1.append(random.randint (1,1000))
    A2.append(random.randint (1,1000))
    A3.append(random.randint (1,1000))

B1=np.sort(A1)[::-1]
B2=np.sort(A2)[::-1]
B3=np.sort(A3)[::-1]

print (B1, B2, B3)
print ("Arreglo 1 a Pila 1: ")

#First In First Out
q = queue.Queue()
for i in range (20):
    c=B1[i]
    q.put (c)
    print (c)

print ("Arreglo 2 a Pila 2: ")
#First In First Out
q2 = queue.Queue()
for i in range (20):
    d=B2[i]
    q2.put (d)
    print (d)

print ("Arreglo 3 a Cola 3: ")
#LiFo Last In First Out
q3 = queue.LifoQueue()
for i in range (20):
    e=B2[i]
    q3.put (e)
    print (e)

print ("Pila 1 y Pila 2 a Cola 2 ")
#LiFo Last In First Out
q4 = queue.LifoQueue()
for i in range (20):
    f=q.get(i)
    q4.put (f)
    g=q2.get(i)
    q4.put (g)
    print (f,g)
    
print ("Cola 1 a Pila 3: ")
#First In First Out
q5 = queue.Queue()
for i in range (20):
    h=q3.get(i)
    q5.put (h)
    print (h)

print ("Pila 1 y Pila 2 a Cola 2: Numeros Primos ")
while not q4.empty ():
    for i in range (40):
        class primo:
            def __init__(self):
                self.o=q4.get(i) 
            def es_primo (self):
                if self.o<2:
                    return False
                for n in range(2, self.o):     
                    if self.o%n==0:
                        return False
                print (self.o,"Es Primo")
                return True
        primo1=primo()
        primo1.es_primo ()

print ("Cola 1 a Pila 3: Numeros Compuestos ")
while not q5.empty ():
    for i in range (20):
        class compuesto:
            def __init__(self):
                self.p=q5.get(i) 
            def es_compuesto (self):
                if self.p<2:
                    return False
                for n in range(2, self.p):     
                    if self.p%n==0:
                        print (self.p,"Es Compuesto")
                        return False
                return True
        compuesto1=compuesto()
        compuesto1.es_compuesto ()
              




   






