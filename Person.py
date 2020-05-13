class Person:
    TeamList = list()
    typeSpeed = ["Correr", "Pedalear", "Nadar"]
    name = ""
    speed = 0
    zona = ""
    nTeam = 0



    def view(self):
        print(self.name.ljust(15, " "), end="")
        print(str(self.speed).ljust(15, " "), end="")
        print(self.zona.ljust(15, " "), end="")
        print(self.team.ljust(15, " "))

    def registerRunner(self, name, speed, zona, nTeam):
        p = Person()
        p.name = name
        p.speed = speed
        p.zona = zona
        p.nTeam = nTeam
        return p

    def run(self,recorrido,p):
        recorrido = recorrido + p
        return recorrido


