x = input("Inserisci Stringa:")
y = (x[2:-2]) #taglio ad x i primi e gli utlimi due caratteri della stringa
s = 2 # creo un dividendo
z = [y[i:i+s] for i in range(0, len(y), s)] #prendo y e lo scompongo usando s
w = [int(w, 16) for w in z] #converto z e lo trasformo in una lista hex
f = sum(w) #sommo gli elementi della lista
M = (x[-2:]) #creo una stringa isolando gli ultimi due caratteri di CRC
K = [int(M, 16)] #converto la stringa HEX isolata e la converto in decimale
g = (hex(f)[-2:]) ## converto la somma in HEX
print(g, "VALORE DI CONTROLLO", g.lower())
print(M, "VALORE DI RISCONTRO", M.lower())
print(x) #ristampo la stringa iniziale
if g.lower() == M.lower(): #se il valore di g(trasformato minuscolo) e M (trasformato minuscolo) è lo stesso allora 
    print("CRC VERIFICATO") #stampa 
if g.lower()!= M.lower(): #se i valori sono diversi allora
    print("ERRORE"); #stampa 





    
    

