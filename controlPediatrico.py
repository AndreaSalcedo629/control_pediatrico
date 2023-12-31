from pyknow import *
from pyknow import Fact
from pyknow import KnowledgeEngine
from pyknow import Rule
from pyknow import MATCH
from pyknow import OR
from pyknow import NOT

class ControlPediatria(KnowledgeEngine):
    def ingresar_datos(self):

        print("\nBIENVENIDO AL SISTEMA EXPERTO PARA CONTROL PEDIÁTRICO\n")
        edad = int(input("Ingrese la edad del niño: "))
        peso = float(input("Ingrese el peso del niño: "))
        altura = float(input("Ingrese la altura del niño en formato decimal (ej: 0.80): "))
        hab1, hab2, hab3, hab4 = "","","",""

        #Al año
        if edad == 1:
            hab1 = input("¿El niño se para solo?: ").lower()
            hab2 = input("¿El niño busca objetos escondidos?: ").lower()
            hab3 = input("¿El niño entiende una orden sencilla?: ").lower()
            hab4 = input("¿El niño bebe de un vaso sin ayuda?: ").lower()

        #A los dos años
        if edad == 2:
            hab1 = input("¿El niño salta en dos pies?: ").lower()
            hab2 = input("¿El niño es capaz de armar torres de 5 o más cubos?: ").lower()
            hab3 = input("¿El niño dice más de 20 palabras claras?: ").lower()
            hab4 = input("¿El niño es capaz de controlar su orina?: ").lower()

        #A los tres años
        if edad == 3:
            hab1 = input("¿El niño es capaz de caminar hacia atrás?: ").lower()
            hab2 = input("¿El niño es capaz de separar objetos grandes y pequeños?: ").lower()
            hab3 = input("¿El niño usa oraciones completas?: ").lower()
            hab4 = input("¿El niño se baña solo las manos y la cara?: ").lower()

        #A los cuatro años
        if edad == 4:
            hab1 = input("¿El niño lanza y agarra la pelota?: ").lower()
            hab2 = input("¿El niño copia figuras geométricas?: ").lower()
            hab3 = input("¿El niño es capaz de describir un dibujo?: ").lower()
            hab4 = input("¿Tiene un amigo especial?: ").lower()

        #A los cinco años
        if edad == 5:

            hab1 = input("¿El niño hace rebotar y agarra la pelota?: ").lower()
            hab2 = input("¿El niño puede dibujar una escalera?: ").lower()
            hab3 = input("¿El niño nombra 4 o más colores?: ").lower()
            hab4 = input("¿El niño propone juegos?: ").lower()



        self.declare(Fact(edad=edad))
        self.declare(Fact(peso=peso))
        self.declare(Fact(altura=altura))
        self.declare(Fact(hab1=hab1))
        self.declare(Fact(hab2=hab2))
        self.declare(Fact(hab3=hab3))
        self.declare(Fact(hab4=hab4))


    @Rule(Fact(edad=MATCH.edad) & Fact(peso=MATCH.peso) & Fact(altura=MATCH.altura))
    def regla_control_crecimiento(self, edad, peso, altura):
        print("\nCONTROL FISICO:\n")
        imc = round(peso / (altura ** 2), 1)
        print("El Índice de Masa Corporal (IMC) calculado es:", imc)

        rango_edades = {
            1: {"peso": (7, 12), "altura": (0.71, 0.80), "imc_bajo": 15.3, "imc_alto": 19.1},
            2: {"peso": (10, 15), "altura": (0.80, 0.91), "imc_bajo": 14.0, "imc_alto": 18.5},
            3: {"peso": (11, 17), "altura": (0.90, 1.02), "imc_bajo": 13.6, "imc_alto": 18.0},
            4: {"peso": (12, 19), "altura": (0.94, 1.09), "imc_bajo": 13.3, "imc_alto": 17.7},
            5: {"peso": (16, 27), "altura": (1.06, 1.24), "imc_bajo": 13.1, "imc_alto": 17.7}
        }

        recomendaciones = {
            "peso_adecuado": "El niño está en un peso adecuado para su edad",
            "peso_bajo": "El niño está en un peso muy bajo para su edad",
            "peso_alto": "El niño está en un peso muy elevado para su edad",
            "altura_adecuada": "El niño está en una altura adecuada para su edad",
            "altura_baja": "El niño tiene una altura baja para su edad",
            "altura_alta": "El niño es muy alto para su edad",
            "desnutricion": "El niño tiene desnutrición, se recomienda aumentar la ingesta de proteínas, hidratos de carbono y sales minerales, además de vitaminas y agua.",
            "sobrepeso": "El niño tiene sobrepeso, se recomienda reducir la ingesta de alimentos altos en calorías, grasas y azúcar",
            "imc_bajo": "Según su IMC, el niño podría estar bajo de peso, se recomienda aumentar la ingesta de proteínas, hidratos de carbono y sales minerales, además de vitaminas y agua"
        }

        if edad in rango_edades:
            rango = rango_edades[edad]
            if rango["altura"][0] <= altura <= rango["altura"][1]:
                print(recomendaciones["altura_adecuada"])
            elif altura < rango["altura"][0]:
                print(recomendaciones["altura_baja"])
            else:
                print(recomendaciones["altura_alta"])

            if rango["peso"][0] <= peso <= rango["peso"][1]:
                print(recomendaciones["peso_adecuado"])
                if imc < rango["imc_bajo"]:
                    print(recomendaciones["imc_bajo"])
            elif peso < rango["peso"][0]:
                print(recomendaciones["peso_bajo"])
                if imc < rango["imc_bajo"]:
                    print(recomendaciones["desnutricion"])
            else:
                print(recomendaciones["peso_alto"])
                if imc > rango["imc_alto"]:
                    print(recomendaciones["sobrepeso"])
                

    @Rule(Fact(edad=MATCH.edad), Fact(hab1=MATCH.hab1), Fact(hab2=MATCH.hab2), Fact(hab3=MATCH.hab3), Fact(hab4=MATCH.hab4))
    def regla_desarrollo_habilidades(self, edad, hab1, hab2, hab3, hab4):
            print("\nCONTROL MOTRIZ Y COGNITIVO:\n")
            if edad == 1:
                recomendaciones = {
                ("si","si","si","si"):"PROGRESO: ALTO - El niño tiene un correcto desarrollo motriz y de sus habilidades.",
                ("si","si","si","no"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, pero se recomienda adaptar los utensilios para que el niño pueda comer y beber por sí mismo.",
                ("si","si","no","si"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, pero se recomienda utilizar un lenguaje claro y sencillo o utilizar gestos y señales que puedan ser asimilados por el niño",
                ("si","si","no","no"):"PROGRESO: MEDIO BAJO - El desarrollo del niño es estable, pero se recomienda utilizar un lenguaje claro y sencillo o utilizar gestos y señales que puedan ser asimilados por el niño, además se recomienda adaptar los utensilios para que el niño pueda comer y beber por sí mismo.",
                ("si","no","si","si"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, pero se recomienda estimular las habilidades de búsqueda del niño, esta habilidad se irá adquiriendo gradualmente",
                ("si","no","si","no"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, pero se recomienda estimular las habilidades de búsqueda del niño, esta habilidad se irá adquiriendo gradualmente, además se recomienda adaptar los utensilios para que el niño pueda comer y beber por sí mismo.",
                ("si","no","no","si"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, pero se recomienda estimular las habilidades de búsqueda del niño, esta habilidad se irá adquiriendo gradualmente, además es importante utilizar un lenguaje claro y sencillo o utilizar gestos y señales que puedan ser asimilados por el niño",
                ("si","no","no","no"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, se recomienda estimular habilidades cognitivas y físicas, debe prestas especial atención al progeso, en caso de no progresar, debe acudir a un especialista",
                ("no","si","si","si"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, pero se recomienda brindar apoyo a sus habilidades motoras, brindando apoyo físico, si no presenta mejorías, consulte con un especialista",
                ("no","si","si","no"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, pero se recomienda brindar apoyo a sus habilidades motoras y adaptar los utensilios para que el niño pueda comer y beber por sí mismo.",
                ("no","si","no","si"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, pero se recomienda brindar apoyo a sus habilidades motoras y utilizar un lenguaje claro y sencillo o utilizar gestos y señales que puedan ser asimilados por el niño ",
                ("no","si","no","no"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, se recomienda estimular habilidades cognitivas y físicas, debe prestas especial atención al progeso, en caso de no progresar, debe acudir a un especialista",
                ("no","no","si","si"):"PROGRESO: MEDIO BAJO - El niño tiene un desarollo estable, pero se recomienda brindar apoyo a sus habilidades motoras y se recomienda estimular las habilidades de búsqueda del niño, esta habilidad se irá adquiriendo gradualmente",
                ("no","no","si","no"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, se recomienda estimular habilidades cognitivas y físicas, debe prestas especial atención al progeso, en caso de no progresar, debe acudir a un especialista",
                ("no","no","no","si"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, se recomienda estimular habilidades cognitivas y físicas, debe prestas especial atención al progeso, en caso de no progresar, debe acudir a un especialista",
                ("no","no","no","no"):"PROGRESO: MUY BAJO - El niño no presenta progreso, acuda a un especialista lo más pronto posible",
                }       

                key = (hab1, hab2, hab3, hab4)
                if key in recomendaciones:
                    print(recomendaciones[key])
                else:
                    print("No ha sido posible realizar el análisis, por favor intente de nuevo")


            if edad == 2:
                recomendaciones = {
                ("si","si","si","si"):"PROGRESO: ALTO - El niño tiene un correcto desarrollo motriz y de sus habilidades.",
                ("si","si","si","no"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, pero se recomienda establecer una rutina de idas al baño para que el niño se adapte a ellas",
                ("si","si","no","si"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, sin embargo puede estar expresando un retraso en el desarrollo del lenguaje, consulte con un especialista del habla, y adicionalmente, fomente las actividades de comunicación",
                ("si","si","no","no"):"PROGRESO: MEDIO BAJO - El desarrollo del niño es estable, se recomienda establecer una rutina de idas al baño para que el niño se adapte a ellas, tambien puede estar expresando un retraso en el desarrollo del lenguaje, consulte con un especialista del habla, y adicionalmente, fomente las actividades de comunicación",
                ("si","no","si","si"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, se recomienda realizar actividades de coordinación estimulen su actividad cerebral",
                ("si","no","si","no"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, se recomienda realizar actividades de coordinación estimulen su actividad cerebral, tambien recomienda establecer una rutina de idas al baño para que el niño se adapte a ellas",
                ("si","no","no","si"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, se recomienda realizar actividades de coordinación estimulen su actividad cerebral,  sin embargo puede estar expresando un retraso en el desarrollo del lenguaje, consulte con un especialista del habla, y adicionalmente, fomente las actividades de comunicación",
                ("si","no","no","no"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, pero se recomienda establecer una rutina de idas al baño para que el niño se adapte a ellas, tambien puede practicar ejercicios que fortalezcan su habilidad motora y coordinación y estimulen su actividad cerebral",
                ("no","si","si","si"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, puede practicar ejercicios que fortalezcan su habilidad motora y coordinación",
                ("no","si","si","no"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, puede practicar ejercicios que fortalezcan su habilidad motora y coordinación, tambien recomienda establecer una rutina de idas al baño para que el niño se adapte a ellas",
                ("no","si","no","si"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, puede practicar ejercicios que fortalezcan su habilidad motora y coordinación, sin embargo puede estar expresando un retraso en el desarrollo del lenguaje, consulte con un especialista del habla, y adicionalmente, fomente las actividades de comunicación",
                ("no","si","no","no"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, pero se recomienda establecer una rutina de idas al baño para que el niño se adapte a ellas, tambien puede practicar ejercicios que fortalezcan su habilidad motora y coordinación y estimulen su actividad cerebral, el niño puede estar expresando un retraso en el desarrollo del lenguaje, consulte con un especialista del habla, y adicionalmente, fomente las actividades de comunicación",
                ("no","no","si","si"):"PROGRESO: MEDIO BAJO - El niño tiene un desarollo estable, puede practicar ejercicios que fortalezcan su habilidad motora y coordinación y estimulen su actividad cerebral",
                ("no","no","si","no"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, pero se recomienda establecer una rutina de idas al baño para que el niño se adapte a ellas, tambien puede practicar ejercicios que fortalezcan su habilidad motora y coordinación y estimulen su actividad cerebral, el niño puede estar expresando un retraso en el desarrollo del lenguaje, consulte con un especialista del habla, y adicionalmente, fomente las actividades de comunicación",
                ("no","no","no","si"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, puede practicar ejercicios que fortalezcan su habilidad motora y coordinación y estimulen su actividad cerebral, el niño puede estar expresando un retraso en el desarrollo del lenguaje, consulte con un especialista del habla, y adicionalmente, fomente las actividades de comunicación",
                ("no","no","no","no"):"PROGRESO: MUY BAJO - El niño no presenta progreso, acuda a un especialista lo más pronto posible",
                }       

                key = (hab1, hab2, hab3, hab4)
                if key in recomendaciones:
                    print(recomendaciones[key])
                else:
                    print("No ha sido posible realizar el análisis, por favor intente de nuevo")

            if edad == 3:
                recomendaciones = {
                ("si","si","si","si"):"PROGRESO: ALTO - El niño tiene un correcto desarrollo motriz y de sus habilidades.",
                ("si","si","si","no"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, se recomienda fomentar habitos de limpieza y autocuidado",
                ("si","si","no","si"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, sin embargo puede estar expresando un retraso en el desarrollo del lenguaje, consulte con un especialista del habla, y adicionalmente, fomente las actividades de comunicación",
                ("si","si","no","no"):"PROGRESO: MEDIO BAJO - El desarrollo del niño es estable, se recomienda fomentar habitos de limpieza y autocuidado, el niño puede estar experimentando un retraso en el desarrollo del lenguaje, consulte con un especialista y adicionalmente, fomente las actividades de comunicación",
                ("si","no","si","si"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, se recomienda realizar actividades de clasificación que estimulen su actividad cerebral",
                ("si","no","si","no"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, se recomienda fomentar habitos de limpieza y autocuidado, puede practicar ejercicios que fortalezcan su habilidad motora y coordinación",
                ("si","no","no","si"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, puede practicar ejercicios que fortalezcan su habilidad motora y coordinación, sin embargo puede estar expresando un retraso en el desarrollo del lenguaje, consulte con un especialista del habla, y adicionalmente, fomente las actividades de comunicación",
                ("si","no","no","no"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, se recomienda fomentar habitos de limpieza y autocuidado, el niño puede estar experimentando un retraso en el desarrollo del lenguaje y retraso en sus habilidades motoras, consulte con un especialista y adicionalmente, fomente las actividades de comunicación",
                ("no","si","si","si"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, pero puede estar experimentando un retraso en sus habilidades motoras, se recomienda realizar actividades que estimulen estas actividades",
                ("no","si","si","no"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, se recomienda fomentar habitos de limpieza y autocuidado, el niño tambien puede estar experimentando un retraso en sus habilidades motoras, se recomienda realizar actividades que estimulen estas actividades",
                ("no","si","no","si"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, sin embargo puede estar expresando un retraso en el desarrollo del lenguaje y un retraso en sus habilidades motoras, consulte con un especialista, y adicionalmente, fomente las actividades de comunicación",
                ("no","si","no","no"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, sin embargo puede estar expresando un retraso en el desarrollo del lenguaje y un retraso en sus habilidades motoras, consulte con un especialista, y adicionalmente, fomente las actividades de comunicación y habitos de limplieza y autocuidado",
                ("no","no","si","si"):"PROGRESO: MEDIO BAJO - El niño tiene un desarollo estable, pero puede estar experimentando un retraso en sus habilidades motoras, se recomienda realizar actividades que estimulen estas actividades",
                ("no","no","si","no"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, sin embargo puede estar expresando un retraso en sus habilidades motoras, consulte con un especialista, y adicionalmente, fomente las actividades de comunicación y habitos de limplieza y autocuidado",
                ("no","no","no","si"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, sin embargo puede estar expresando un retraso en el desarrollo del lenguaje y un retraso en sus habilidades motoras, consulte con un especialista, y adicionalmente, fomente las actividades de comunicación",
                ("no","no","no","no"):"PROGRESO: MUY BAJO - El niño no presenta progreso, acuda a un especialista lo más pronto posible",
                }       

                key = (hab1, hab2, hab3, hab4)
                if key in recomendaciones:
                    print(recomendaciones[key])
                else:
                    print("No ha sido posible realizar el análisis, por favor intente de nuevo")


            if edad == 4:
                recomendaciones = {
                ("si","si","si","si"):"PROGRESO: ALTO - El niño tiene un correcto desarrollo motriz y de sus habilidades.",
                ("si","si","si","no"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, Se recomienda fortalecer las habilidades sociales y comunicativas del niño",
                ("si","si","no","si"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, Se recomienda estimular las habilidades comunicativas del niño",
                ("si","si","no","no"):"PROGRESO: MEDIO BAJO - El desarrollo del niño es estable, Se recomienda fortalecer las habilidades sociales y comunicativas del niño",
                ("si","no","si","si"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, Se recomienda estimular las habilidades motrices del niño",
                ("si","no","si","no"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, Se recomienda fortalecer las habilidades sociales y comunicativas del niño y estimular sus habilidades motrices",
                ("si","no","no","si"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, Se recomienda fortalecer las habilidades sociales y comunicativas del niño y estimular sus habilidades motrices",
                ("si","no","no","no"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, Se recomienda fortalecer las habilidades sociales y comunicativas del niño y estimular sus habilidades motrices",
                ("no","si","si","si"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, Se recomienda estimular las habilidades motrices del niño",
                ("no","si","si","no"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, Se recomienda fortalecer sus habilidades sociales y comunicativas y estimular sus habilidades motrices",
                ("no","si","no","si"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, Se recomienda fortalecer sus habilidades comunicativas y estimular sus habilidades motrices",
                ("no","si","no","no"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, Se recomienda fortalecer las habilidades sociales y comunicativas del niño y estimular sus habilidades motrices",
                ("no","no","si","si"):"PROGRESO: MEDIO BAJO - El niño tiene un desarollo estable, Se recomienda estimular las habilidades motrices del niño",
                ("no","no","si","no"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, Se recomienda fortalecer las habilidades sociales del niño y estimular sus habilidades motrices",
                ("no","no","no","si"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, Se recomienda fortalecer las habilidades comunicativas del niño y estimular sus habilidades motrices",
                ("no","no","no","no"):"PROGRESO: MUY BAJO - El niño no presenta progreso, acuda a un especialista lo más pronto posible",
                }       

                key = (hab1, hab2, hab3, hab4)
                if key in recomendaciones:
                    print(recomendaciones[key])
                else:
                    print("No ha sido posible realizar el análisis, por favor intente de nuevo")


            if edad == 5:
                recomendaciones = {
                ("si","si","si","si"):"PROGRESO: ALTO - El niño tiene un correcto desarrollo motriz y de sus habilidades.",
                ("si","si","si","no"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, Se recomienda estimular sus habilidades sociales y participativas en el entorno",
                ("si","si","no","si"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, Se recomienda estimular las habilidades de reconocimiento de patrones, formas, colores, por medio de juegos educativos o canciones",
                ("si","si","no","no"):"PROGRESO: MEDIO BAJO - El desarrollo del niño es estable, Se recomienda estimular sus habilidades sociales, participativas en el entorno y de reconocimiento de patrones, formas, colores, por medio de juegos educativos o canciones",
                ("si","no","si","si"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, Se recomienda la estimulación motriz y fomentar la creatividad en el niño",
                ("si","no","si","no"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, Se recomienda la estimulación motriz y fomentar la creatividad en el niño, además de estimular sus habilidades sociales y participativas en el entorno",
                ("si","no","no","si"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, Se recomienda la estimulación motriz y fomentar la creatividad en el niño, además de estimular las habilidades de reconocimiento de patrones, formas, colores, por medio de juegos educativos o canciones",
                ("si","no","no","no"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, Se recomienda la estimulación motriz y fomentar la creatividad en el niño, además de estimular las habilidades sociales, patricipativas y de reconocimiento de patrones, formas, colores, por medio de juegos educativos o canciones",
                ("no","si","si","si"):"PROGRESO: MEDIO - El niño tiene un correcto desarrollo, El niño puede presentar un retraso en sus habilidades, estimule principalmente sus habilidades físicas y cognitivas",
                ("no","si","si","no"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, El niño puede presentar un retraso en sus habilidades, estimule sus habilidades físicas, sociales y participativas",
                ("no","si","no","si"):"PROGRESO: MEDIO BAJO - El niño tiene un desarrollo estable, El niño puede presentar un retraso en sus habilidades, estimule sus habilidades físicas, además de estimular las habilidades de reconocimiento de patrones, formas, colores, por medio de juegos educativos o canciones",
                ("no","si","no","no"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, El niño puede presentar un retraso en sus habilidades, estimule sus habilidades físicas, sociales, participativas en el entorno y de reconocimiento de patrones, formas, colores, por medio de juegos educativos o canciones",
                ("no","no","si","si"):"PROGRESO: MEDIO BAJO - El niño tiene un desarollo estable, El niño puede presentar un retraso en sus habilidades, estimule sus habilidades físicas, se recomienda también fomentar la creatividad en el niño",
                ("no","no","si","no"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, El niño puede presentar un retraso en sus habilidades, estimule sus habilidades físicas, motrices y fomente la creatividad en el niño, además de estimular sus habilidades sociales y participativas en el entorno",
                ("no","no","no","si"):"PROGRESO: BAJO - El niño tiene un desarrollo bajo, El niño puede presentar un retraso en sus habilidades, estimule sus habilidades físicas, motrices y fomente la creatividad en el niño, además de estimular las habilidades de reconocimiento de patrones, formas, colores, por medio de juegos educativos o canciones",
                ("no","no","no","no"):"PROGRESO: MUY BAJO - El niño no presenta progreso, acuda a un especialista lo más pronto posible",
                }       

                key = (hab1, hab2, hab3, hab4)
                if key in recomendaciones:
                    print(recomendaciones[key])
                else:
                    print("No ha sido posible realizar el análisis, por favor intente de nuevo")
            

if __name__ == "__main__":
    engine = ControlPediatria()
    engine.reset() 
    engine.ingresar_datos()
    engine.run()
