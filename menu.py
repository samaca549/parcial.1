from login import _usuario
from biblioteca import Registrarlibros

class Menu:
    def __init__(self):
        self.decision = None
        self.usuario = None
        self.biblioteca = Registrarlibros()

    def opciones(self):
        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Registrarse")
            print("2. Ver libros")
            print("3. Registrar libros")
            print("0. Salir")

            try:
                self.decision = int(input("Digite el número de su opción: "))
            except ValueError:
                print("Debe digitar un número válido")
                continue

            if self.decision == 1:
                self.registrar_usuario()
            elif self.decision == 2:
                self.biblioteca.mostrar_libros()
                self.biblioteca.preguntaralusuariosiquierevarlascategorias()

            elif self.decision == 3:
                self.biblioteca.registro_nuevos_libros()
            elif self.decision == 0:
                print("¡Hasta pronto!")
                break
            else:
                print("Opción inválida")

    def registrar_usuario(self):
        nombre = input("Digite su nombre: ")
        self.usuario = _usuario(nombre)
        print(f"Usuario {self.usuario.nombre} registrado con éxito.")

def main():
    m = Menu()
    m.opciones()

if __name__ == "__main__":
    main()
