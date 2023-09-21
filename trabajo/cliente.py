
class Cliente: 

   
    def __init__ (self, nombre, mail, edad, local, producto):
        self.nombre = nombre
        self.mail = mail
        self.edad = edad
        self.local = local
        self.producto = producto
    
    def __str__(self):
       return f"{self.nombre} de {self.edad} con su mail {self.mail} ha comprado del local {self.local} el producto {self.producto}"
