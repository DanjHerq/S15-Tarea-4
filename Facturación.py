
class Empresa:
    def __init__(self,nom="El Baratón",ruc="0999999999",tel="0995158698",dir="9 de Octubre y el Malecóm 2000"):
        self.nombre = nom
        self.ruc = ruc
        self.telefono = tel
        self.direccion = dir
    def mostrarEmpresa(self):
        print("Empresa: {:20}Ruc:{}".format(self.nombre,self.ruc))

class Cliente:
    def __init__(self,nom,ced,tel):
        self.nombre = nom
        self.cedula = ced
        self.telefono = tel
    
    def mostrarCliente(self):
        print(self.nombre,self.cedula,self.telefono)

class ClienteCorporativo(Cliente):
    def __init__(self,nom,ced,tel,contrato):
        super().__init__(nom,ced,tel)
        self.__contrato=contrato


    @property
    def contrato(self):  # getter: obtener el valor del atributo privado
        return self.__contrato
    @contrato.setter
    def contrato(self, value):  # setter: asigna un valor al atributo privado
        if value:
            self.__contrato = value
        else:
            self.__contrato = 'Sin contrato'

    def mostrarCliente(self):
        print(self.nombre,self.__contrato)

class ClientePersonal(Cliente):
    def __init__(self,nom,ced,tel,promocion=True):
        super().__init__(nom,ced,tel)
        self.__promocion=promocion

    @property
    def promocion(self): # getter: obtener el valor del atributo privado
        if self.__promocion == True:
            return "10% Descuento"
        else:
            return "No hay Promoción"


    def mostrarCliente(self):
        print(self.nombre,self.promocion)
    
# emp = Empresa()
# emp.mostrarEmpresa()
# print(emp.nombre)

cli1 = ClientePersonal("Daniel","0951476662","0994602596",True)
cli1.mostrarCliente()
