class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Inizializziamo l'array dei risultati con tutti zeri.
        # La lunghezza è uguale all'array di input.
        # Se per un giorno non troviamo una temperatura più alta, il suo valore rimarrà 0 di default.
        result = [0] * len(temperatures)
        
        # Lo stack terrà traccia degli INDICI dei giorni per i quali 
        # non abbiamo ancora trovato una giornata successiva più calda.
        stack = []
        
        # Usiamo un ciclo for per scorrere l'array. 
        # 'i' rappresenta l'indice (il giorno corrente).
        for i in range(len(temperatures)):
            
            # Il ciclo while si attiva SOLO se lo stack non è vuoto E
            # la temperatura del giorno attuale (temperatures[i]) è MAGGIORE 
            # della temperatura del giorno registrato in cima allo stack.
            # Leggiamo la temperatura del giorno in cima allo stack tramite: temperatures[stack[-1]]
            while stack and temperatures[i] > temperatures[stack[-1]]:
                
                # Se entriamo nel while, significa che la giornata di oggi è più calda.
                # Abbiamo quindi "risolto" l'attesa per il giorno che era in cima allo stack.
                # Estraiamo l'indice di quel giorno passato (rimuovendolo dallo stack).
                giorno_passato = stack.pop()
                
                # Calcoliamo quanti giorni sono trascorsi facendo una semplice sottrazione 
                # tra l'indice di oggi (i) e l'indice del giorno estratto.
                # Inseriamo il risultato direttamente nella posizione corretta dell'array 'result'.
                result[giorno_passato] = i - giorno_passato
                
            # Dopo aver risolto e rimosso tutti i giorni precedenti più freddi
            # (oppure se lo stack era vuoto fin dall'inizio),
            # inseriamo l'indice del giorno attuale nello stack.
            # Da questo momento in poi, anche il giorno attuale aspetterà una giornata più calda.
            stack.append(i)
            
        # Restituiamo l'array finale compilato. I giorni rimasti nello stack alla fine
        # (per cui il ciclo while non si è mai attivato) non hanno mai trovato una 
        # temperatura più alta, quindi mantengono lo 0 inserito all'inizio.
        return result