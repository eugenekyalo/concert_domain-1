import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class Venue:
    def __init__(self, venue_id):
        self.venue_id = venue_id

    def concerts(self):
        query = "SELECT * FROM concerts WHERE venue_id = %s"
        return self._execute_query(query, (self.venue_id,))

    def bands(self):
        query = """
        SELECT DISTINCT bands.* FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        WHERE concerts.venue_id = %s
        """
        return self._execute_query(query, (self.venue_id,))

    def concert_on(self, date):
        query = "SELECT * FROM concerts WHERE venue_id = %s AND date = %s ORDER BY date LIMIT 1"
        return self._execute_query(query, (self.venue_id, date))

    def most_frequent_band(self):
        query = """
        SELECT bands.*, COUNT(concerts.id) as performance_count
        FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        WHERE concerts.venue_id = %s
        GROUP BY bands.id
        ORDER BY performance_count DESC LIMIT 1
        """
        return self._execute_query(query, (self.venue_id,))

    def _execute_query(self, query, params):
        try:
            conn = psycopg2.connect(
                dbname=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                host=os.getenv('DB_HOST')
            )
            with conn.cursor() as cur:
                cur.execute(query, params)
                if query.strip().startswith("SELECT"):
                    result = cur.fetchall()
                else:
                    conn.commit()
                    result = None
            conn.close()
            return result
        except Exception as e:
            print("Error:", e)
            return None
