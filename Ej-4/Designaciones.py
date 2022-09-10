class Designaciones:
    __anio=0
    __justicia=""
    __cargo=""
    __instancia=""
    __materia=""
    __canth=0
    __cantm=0

    def __init__(self, anio, just, carg, inst, mate, canth, cantm):
        self.__anio= anio
        self.__justicia= just
        self.__cargo= carg
        self.__instancia= inst
        self.__materia= mate
        self.__canth= canth
        self.__cantm= cantm

    def __str__(self):
        return(f"{self.__anio} - {self.__cantm}")

    def getCargo(self):
        return self.__cargo
    def getMateria(self):
        return self.__materia
    def getYear(self):
        return self.__anio
    def getCanth(self):
        return self.__canth
    def getCantm(self):
        return self.__cantm
