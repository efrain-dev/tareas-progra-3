from tarea_4_triatlon.Race import Race
from tarea_4_triatlon.Person import Person



class Main:
    while True:
        print("Bienvenido Al triatlon")
        print("1. Ingrese los participantes de los Equipos")
        print("2. Ver los Equipos")
        print("3. Inicio de la carrera")
        optionMenu = input("Inserte la opcion>> ")

        if optionMenu == "1":

            for y in range(2):
                print("==================================================================================")
                print("Ingreso del Equipo Numero " + str(y + 1))
                for x in range(3):
                    p = Person()
                    print("Especialidad en ", p.typeSpeed[x])
                    p.TeamList.append(p.registerRunner(input("Ingrese el nombre: "),
                                                         int(input("Ingrese su velocidad metros/seg: ")),
                                                         p.typeSpeed[x], y))
                print("==================================================================================")

        elif optionMenu == "2":
            p = Person()
            print("==================================================================================")
            print("=====                         Participantes de la carrera                    =====")
            print("Nombre: ".ljust(15, " "), end="")
            print("Velocidad: ".ljust(15, " "), end="")
            print("Zona: ".ljust(15, " "), end="")
            print("Equipo: ".ljust(15, " "))
            for x in p.TeamList:
                x.view()
                print("==================================================================================")




        elif optionMenu == "3":
            print("==================================================================================")
            r = Race()
            p = Person()
            ganador = r.stopWatch()
            print("El equipo ganador es: " + str(ganador))

            print("==================================================================================")



        elif optionMenu == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
