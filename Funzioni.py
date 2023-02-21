def switchCase(risposta):
    if risposta == "1":
        domanda = "Spiegami le regole generali del baseball"
    elif risposta== "2":
        domanda = "Spiegami da quali fasi è composto un inning nel baseball"
    elif risposta == "3":
        domanda = "Quali sono i principali ruoli difensivi nel baseball?"
    elif risposta == "4":
        domanda = "ruoli"
    elif risposta == "5":
        domanda = "come funziona la fase di battuta nel baseball?"
    elif risposta == "6":
        domanda = "Quali sono le tipologie di lancio più comuni nel baseball?"
    elif risposta == "7":
        domanda = "Quali sono i diversi modi in cui è possibile segnare punti nel baseball?"
    elif risposta == "8":
        domanda = "Cos'è un Grand Slam nel baseball?"
    elif risposta == "9":
        domanda = "Spiegami la regola del Ground Rule Double nel baseball"
    elif risposta == "10":
        domanda = "Spiegami la regola dell'Infield Fly nel baseball"
    elif risposta == "11":
        domanda = "Quali sono le differenze principali tra baseball americano e baseball giapponese?"
    else:
        print("Input errato!")
        domanda = "nulla"
    return domanda

def switchCasePos(risposta):
    if risposta == "1":
        domanda = "Spiegami il ruolo del pitcher nel baseball"
    elif risposta == "2":
        domanda = "Spiegami il ruolo del catcher nel baseball"
    elif risposta == "3":
        domanda = "Spiegami il ruolo del prima base nel baseball"
    elif risposta == "4":
        domanda = "Spiegami il ruolo del seconda base nel baseball"
    elif risposta == "5":
        domanda = "Spiegami il ruolo dello shortstop nel baseball"
    elif risposta == "6":
        domanda = "Spiegami ilruolo del terza base nel baseball"
    elif risposta == "7":
        domanda = "Spiegami il ruolo degli outfielders nel baseball"
    else:
        print("Input errato!")
        domanda = "nulla"
    return domanda