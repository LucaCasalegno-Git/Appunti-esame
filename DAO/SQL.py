#QUERY UTILI#

#Estrae coppie ordinate di entità distinte, collegate da una relazione registrata
# in una tabella di interazioni, filtrando solo quelle associate a gruppi diversi
# e validi, e restituisce per ciascuna coppia un valore numerico rappresentativo
# della loro relazione, eliminando i duplicati tramite raggruppamento.
"""SELECT g1.id AS gene1, g2.id AS gene2, i.correlazione
                FROM gene g1, gene g2, interazione i
                WHERE  g1.id = i.id_gene1 and g2.id = i.id_gene2
                       and g2.cromosoma != g1.cromosoma
                       and g2.cromosoma>0
                       and g1.cromosoma>0
                GROUP BY g1.id, g2.id """


#Estrae gli elementi principali (con i loro attributi identificativi) collegati
# a più record di dettaglio, calcola un valore aggregato su tali record
# (in questo caso una durata totale), raggruppa per elemento, e restituisce solo
# quelli che superano una soglia specificata.
"""SELECT a.id, a.title, a.artist_id, SUM(t.milliseconds)/60000 AS duration
                FROM album a, track t
                WHERE a.id = t.album_id
                GROUP BY a.id, a.title, a.artist_id
                HAVING duration > %s"""

#Estrae le associazioni tra elementi principali e contenitori, selezionando per
# ciascun elemento il contenitore a cui appartiene, limitando il risultato solo
# a un insieme specifico di elementi fornito come input.
f"""
    SELECT t.album_id, pt.playlist_id
    FROM track t, playlist_track pt
    WHERE t.id = pt.track_id and t.album_id IN {album_ids}
"""


#Estrae tutti i record di una tabella e li restituisce ordinati cronologicamente
# in base a un campo data/ora crescente.
""" SELECT * 
    FROM sighting
    ORDER BY s_datetime ASC """


#Estrae i valori distinti di un attributo, scartando quelli vuoti, limitandoli ai
# record che soddisfano una condizione temporale (appartenenza a uno specifico anno).
""" SELECT DISTINCT shape 
                    FROM sighting 
                    WHERE shape <> "" AND YEAR(s_datetime) = %s """


#Estrae coppie non ordinate di entità collegate tra loro, normalizzandone l’ordine
# per evitare duplicati, e conta quante volte ciascuna coppia compare tra i record
# che soddisfano specifiche condizioni di filtro (temporali e su attributi),
# restituendo una frequenza per ogni coppia.
""" SELECT LEAST(n.state1, n.state2) AS st1,
           GREATEST(n.state1, n.state2) AS st2, 
           COUNT(*) as N
    FROM sighting s , neighbor n 
    WHERE year(s.s_datetime) = %s
          AND s.shape = %s
          AND (s.state = n.state1 OR s.state = n.state2)
    GROUP BY st1 , st2 """

#Calcola quante volte ogni elemento compare in un certo periodo e in una certa
# categoria, poi forma coppie di elementi diversi, assegna a ciascuna coppia un peso
# dato dalla somma delle loro occorrenze, mantiene solo le coppie che rispettano una
# condizione sui conteggi e restituisce il risultato ordinato per peso.
""" SELECT t1.id AS n1, t2.id AS n2, t1.num+t2.num AS peso
    FROM (SELECT p.id , count(*) AS num
          FROM product p, order_item oi, `order` o 
          WHERE p.id = oi.product_id AND oi.order_id = o.id 
                AND o.order_date BETWEEN %s AND %s
                AND p.category_id = %s
                GROUP BY (p.id)
                ORDER BY p.id ) t1, 
         (SELECT p.id , count(*) AS num
          FROM product p, order_item oi, `order` o 
          WHERE p.id = oi.product_id AND oi.order_id = o.id 
                AND o.order_date BETWEEN %s AND %s
                AND p.category_id = %s
          GROUP BY (p.id)
          ORDER BY p.id ) t2
   WHERE t1.num >= t2.num
         AND t1.id <> t2.id
   ORDER BY peso DESC, n1 ASC, n2 ASC """


