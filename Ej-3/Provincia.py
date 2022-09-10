class Provincia:
    __nombre=""
    __superficieAf= 0.0

    def __init__(self, nom, sup):
        self.__nombre= nom
        self.__superficieAf= sup

    def __str__(self):
        nombre=self.__nombre.center(10)
        return (f" {nombre} - {self.__superficieAf}")

    def getNombre(self):
        return self.__nombre
    def getSuperficie(self):
        return self.__superficieAf

    def __gt__(self, other):
        return self.__superficieAf < other.__superficieAf
