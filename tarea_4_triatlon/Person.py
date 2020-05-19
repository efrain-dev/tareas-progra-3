class Person:
    TeamList = list()
    typeSpeed = ["Correr", "Pedalear", "Nadar"]
    name = ""
    speed = 0
    type = ""
    nTeam = 0



    def view(self):
        print(self.name.ljust(15, " "), end="")
        print(str(self.speed).ljust(15, " "), end="")
        print(self.typeSpeed.ljust(15, " "), end="")
        print(str(self.nTeam).ljust(15, " "))

    def registerRunner(self, name, speed, zona, nTeam):
        p = Person()
        p.name = name
        p.speed = speed
        p.type = zona
        p.nTeam = nTeam
        return p

    def run(self, x, travel):
        travel = travel + x.speed
        return travel


