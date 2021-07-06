#*Urbano Iguala, 9-744-1120*
#*Estructura de Datos 1*
#*Parcial 1 problema 2*

import array


class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None
      
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

class doubly_linked_list:
   def __init__(self):
      self.first = None
      self.last = None
      
   def Nodata (self):
       return self.first ==  None
    
   def add_end(self, NewVal):  
      NewNode = Node(NewVal)
      if self.Nodata ():
          self.first = self.last= NewNode
      else:
          temp=self.last
          self.last = temp.next
          temp.next = NewNode
          self.first.prev = temp
          
   def add_first(self, NewVal):
      NewNode = Node(NewVal)
      if self.Nodata ():
          self.first = self.last= NewNode
      else:
          temp= NewNode
          temp.next = self.first
          self.first.prev = temp
          self.first = temp
   def Dele_end (self):
       if self.Nodata ():
           print ("La lista esta vacia")
       elif self.first.next == None:
           self.first=self.last = None
       else:
           self.last = None
   def Dele_first (self):
       if self.Nodata ():
           print ("La lista esta vacia")
       else:
           self.first= None
       
# Print the Doubly Linked list		
   def listprint(self):
       temp=self.first
       print ("Imprimimos la lista")
       while (temp is not None):
         print(temp.data)
         last=temp
         temp = temp.next
   def lstprint(self):
       temp=self.last
       while (temp is not None):
         print(temp.data)
         last=temp
         temp = temp.prev
              
class Student:
    def __init__(self):
        self.nombre=None
        self.apellido=None
        self.edad=None
        self.ID=None
        self.carnet=None
        self.carrera=None
    
    def Estudiante (self):
        self.nombre=str(input("Ingrese su nombre: "))
        self.apellido=str(input("Ingrese su Apellido: "))
        self.edad=str(input("Ingrese su edad: "))
        self.ID=str(input("Ingrese su Numero de Cedula o Pasaporte: "))
        self.carnet=str(input("Ingrese su Numero de Carnet: "))
        self.carrera=str(input("Ingrese la carrera que esta cursando: "))
        self.Estudiante= ("\nNom:" + self.nombre + " Ape:" + self.apellido + " Ed:" + self.edad + " ID:" + self.ID + " Carnet:" + self.carnet + " Carrera:" + self.carrera)
        return self.Estudiante
        
   
Estudiante1=Student()
A=Estudiante1.Estudiante()   
dllist = doubly_linked_list()
dllist.add_end("Nom:Laura Ape:Cornejo Ed:24 ID:4-784-1120 Carnet:040786 Carrera: Lic Admin")
dllist.add_end ("Nom:Juan Ape:Heredia Ed:29 ID:8-624-1120 Carnet:032786 Carrera:Ing Alimentos")
dllist.add_first ("Nom:Carlos Ape:Jimenez Ed:31 ID:2-784-1120 Carnet:018786 Carrera: Ing Indust")     
dllist.add_first  (A)
dllist.listprint()
dllist.lstprint()
dllist.Dele_first ()
dllist.Dele_end ()
dllist.listprint()
dllist.lstprint()






                  




       







