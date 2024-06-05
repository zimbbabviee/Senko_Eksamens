class Tests:
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
                
            input_atbilde = input("\nIespējamas vairākas pareizas atbildes.\nIevadi pareizo atbilžu burtus atdalot ar komatu (piemēram A,B,C): ").replace(" ", "").upper()
            lietotaja_atbilde = set(input_atbilde.split(','))
            
            if lietotaja_atbilde == q['pareizas_atbildes']:
                pareizas_atbildes = pareizas_atbildes + 1
                print(pareizas_atbildes)
            else:
                nepareizi_atbildets.append(i-1)
        print("#####################################################################################")
        print("\nAtbildēts pareizi uz ",pareizas_atbildes," jautājumiem.\n")
        
        if len(nepareizi_atbildets) > 0:
            print("Nepareizi atbildēti jautājumi: \n")
                
jautajumi = [
    {
        "jautajums": "...",
        "atbildes": ["A) ...", 
                     "B) ...", 
                     "C) ...", 
                     "D) ..."],
        "pareizas_atbildes": {"A", "C"}
    },
    {
        "jautajums": "...",
        "atbildes": ["A) ...", 
                     "B) ...", 
                     "C) ...", 
                     "D) ..."],
        "pareizas_atbildes": {"A", "B"}
    }
]

T = Tests(jautajumi)
T.pildit_testu()
