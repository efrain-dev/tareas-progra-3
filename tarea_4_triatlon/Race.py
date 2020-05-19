import time

from tarea_4_triatlon.Person import Person


class Race:
    segundos = 0
    ganador = ""
    runK = 10000
    pedalK = 20000
    swimK = 1000
    teamWrites = 2
    travel = list()

    def stopWatch(self):

        p = Person()
        self.initRecorrido()
        while True:
            resultado = False
            self.segundos = self.segundos + 1
            for nTeam in range(self.teamWrites):

                if self.travel[nTeam] <= self.runK:
                    self.travel[nTeam] = self.runZ(nTeam, p)
                    print("Total Recorrido " + str(self.travel[nTeam]) + "del Team " + str(nTeam))
                    if self.travel[nTeam] == self.runK:
                        print("Cambio de Relevo team " + str(nTeam))

                elif self.runK <= self.travel[nTeam] <= self.runK + self.pedalK:
                    self.travel[nTeam] = self.pedalZ(nTeam, p)
                    print("Total Recorrido " + str(self.travel[nTeam]) + "del Team " + str(nTeam))
                    if self.travel[nTeam] == self.runK + self.pedalK:
                        print("Cambio de Relevo team " + str(nTeam))

                elif self.runK + self.pedalK <= self.travel[nTeam] <= self.runK + self.pedalK + self.swimK:
                     self.travel[nTeam] = self.swimZ(nTeam, p)
                     print("Total Recorrido " + str(self.travel[nTeam]) + " del Team " + str(nTeam))

                elif self.travel[nTeam] >= self.runK + self.pedalK + self.swimK:
                     self.ganador = (str(nTeam) + " Con un tiempo de :" + str(int((self.segundos / 60) / 60)) + ":" + str(
                     int(self.segundos / 60)) + ":" + str(self.segundos) + "Hras")
                     resultado = True
                     break

            if resultado == True:
                break
        return self.ganador

    def initRecorrido(self):
        for x in range(self.teamWrites):
            self.travel.append(0)

    def runZ(self, nTeam, p):
        for x in p.TeamList:

            if x.type == "Correr" and x.nTeam == nTeam:
                print(x.type)
                return x.run(x, self.travel[nTeam])

    def pedalZ(self, nTeam, p):
        for x in p.TeamList:
            if x.type == "Pedalear" and x.nTeam == nTeam:
                print(x.type)
                return x.run(x, self.travel[nTeam])

    def swimZ(self, nTeam, p):
        for x in p.TeamList:

            if x.type == "Nadar" and x.nTeam == nTeam:
                print(x.type)
                return x.run(x, self.travel[nTeam])
