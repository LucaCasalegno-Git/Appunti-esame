class DAO:

 #(1)-----------------------------------------------------------------------#
    @staticmethod
    def esempio():
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        query = """  """

        cursor.execute(query, (   ,))

        for row in cursor:
            result.append(Obj(row['']))

        cursor.close()
        conn.close()
        return result

 #(2)-----------------------------------------------------------------------#
 # Costruisce una mappa oggetto → insieme di collegamenti.
 # Interroga una relazione molti-a-molti (tabella ponte).
 # Per ogni entità principale raccoglie tutte le entità collegate.
 # Usa un set per eliminare duplicati dovuti a più righe SQL.
 # Serve a ricostruire in Python una relazione del database.
 @staticmethod
    def get_album_playlist_map(albums):
        """Restituisce un dizionario: album -> set di playlist_id in cui appaiono le sue canzoni"""
        conn = DBConnect.get_connection()
        result = {a: set() for a in albums}
        album_ids = tuple(a.id for a in albums)
        if not album_ids:
            return result

        cursor = conn.cursor(dictionary=True)
        query = f"""
                           SELECT t.album_id, pt.playlist_id
                           FROM track t, playlist_track pt
                           WHERE t.id = pt.track_id and t.album_id IN {album_ids}
                       """
        cursor.execute(query)
        for row in cursor:
            album = next((a for a in albums if a.id == row['album_id']), None)
            if album:
                result[album].add(row['playlist_id'])
        cursor.close()
        conn.close()
        return result

