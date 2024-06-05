class Tests:
    def __init__(self, jautajumi):
        self.jautajumi = jautajumi
        
    def pildit_testu(self):  
        for i, q in enumerate(self.jautajumi, 1):
            print("--------------------------------------------------------------------------------")
            print(f"\nJautajums {i}: {q['jautajums']}")
            for atbilde in q['atbildes']:
                print(atbilde)
                
jautajumi = [
    {
        "jautajums": "...",
        "atbildes": ["A) ...", 
                     "B) ...", 
                     "C) ...", 
                     "D) ..."],
        "pareizas_atbildes": {"A", "C"}
    }
]

T = Tests(jautajumi)
T.pildit_testu()
