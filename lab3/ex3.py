'''
Spiegate brevemente come avete implementato la coda di priorità nell'algoritmo di Dijkstra per la ricerca dei cammini minimi.
Qual'è la complessità delle operazioni di base della vostra implementazione: creazione della coda, estrazione del minimo e decremento della chiave?


RISPOSTA

la coda di priorità è stata implementata tramite la struttora heapq fornita da python

la creazione della coda avviene con complessità O(n log n), poichè O(log n) è la complessità per l'operazione di push (si inserisce un nodo O(1) e si mantiene invariata la proprietà di heap O(log n), ed essa viene eseguita per inserire tutti gli n nodi
l'estrazione del minimo avviene con complessità O(log n), poichè O(log n) è la complessità per la funzione pop (si estrae il primo nodo O(1) e si mantiene invariata la proprietà di heap O(log n))


La coda di priorità Q è un min-heap e l'implementazione è stata resa grazie alla libreria heapq di python, la quale però non fornisce tutte le funzionalità 
necessarie.

Descrizione del min-heap:
    Lo heap è un albero binario di coppie (peso_arco,key_nodo) nelle quali il primo elemento della coppia è la chiave d'ordinamento del min-heap, ed essa corrisponde al peso
    dell'arco tra il nodo supersorgente e il nodo "key_nodo", che è il secondo elemento della coppia.

Creazione:
    la coda di priorità Q è inizialmente una lista vuota, nella quale vengono inseriti tutti i nodi con il metodo 'heapq.heappush(Q,(peso_arco,key_nodo))', il quale inserisce 
    nella coda Q la coppia (peso_arco,key_node), rispettando la proprietà del min-heap secondo la chiave 'peso_arco'. 
    la creazione della coda avviene con complessità O(n log n), poichè O(log n) è la complessità per l'operazione di push (si inserisce un nodo O(1) e si mantiene invariata 
    la proprietà di heap O(log n), ed essa viene eseguita per inserire tutti gli n nodi.

Estrazione:
    l'estrazione del minimo avviene con complessità O(log n), poichè O(log n) è la complessità per la funzione pop 
    (si estrae il primo nodo O(1) e si mantiene invariata la proprietà di heap O(log n)).

Decremento:
    Un vero decremento non esiste ed è qui che l'algoritmo implementato differisce da uno più tradizionale.
    Un algoritmo più tradizionale vorrebbe l'aggiornamento della chiave e poi il bubbleUp per mantenere rispettato l'invariante
    del min-heap. Nell'algoritmo implementato, invece, la chiave vecchia viene lasciata nello heap, mentre quella nuova viene inserita con heapq.heappush().
    Quest'ultimo metodo pare essere molto più veloce di un bubbleUp implementato a mano. 


'''
