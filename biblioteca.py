class Registrarlibros:
    def __init__(self):
        self.libros=[]
        self.nuevos=None
        self.cantidad=0
        self.categoria=None
        self.todas_las_categorias=[]
        self.categoria_comedia=[]
        self.categoria_romance=[]
        self.categoria_historia=[]
        self.categoria_divulgacion=[]
        self.decision0=None
        self.decision=None
        self.decision2=None
        self.decisionfinal=None
    def registro_nuevos_libros(self):
        self.cantidad=int(input("digite la cantidad de numero de libros que quiere usted registrar:"))
        contador=1
        for i in range (self.cantidad):
            self.nuevos=str(input(f"{contador}.digite el nombre de su libro:"))
            while True:
                print("Muy bien ahora de las siguientes opciones cual genero literario es su libro:")
                print("1.comedia")
                print("2.romance")
                print("3.historia")
                print("4.divulgacion cientifica")
                print("5.otro")
                try:
                    self.categoria=int(input("digite la opcion correspondiente:"))
                    if self.categoria==1:
                        self.categoria="comedia"
                        self.todas_las_categorias.append(self.categoria)
                        self.categoria_comedia.append(self.nuevos)
                    elif self.categoria==2:
                        self.categoria="romance"
                        self.todas_las_categorias.append(self.categoria)
                        self.categoria_romance.append(self.nuevos)
                    elif self.categoria==3:
                        self.categoria="historia"
                        self.todas_las_categorias.append(self.categoria)
                        self.categoria_historia.append(self.nuevos)
                    elif self.categoria==4:
                        self.categoria="divulgacion cientifica"
                        self.todas_las_categorias.append(self.categoria)
                        self.categoria_divulgacion.append(self.nuevos)
                    elif self.categoria==5:
                        self.categoria=str(input("digite el genero por fa"))
                        self.todas_las_categorias.append(self.categoria)
                    break
                except ValueError:
                    print("por favor digite un numero")

            self.libros.append(self.nuevos)
            contador+=1
    def mostrar_libros(self):
        contador1=1
        k=0
        self.decision0=str(input("digite ---si---, si quiere ver los libros digitados por usted o pues si no quiere entoncese ---no---"))
        if self.decision0=="si":
            for i in self.libros:
                print(f"{contador1}.el libro registrado por ustes es --{i}-- y es del genero {self.todas_las_categorias[k]}")
                contador1+=1
                k+=1
        else:
            print("no pasa nada continuemos")
    def preguntaralusuariosiquierevarlascategorias(self):
        self.decision=int(input("quiere ver los libros que tenemos por categorias digite 1 o sino 0:"))
        if self.decision==1:
            while True:
                print("mira nuestros generos:")
                print("1.comedia")
                print("2.romance")
                print("3.historia")
                print("4.divulgacion cientifica")
                self.decision2=int(input("digite el numero de la categoria:"))
                contador=1
                if self.decision2==1:
                    for i in self.categoria_comedia:
                        print(f"{contador}. {i}")
                        contador+=1
                elif self.decision2==2:
                    for i in self.categoria_romance:
                        print(f"{contador}. {i}")
                        contador+=1
                elif self.decision2==3:
                    for i in self.categoria_historia:
                        print(f"{contador}. {i}")
                        contador+=1
                elif self.decision2==4:
                    for i in self.categoria_divulgacion:
                        print(f"{contador}. {i}")
                        contador+=1
                self.decisionfinal=int(input("quiere continuar digite 1 o si no 0:"))
                if self.decisionfinal==0:
                    break
                else:
                    print("continuemos...")
        else:
            print("no pasa nada")
        
