from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Inizializziamo il puntatore sinistro al primo indice (0).
        left = 0
        
        # Inizializziamo il puntatore destro all'ultimo indice dell'array.
        right = len(nums) - 1

        # Usiamo 'while left < right': il ciclo si ferma quando i due puntatori convergono
        # esattamente sullo stesso elemento (left == right), che sara' il minimo assoluto.
        while left < right:
            # Calcoliamo l'indice del punto mediano arrotondato per difetto.
            mid = (left + right) // 2
            
            # CONFRONTO CHIAVE: confrontiamo l'elemento mediano con l'estremo destro.
            # Se nums[mid] e' maggiore di nums[right], significa che la rottura dell'ordinamento
            # (il punto di flesso dove si trova il numero piu piccolo) e' nella meta' destra.
            if nums[mid] > nums[right]:
                # Il minimo non puo' essere 'mid' (perche' nums[right] e' piu' piccolo di mid).
                # Spostiamo quindi con certezza la ricerca a destra: 'mid + 1'.
                left = mid + 1
                
            # Se nums[mid] <= nums[right], la meta' destra da mid a right e' ordinata regolarmente.
            # Il minimo non puo' essere a destra di mid, ma potrebbe essere proprio 'mid' stesso.
            else:
                # Restringiamo la ricerca alla meta' sinistra includendo 'mid'.
                # Non usiamo 'mid - 1' per non rischiare di scartare il minimo se fosse proprio 'mid'.
                right = mid
        
        # Quando left == right, i due puntatori sono collassati sull'unico elemento minimo possibile.
        return nums[left]