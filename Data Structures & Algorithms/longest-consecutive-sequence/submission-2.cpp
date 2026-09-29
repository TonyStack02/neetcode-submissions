// Queste direttive comunicano direttamente al compilatore (GCC) di LeetCode.
// "O3" attiva il livello massimo di ottimizzazione del codice.
// "unroll-loops" srotola i cicli (espande il codice del while/for) per risparmiare il tempo 
// perso dalla CPU per saltare da un'istruzione all'altra e valutare le condizioni.
#pragma GCC optimize("O3", "unroll-loops")

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // Disabilitiamo la sincronizzazione automatica tra l'input/output del linguaggio C 
        // e quello del C++. Su LeetCode, questo trucco taglia drasticamente i tempi 
        // di lettura dei dati di test e abbassa il runtime globale.
        ios_base::sync_with_stdio(false);
        
        // Svincoliamo il flusso di input (cin) da quello di output (cout).
        // Evita che il programma "pulisca" la memoria temporanea a ogni operazione, 
        // rendendo l'avvio molto più veloce.
        cin.tie(NULL);
        
        // Se l'array di input è vuoto, non c'è nessuna sequenza. Ritorniamo 0.
        if (nums.empty()) {
            return 0;
        }
        
        // unordered_set è l'equivalente C++ del set di Python (una Hash Table).
        // Usiamo nums.begin() e nums.end() per copiare in massa l'intero array 
        // direttamente in fase di costruzione, operazione molto più veloce 
        // rispetto a fare .insert() in un ciclo for manuale.
        unordered_set<int> nums_set(nums.begin(), nums.end());
        
        // Variabile per tenere traccia della lunghezza massima trovata.
        int longest = 0;
        
        // Iteriamo direttamente sull'hash set per garantire di processare
        // solo elementi unici, risparmiando cicli della CPU.
        for (int num : nums_set) {
            
            // Il metodo .find(valore) cerca l'elemento in tempo medio O(1).
            // Se l'elemento NON c'è, il metodo ritorna un puntatore speciale chiamato .end().
            // Qui controlliamo se (num - 1) manca: se manca, 'num' è l'inizio di una catena.
            if (nums_set.find(num - 1) == nums_set.end()) {
                
                // Impostiamo l'offset iniziale a 1.
                int length = 1;
                
                // Continuiamo a cercare il valore (num + length).
                // Finché .find() NON è uguale a .end(), significa che il numero consecutivo esiste.
                while (nums_set.find(num + length) != nums_set.end()) {
                    
                    // Incrementiamo la lunghezza trovata.
                    length++;
                }
                
                // Aggiorniamo il record. L'istruzione if nativa del C++ 
                // è più veloce rispetto a chiamare una funzione esterna come std::max.
                if (length > longest) {
                    longest = length;
                }
            }
        }
        
        // Al termine dei controlli, ritorniamo il risultato.
        return longest;
    }
};