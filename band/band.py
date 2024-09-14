import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class Band:
    def __init__(self, band_id):
        self.band_id = band_id

    def concerts(self):
        query = "SELECT * FROM concerts WHERE band_id = %s"
        return self._execute_query(query, (self.band_id,))

    def venues(self):
        query = """
        SELECT DISTINCT venues.* FROM venues
        JOIN concerts ON venues.id = concerts.venue_id
        WHERE concerts.band_id = %s
        """
        return self._execute_query(query, (self.band_id,))

    def play_in_venue(self, venue_title, date):
        query = """
        INSERT INTO concerts (band_id, venue_id, date)
        SELECT %s, venues.id, %s
        FROM venues WHERE venues.title = %s
        """
        return self._execute_query(query, (self.band_id, date, venue_title))

    def all_introductions(self):
        query = """
        SELECT venues.city, bands.name, bands.hometown
        FROM concerts
        JOIN venues ON concerts.venue_id = venues.id
        JOIN bands ON concerts.band_id = bands.id
        WHERE concerts.band_id = %s
        """
        results = self._execute_query(query, (self.band_id,))
        introductions = [f"Hello {r[0]}!!!!! We are {r[1]} and we're from {r[2]}!" for r in results]
        return introductions

    def most_performances(self):
        query = """
        SELECT bands.*, COUNT(concerts.id) as performance_count
        FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        GROUP BY bands.id
        ORDER BY performance_count DESC LIMIT 1
        """
        return self._execute_query(query, ())

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
