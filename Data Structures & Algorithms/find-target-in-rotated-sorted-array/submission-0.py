from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Se l'array è vuoto, il target non può essere presente.
        if not nums:
            return -1

        # Memorizziamo la dimensione complessiva dell'array.
        # Questo valore sarà il modulo fondamentale per la rimappatura circolare degli indici.
        n = len(nums)

        # -------------------------------------------------------------------------
        # FASE 1: Trovare l'indice del valore minimo (punto di rotazione / pivot)
        # Complessità temporale: O(log n)
        # -------------------------------------------------------------------------
        left = 0
        right = n - 1

        # Eseguiamo una binary search modificata per convergere sull'indice dell'elemento più piccolo.
        while left < right:
            mid = (left + right) // 2

            # Se l'elemento centrale è strettamente maggiore dell'elemento all'estrema destra,
            # significa che il punto di rottura (e quindi il minimo assoluto) si trova
            # obbligatoriamente nella metà destra dell'intervallo esaminato.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Altrimenti, la sequenza tra mid e right è regolarmente ordinata, quindi
            # il minimo deve trovarsi nella metà sinistra oppure coincidere con mid stesso.
            else:
                right = mid

        # Alla conclusione del ciclo, 'left' (o 'right') punta esattamente all'indice del minimo.
        # Questo indice rappresenta l'offset con cui l'array originale è stato ruotato.
        min_index = left

        # -------------------------------------------------------------------------
        # FASE 2: Ricerca Binaria Modulare
        # Complessità temporale: O(log n)
        # -------------------------------------------------------------------------
        # Lavoriamo in uno spazio "virtuale" da 0 a n - 1 dove immaginiamo che la lista
        # sia ordinata normalmente partendo dal valore minimo fino al massimo.
        left = 0
        right = n - 1

        # Condizione classica della ricerca binaria standard (nessun modulo qui).
        while left <= right:
            # Calcoliamo il centro nello spazio virtuale non ruotato.
            mid_virtuale = (left + right) // 2

            # Trasliamo l'indice virtuale sull'indice fisico reale sommando l'offset (min_index)
            # e applicando il modulo '% n' per riavvolgere all'inizio dell'array se superiamo la fine.
            real_mid = (mid_virtuale + min_index) % n

            # Controlliamo se l'elemento nella posizione effettiva dell'array corrisponde al target.
            if nums[real_mid] == target:
                # Trovato: restituiamo l'indice reale nell'array ruotato originario.
                return real_mid

            # Se il target cercato è minore dell'elemento esaminato,
            # ci spostiamo nella metà sinistra dello spazio virtuale (senza modulo).
            elif target < nums[real_mid]:
                right = mid_virtuale - 1

            # Se il target cercato è maggiore dell'elemento esaminato,
            # ci spostiamo nella metà destra dello spazio virtuale (senza modulo).
            else:
                left = mid_virtuale + 1

        # Se l'intervallo virtuale si esaurisce senza aver trovato il target,
        # restituiamo -1 a indicare che il valore non è presente nell'array.
        return -1