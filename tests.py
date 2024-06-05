﻿class Tests:
    def __init__(self, jautajumi):
        self.jautajumi = jautajumi
        
    def pildit_testu(self):
        nepareizi_atbildets = []
        pareizas_atbildes = 0
        
        for i, q in enumerate(self.jautajumi, 1):
            print("--------------------------------------------------------------------------------")
            print(f"\nJautajums {i}: {q['jautajums']}")
            for atbilde in q['atbildes']:
                print(atbilde)
                
            input_atbilde = input("\nIespējamas vairākas pareizas atbildes.\nIevadi pareizo atbilžu burtus atdalot ar komatu (piemēram a,b,c): ").replace(" ", "").upper()
            lietotaja_atbilde = set(input_atbilde.split(','))
            
            if lietotaja_atbilde == q['pareizas_atbildes']:
                pareizas_atbildes = pareizas_atbildes + 1
            else:
                nepareizi_atbildets.append(i-1)
        print("#####################################################################################")
        print("\nAtbildēts pareizi uz ",pareizas_atbildes," jautājumiem.\n")
        
        if len(nepareizi_atbildets) > 0:
            print("Nepareizi atbildēti jautājumi: \n")
            for i in nepareizi_atbildets:
                print(f"Jautajums {i+1}: {self.jautajumi[i]['jautajums']}")
                for atbilde in self.jautajumi[i]['atbildes']:
                    print(atbilde)
                print("")
                
jautajumi = [
    {
        "jautajums": "Kas raksturo parasto While ciklu?",
        "atbildes": ["a) while ciklā izpildās kāda koda daļa, kamēr izpildās kāds noteikts nosacījums", 
                     "b) while ciklā kods izpildās tikai vienu reizi", 
                     "c) while cikla sākumā tiek pārbaudīts nosacījums", 
                     "d) while cikla beigās tiek pārbaudīts nosacījums"],
        "pareizas_atbildes": {"A", "C"}
    },
    {
        "jautajums": "Kā iespējams pārtraukt visu While ciklu vai tā pašreizējo cikla izpildi?",
        "atbildes": ["a) ciklu nav iespējams pārtraukt", 
                     "b) ar operatoru break", 
                     "c) ar operatoru continue", 
                     "d) ar operatoru end"],
        "pareizas_atbildes": {"B", "C"}
    },
    {
        "jautajums": "While cikla veidi:",
        "atbildes": ["a) saraksta (list) while cikls (paredzēts sarakstu caurskatīšanai)", 
                     "b) beznosacījumu while cikls", 
                     "c) parastais while cikls", 
                     "d) bezgalīgais while cikls (while True)"],
        "pareizas_atbildes": {"C", "D"}
    },
    {
        "jautajums": "NEPAREIZI apgalvojumi ir:",
        "atbildes": ["a) continue nodrošina tūlītēju iziešanu no cikla, pārtraucot jebkuru tajā esošo darbību turpmāku izpildi", 
                     "b) continue atšķirībā no break ļauj izlaist pašreizējā soļa atlikušo daļu un nekavējoties pāriet pie nākamā soļa", 
                     "c) continue While ciklā netiek lietots", 
                     "d) continue izmantojams tikai kopā ar break"],
        "pareizas_atbildes": {"A", "C", "D"}
    },
    {
        "jautajums": "Kas notiek, ja while cikla nosacījums nekad nav False?",
        "atbildes": ["a) cikls izpildīsies mūžīgi (infinite loop)", 
                     "b) programma nekad neapstāsies", 
                     "c) cikls izpildīsies tikai vienu reizi", 
                     "d) cikls nekad nesāksies"],
        "pareizas_atbildes": {"A", "B"}
    },
    {
        "jautajums": "Ko dara break atslēgvārds while ciklā?",
        "atbildes": ["a) nodrošina tūlītēju iziešanu no cikla, pārtraucot jebkuru tajā esošo darbību turpmāku izpildi", 
                     "b) atsāk pildīt koda daļu ciklā no sākuma", 
                     "c) pārtrauc cikla izpildi", 
                     "d) izmaina cikla sākuma nosacījumu"],
        "pareizas_atbildes": {"A", "C"}
    },
    {
        "jautajums": "Kāda ir atšķirība starp while un while True:",
        "atbildes": ["a) while cikls darbojas tik ilgi, kamēr nosacījums ir patiess", 
                     "b) nav atšķirību", 
                     "c) while true tiek izpildīts, līdz to pārtrauc komanda break", 
                     "d) while true tiek izpildīts, līdz to pārtrauc komanda end"],
        "pareizas_atbildes": {"A", "C"}
    },
    {
        "jautajums": "PATIESI apgalvojumi par ciklu While ar else ir:",
        "atbildes": ["a) Python programmā while cikls ar else tiek izmantots, ja vēlaties kaut ko darīt pēc cikla beigām", 
                     "b) else darbojas tikai tad, ja cikla nosacījums kļūst nepatiess un cikls beidzas pats no sevis", 
                     "c) ja cikls tika pārtraukts agrāk ar break, kods else daļā netiks izpildīts", 
                     "d) while kopā ar else Python programmēšanā netiek izmantots"],
        "pareizas_atbildes": {"A", "B", "C"}
    },
    {
        "jautajums": """Kas notiks sekojošā kodā: 
        i=5
        while i > 7:
            print("Hello World")
        """,
        "atbildes": ["a) ekrānā tiks izvadīts Hello World piecas reizes", 
                     "b) cikla izpilde nekad nesāksies", 
                     "c) cikls darbosies bazgalīgi un visu laiku ekrānā tiks izvadīts Hello World", 
                     "d) no šī koda ekrānā nekas netiks izvadīts"],
        "pareizas_atbildes": {"B", "D"}
    },
    {
        "jautajums": """Sekojošajā kodā while cikls darbojas bezgalīgi:
        i=0
        while i < 5:
            print(i)   
        kuras no sekojošām programmas rindiņām var uzrakstīt zem print(i), lai cikls nebūtu bezgalīgs:
        """,
        "atbildes": ["a) i = i - 1", 
                     "b) i = i + 1", 
                     "c) i = 6", 
                     "d) break"],
        "pareizas_atbildes": {"B", "C", "D"}
    }
]

T = Tests(jautajumi)
T.pildit_testu()
