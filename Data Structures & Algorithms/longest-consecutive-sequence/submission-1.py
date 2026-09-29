class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Creiamo il set una sola volta. L'implementazione interna di set() in Python 
        # è scritta in C ed è estremamente veloce. Questo rimuove anche i duplicati.
        nums_set = set(nums)
        
        # Inizializziamo la variabile per tracciare la lunghezza massima trovata.
        longest = 0
        
        # Cicliamo direttamente su nums_set. Questo garantisce che non valuteremo
        # mai lo stesso numero più di una volta, riducendo le iterazioni totali.
        for num in nums_set:
            
            # Verifichiamo se l'elemento attuale è l'inizio di una sequenza.
            # Se il numero precedente (num - 1) NON è nel set, allora 'num' è una testa.
            # Questo lookup in O(1) evita di processare numeri che stanno in mezzo a una sequenza.
            if num - 1 not in nums_set:
                
                # Invece di modificare 'num', usiamo un offset ('length') che parte da 1.
                # È più efficiente in termini di memoria e passaggi logici.
                length = 1
                
                # Sfruttiamo direttamente l'aritmetica nel controllo del while:
                # 'num + length' calcola a ogni ciclo il prossimo numero da cercare.
                # Evitiamo di usare flag booleani ('trovato') per avere un ciclo più pulito e veloce.
                while (num + length) in nums_set:
                    
                    # Se il consecutivo esiste, incrementiamo solo la lunghezza.
                    length += 1
                    
                # Il ciclo while si è fermato perché la sequenza si è interrotta.
                # Usiamo un if logico puro invece della funzione built-in max().
                # Un 'if' inline è leggermente più veloce di 'longest = max(longest, length)'
                # perché risparmia i tempi di invocazione della funzione a basso livello.
                if length > longest:
                    
                    # Aggiorniamo la variabile con il nuovo record.
                    longest = length
                    
        # Ritorniamo il valore massimo trovato alla fine dell'esecuzione.
        return longest