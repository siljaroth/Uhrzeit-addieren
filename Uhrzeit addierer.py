def uhrzeit_minuten_addieren(stunden,minuten,summand):
    while minuten+summand >= 60: 
        stunden=stunden+1 
        minuten=minuten-60 
    if stunden >= 24:
        stunden=stunden-24 
    print(stunden,+minuten+summand)

uhrzeit_minuten_addieren(23,55,6)
uhrzeit_minuten_addieren(16,10,1111)