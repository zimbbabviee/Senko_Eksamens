﻿from tkinter import *

class Tests:
    def __init__(self, jautajumi):
        self.jautajumi = jautajumi
        self.root = root
        
        self.nepareizi_atbildets = []
        self.pareizas_atbildes = 0
        self.nr = 0
        
    def parbaudit_atbildi(self, var1, var2, var3, var4, atbilde):
        selected = []
        if var1.get():
            selected.append("A")
        if var2.get():
            selected.append("B")
        if var3.get():
            selected.append("C")
        if var4.get():
            selected.append("D")

        if set(selected) == atbilde:
            self.pareizas_atbildes = self.pareizas_atbildes + 1
        else:
            self.nepareizi_atbildets.append(self.nr)
        
        if (self.nr + 1 < len(self.jautajumi)):
            self.nr = self.nr + 1
            self.pildit_testu(self.nr)
        else:
            self.pazinot_rezultatu()
            
    def pazinot_rezultatu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
        pazinojums = Label(self.root, text="Testa izpilde beigusies", pady=20)
        pazinojums.pack()
        pazinojums = Label(self.root, text=f"Atbildēts pareizi uz {self.pareizas_atbildes} jautājumiem.\n", pady=20)
        pazinojums.pack()

        if(len(self.nepareizi_atbildets)>0):
            pazinojums = Label(self.root, text="Nepareizi atbildēti jautājumi:\n")
            pazinojums.pack()            

            container = Frame(self.root)
            canvas = Canvas(container)
            scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
            scrollable_frame = Frame(canvas)
            scrollable_frame.bind("<Configure>", lambda e: canvas.configure( scrollregion=canvas.bbox("all")))
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            for i in self.nepareizi_atbildets:
                nepareizs_jautajums = Label(scrollable_frame, text=f"Jautajums {i+1}: {self.jautajumi[i]['jautajums']}", width = 200, anchor="w", padx=50, justify="left")
                nepareizs_jautajums.pack()
                for atbilde in self.jautajumi[i]['atbildes']:
                    atbildes = Label(scrollable_frame, text=atbilde, width = 200, anchor="w", padx=50,)
                    atbildes.pack()
                nepareizs_jautajums = Label(scrollable_frame, text="\n")
                nepareizs_jautajums.pack()

            container.pack(fill=BOTH, expand=1)
            canvas.pack(side="left", fill="both", expand=1)
            scrollbar.pack(side="right", fill="y") 
        
    def pildit_testu(self, nr):
        for widget in self.root.winfo_children():
            widget.destroy()
            
        jautajums = Label(self.root, text=f"\nJautajums {nr + 1}: {self.jautajumi[nr]['jautajums']}", justify="left")
        jautajums.pack()
            
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
            
        checkbox1 = Checkbutton(self.root, text=self.jautajumi[nr]['atbildes'][0], width = 200, anchor="w", padx=50, variable=var1)
        checkbox2 = Checkbutton(self.root, text=self.jautajumi[nr]['atbildes'][1], width = 200, anchor="w", padx=50, variable=var2)
        checkbox3 = Checkbutton(self.root, text=self.jautajumi[nr]['atbildes'][2], width = 200, anchor="w", padx=50, variable=var3)
        checkbox4 = Checkbutton(self.root, text=self.jautajumi[nr]['atbildes'][3], width = 200, anchor="w", padx=50, variable=var4)
           
        checkbox1.pack()
        checkbox2.pack()
        checkbox3.pack()
        checkbox4.pack()
        
        submit_button = Button(root, text="Atbildēt", command=lambda: self.parbaudit_atbildi(var1, var2, var3, var4, self.jautajumi[nr]['pareizas_atbildes']))
        submit_button.pack()
        
    def palaist_testu(self):
        pazinojums = Label(self.root, text=f"Python while tests. \nTests sastāv no 10 jautājumiem, uz kuriem iespējamas 2 līdz 3 pareizas atbildes.", pady=50)
        pazinojums.pack()
        submit_button = Button(root, text="Sākt testu", command=lambda: self.pildit_testu(0))
        submit_button.pack()
        self.root.mainloop()
                
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

root = Tk()
root.title("Python while cikla tests")
root.geometry('800x450')

T = Tests(jautajumi)
T.palaist_testu()
