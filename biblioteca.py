import random

# se utiliza esta biblioteca de random para generar nombres de libros aleatorias, # porque no hay tiempo para ponerme a agregar a listas nombres reales de libros
class Librospredeterminados:
    def __init__(self):
        self.librosdecomedias = []
        self.librosderomance = []
        self.librosdehistoria = []
        self.librosdedivulgacion = []

    def generar_nombres_libros(self):
        nombres_base = [
            "El misterio", "Amor eterno", "Risas aseguradas", "La batalla final",
            "Ciencia para todos", "Historia oculta", "Viaje sin fin", "Corazones rotos",
            "El universo explicado", "Rey sin corona"
        ]
        for _ in range(7):
            self.librosdecomedias.append(random.choice(nombres_base) + " (Comedia)")
            self.librosderomance.append(random.choice(nombres_base) + " (Romance)")
            self.librosdehistoria.append(random.choice(nombres_base) + " (Historia)")
            self.librosdedivulgacion.append(random.choice(nombres_base) + " (Divulgación)")


class Registrarlibros(Librospredeterminados):
    def __init__(self):
        super().__init__()  
        self.libros = []
        self.nuevos = None
        self.cantidad = 0
        self.categoria = None
        self.todas_las_categorias = []
        self.categoria_comedia = []
        self.categoria_romance = []
        self.categoria_historia = []
        self.categoria_divulgacion = []
        self.decision0 = None
        self.decision = None
        self.decision2 = None
        self.decisionfinal = None

      
        self.generar_nombres_libros()
        self.categoria_comedia.extend(self.librosdecomedias)
        self.categoria_romance.extend(self.librosderomance)
        self.categoria_historia.extend(self.librosdehistoria)
        self.categoria_divulgacion.extend(self.librosdedivulgacion)

    
    def registro_nuevos_libros(self):
        self.cantidad = int(input("digite la cantidad de numero de libros que quiere usted registrar:"))
        contador = 1
        for i in range(self.cantidad):
            self.nuevos = str(input(f"{contador}.digite el nombre de su libro:"))
            while True:
                print("Muy bien ahora de las siguientes opciones cual genero literario es su libro:")
                print("1.comedia")
                print("2.romance")
                print("3.historia")
                print("4.divulgacion cientifica")
                print("5.otro")
                try:
                    self.categoria = int(input("digite la opcion correspondiente:"))
                    if self.categoria == 1:
                        self.categoria = "comedia"
                        self.todas_las_categorias.append(self.categoria)
                        self.categoria_comedia.append(self.nuevos)
                    elif self.categoria == 2:
                        self.categoria = "romance"
                        self.todas_las_categorias.append(self.categoria)
                        self.categoria_romance.append(self.nuevos)
                    elif self.categoria == 3:
                        self.categoria = "historia"
                        self.todas_las_categorias.append(self.categoria)
                        self.categoria_historia.append(self.nuevos)
                    elif self.categoria == 4:
                        self.categoria = "divulgacion cientifica"
                        self.todas_las_categorias.append(self.categoria)
                        self.categoria_divulgacion.append(self.nuevos)
                    elif self.categoria == 5:
                        self.categoria = str(input("digite el genero por fa: "))
                        self.todas_las_categorias.append(self.categoria)
                    break
                except ValueError:
                    print("por favor digite un numero")

            self.libros.append(self.nuevos)
            contador += 1

    def mostrar_libros(self):
        print("\n--- LIBROS DISPONIBLES ---")

        if hasattr(self, "libros_predeterminados"):
            print("\nLibros predeterminados:")
            for i, libro in enumerate(self.libros_predeterminados, 1):
                print(f"{i}. {libro}")

        if self.libros:
            print("\nLibros registrados por usted:")
            for i, libro in enumerate(self.libros, 1):
                print(f"{i}. {libro}")
        else:
            print("\nNo ha registrado libros todavía.")



    def preguntaralusuariosiquierevarlascategorias(self):
        self.decision = int(input("¿Quiere ver los libros que tenemos por categorias? digite 1 o sino 0: "))
        if self.decision == 1:
            while True:
                print("\nMira nuestros géneros:")
                print("1.comedia")
                print("2.romance")
                print("3.historia")
                print("4.divulgacion cientifica")
                self.decision2 = int(input("digite el numero de la categoria:"))
                contador = 1
                if self.decision2 == 1:
                    for i in self.categoria_comedia:
                        print(f"{contador}. {i}")
                        contador += 1
                elif self.decision2 == 2:
                    for i in self.categoria_romance:
                        print(f"{contador}. {i}")
                        contador += 1
                elif self.decision2 == 3:
                    for i in self.categoria_historia:
                        print(f"{contador}. {i}")
                        contador += 1
                elif self.decision2 == 4:
                    for i in self.categoria_divulgacion:
                        print(f"{contador}. {i}")
                        contador += 1
                self.decisionfinal = int(input("¿Quiere continuar? digite 1 o si no 0:"))
                if self.decisionfinal == 0:
                    break
                else:
                    print("continuemos...")
        else:
            print("no pasa nada")
