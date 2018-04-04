'''
Spiegate brevemente come avete implementato la coda di priorità nell'algoritmo di Dijkstra per la ricerca dei cammini minimi.
Qual'è la complessità delle operazioni di base della vostra implementazione: creazione della coda, estrazione del minimo e decremento della chiave?


RISPOSTA

la coda di priorità è stata implementata tramite la struttora heapq fornita da python

la creazione della coda avviene con complessità O(n log n), poichè O(log n) è la complessità per l'operazione di push (si inserisce un nodo O(1) e si mantiene invariata la proprietà di heap O(log n), ed essa viene eseguita per inserire tutti gli n nodi
l'estrazione del minimo avviene con complessità O(log n), poichè O(log n) è la complessità per la funzione pop (si estrae il primo nodo O(1) e si mantiene invariata la proprietà di heap O(log n))
il decremento della chiave avviene con complessità O(log n), poichè è la complessità dell'operazione di push con cui è stato implementato il decremento
'''
