class _usuario:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.continuar = None

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valornombre):
        if isinstance(valornombre, str):
            self.__nombre = valornombre
            print(f"Guardado con éxito: {valornombre}")




        