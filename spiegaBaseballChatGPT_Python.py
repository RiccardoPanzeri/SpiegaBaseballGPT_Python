#importo la libreria openai
import openai
from Funzioni import *
#affinchè il programma funzioni, è necessario inserire qui la chiave API OpenAi personale.
openai.api_key = "Inserisci la tua chiave API qui"
#creiamo le variabili necessarie, che contengono: 
#il modello dell'engine di completamento automatico di OpenAI
modelloEngine = "text-davinci-003"
restart = True
rispiega = False
domanda = "default"
risposta = "default"
print("""Il Baseball è uno sport molto popolare negli Stati Uniti, ma quasi del tutto sconosciuto in Italia.
   Questo programma ha l'obbiettivo di spiegare ad un pubblico alle prime armi i fondamenti e le dinamiche di questo sport.""")

while restart == True:#mi assicuro che l'utente possa fare più di una domanda
#e l'input che verrà inserito dall'utente per interagire con l'AI
#con questa porzione di codice, andiamo a generare una risposta all'input, aggiustando i parametri di comportamento del bot:
    if rispiega == False:
        risposta = input("""cosa ti interessa sapere? (seleziona il numero della domanda nel menù, e premi invio)
        1-Spiegami le regole generali.
        2-Spiegami da quali fasi è composto un inning.
        3-Quali sono i principali ruoli difensivi nel baseball?
        4-Voglio sapere di più in merito agli specifici ruoli difensivi.
        5-Come funziona la fase di battuta?
        6-Quali sono le tipologie di lancio più comuni?
        7-Quali sono i diversi modi in cui è possibile segnare punti?
        8-Cos'è un "Grand Slam"?
        9-Spiegami la regola del "Ground Rule Double".
        10-Spiegami la regola dell'"Infield Fly".
        11-Quali sono le differenze principali tra baseball americano e baseball giapponese?
        """)
        domanda = switchCase(risposta);
        if risposta == "4":
            risposta = input("""Quale ruolo ti interessa?
            1-Spiegami il ruolo del pitcher.
            2-Spiegami il ruolo del catcher.
            3-Spiegami il ruolo del prima base.
            4-Spiegami il ruolo del seconda base.
            5-Spiegami il ruolo dello shortstop.
            6-Spiegami ilruolo del terza base.
            7-Spiegami il ruolo degli outfielders
       
            """) 
            domanda = switchCasePos(risposta)
    print(domanda + "\n")
    if domanda != "nulla":
        completion = openai.Completion.create(
            engine = modelloEngine,
            prompt = domanda,
            max_tokens = 1024,
            n= 1,
            stop = None,
            temperature = 0.5,#la temperatura influisce sulla coerenza della risposta: più è alta, più varia ma meno accurata sarà la risposta all'input.
        )


        risposta = completion.choices[0].text #inseriamo la risposta generata in una variabile;
        if rispiega == True:
            domanda = temp

        print(risposta)#stampo la risposta dell'AI a schermo
        print("\n")
        print("è tutto chiaro? oppure vuoi che te lo spieghi meglio? (premi 1 se vuoi che te lo rispieghi meglio, altrimenti premi un qualunque tasto:)")
        risposta = input();
        if risposta == "1":
            temp = domanda
            domanda = domanda + " In maniera semplice\n"
            rispiega = True
        else: 
            rispiega = False
            domanda = "default"
    
        
      
    