#Estrae coppie di elementi diversi che compaiono insieme nello stesso contesto,
# conta quante volte ogni coppia appare insieme, e restituisce per ciascuna coppia
# un peso che rappresenta la frequenza della loro co-occorrenza, evitando duplicati
# grazie all’ordinamento sugli identificativi.
""" SELECT eo1.object_id AS o1, eo2.object_id AS o2, COUNT(*) AS peso
    FROM exhibition_objects eo1, exhibition_objects eo2 
    WHERE eo1.exhibition_id = eo2.exhibition_id 
    AND eo1.object_id < eo2.object_id 
    GROUP BY eo1.object_id, eo2.object_id"""

#Calcola quante volte ogni elemento è coinvolto in una relazione considerando
# più ruoli possibili, somma tali occorrenze su tutti i sottogruppi, e restituisce
# solo gli elementi che raggiungono o superano una soglia minima di frequenza.
"""SELECT tmp.id, tmp.IATA_CODE, count(*) as somma
    FROM
    (SELECT a.id, a.IATA_CODE, f.AIRLINE_ID, COUNT(*)   
    FROM flights f, airports a
    WHERE a.id = f.ORIGIN_AIRPORT_ID OR
          a.id = f.DESTINATION_AIRPORT_ID 
    GROUP BY a.id, a.IATA_CODE, f.AIRLINE_ID) AS tmp
    GROUP BY tmp.id, tmp.IATA_CODE 
    HAVING somma>= %s """


#Calcola il numero totale di relazioni bidirezionali tra coppie di elementi,
# sommando le occorrenze nei due versi (A→B e B→A), evitando i duplicati e mantenendo
# anche i casi in cui la relazione esiste in un solo verso.
"""SELECT t1.ORIGIN_AIRPORT_ID, t1.DESTINATION_AIRPORT_ID, COALESCE(t1.n, 0) + coalesce(t2.n, 0) as voli
    from 
    (SELECT f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID , count(*) as n FROM flights f 
    group by f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID
    order by f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID ) t1
    left join 
    (SELECT f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID , count(*) as n FROM flights f 
    group by f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID
    order by f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID ) t2
    on t1.ORIGIN_AIRPORT_ID = t2.DESTINATION_AIRPORT_ID and t1.DESTINATION_AIRPORT_ID = t2.ORIGIN_AIRPORT_ID
    where t1.ORIGIN_AIRPORT_ID < t1.DESTINATION_AIRPORT_ID or t2.ORIGIN_AIRPORT_ID is null"""


#La query costruisce gli archi di un grafo orientato tra cromosomi sommando le correlazioni delle interazioni tra geni
# appartenenti a cromosomi diversi, dopo aver eliminato sia i duplicati delle coppie di geni sia le duplicazioni dovute
# a più occorrenze dello stesso gene.
'''SELECT
    g1.cromosoma AS cromosoma1,
    g2.cromosoma AS cromosoma2,
    SUM(t.correlazione) AS peso
FROM (
    -- 1) dedup coppie di geni: una sola volta per (id_gene1, id_gene2)
    SELECT
        id_gene1,
        id_gene2,
        MAX(correlazione) AS correlazione
    FROM interazione
    GROUP BY id_gene1, id_gene2) t
JOIN (
    -- 2) dedup gene -> cromosoma: una sola riga per id
    SELECT DISTINCT id, cromosoma
    FROM gene
    WHERE cromosoma <> 0) g1 ON g1.id = t.id_gene1
JOIN (
    SELECT DISTINCT id, cromosoma
    FROM gene
    WHERE cromosoma <> 0) g2 ON g2.id = t.id_gene2
WHERE g1.cromosoma <> g2.cromosoma
GROUP BY g1.cromosoma, g2.cromosoma
ORDER BY peso desc'''
