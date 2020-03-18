import os

class Proyecto():
    def __init__(self, nombre, dominio, lenguaje, url_git):
        self.nombre = nombre
        self.dominio = dominio
        self.lenguaje = lenguaje
        self.url_git =
        self.usuario = '{}-user'.format(self.nombre)

    def pasos():
        resource_principal = open('resources/ppal.txt')
        principal = open('{}/principal.txt'.format(self.nombre), 'w')

        self.tipo_python() if(lenguaje == 1) else self tipo_node()



    def tipo_python():
        pass

    def tipo_node():
        port = input('Puerto del servicio node')
        nginx = open('{}/nginx.txt'.format(self.nombre), 'w')
        pass

def main():
    lenguaje = input('Lenguaje:\n1. Python\n2. Node')
    dominio = input('Ingrese el dominio del proyecto')
    nombre_proyecto = input('Ingrese el nombre del proyecto')
    url = input('Ingrese la url del repositorio del proyecto')
    proyecto = Proyecto(nombre_proyecto, dominio, lenguaje, url)

if __name__=='__main__':
	main()
