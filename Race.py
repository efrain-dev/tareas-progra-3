import time

from Person import Person


class Race:
    segundos = 0
    ganador = ""
    runK = 10000
    pedalK = 20000
    swimK = 1000
    teamWrites = 2
    travel = list()

    def stopWatch(self):


        self.initRecorrido()
        while True:
            resultado = False

            time.sleep(1)
            self.segundos = self.segundos + 1
            for nTeam in range(self.teamWrites):

                if 0 >= self.travel[nTeam] <= self.runK:
                    self.travel[nTeam] = self.runZ(nTeam)
                    print("Total Recorrido " + str(self.travel[nTeam]) + "del Team " + str(nTeam))
                    if self.travel[nTeam] == self.runK:
                        print("Cambio de Relevo team " + str(nTeam))
                elif self.runK >= self.travel[nTeam] <= self.runK + self.pedalK:
                    self.travel[nTeam] = self.pedalZ(nTeam)
                    print("Total Recorrido " + str(self.travel[nTeam]) + "del Team " + str(nTeam))
                    if self.travel[nTeam] == self.runK + self.pedalK:
                        print("Cambio de Relevo team " + str(nTeam))
                elif self.runK + self.pedalK >= self.travel[nTeam] <= self.runK + self.pedalK + self.swimK:
                     self.travel[nTeam] = self.swimZ(nTeam)
                     print("Total Recorrido " + str(self.travel[nTeam]) + " del Team " + str(nTeam))
                elif self.travel[nTeam] >= self.runK + self.pedalK + self.swimK:
                    self.ganador = (str(nTeam)+" Con un tiempo de :"+str(int((self.segundos/60)/60))+":"+str(int(self.segundos/60))+":"+str(self.segundos)+ "Hras")
                    resultado = True

            if resultado == True:
                break

        return self.ganador

    def initRecorrido(self):
        for x in range(self.teamWrites):
            self.travel.append(0)

    def runZ(self, nTeam):
        p = Person()
        for x in p.TeamList:
            if x.zona == p.typeSpeed[0] and x.nTeam == nTeam:
                return x.run(self.travel[nTeam],x.speed)

    def pedalZ(self, nTeam):
        p = Person()
        for x in p.TeamList:
            if x.zona == p.typeSpeed[1] and x.nTeam == nTeam:
                return x.run(self.travel[nTeam],x.speed)

    def swimZ(self, nTeam):
        p = Person()
        for x in p.TeamList:
            if x.zona == p.typeSpeed[2] and x.nTeam == nTeam:
                return x.run(self.travel[nTeam],x.speed)
