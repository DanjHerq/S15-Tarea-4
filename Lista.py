class Lista:
    def __init__(self,tamaño=4):
        self.lista = []
        self.longitud = 0
        self.size = tamaño
    
    def insertar(self,valor):
        i=0
        enc = False
        while i < len(self.lista) and enc:
            if self.lista[i]==valor:
                enc=True
            i=i=+1
        if enc:
            self.lista= self.lista[:1]+[valor]+self.lista[i:]
            self.longitud+=1
        return enc
    
    def append(self,dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud += 1
            return True
        else:
            return False 
lista1 = Lista()
lista1.append(2)                
lista1.append(5)                
lista1.append(20)
print(lista1.insertar(5))         
