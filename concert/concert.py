import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class Concert:
    def __init__(self, concert_id):
        self.concert_id = concert_id

    def band(self):
        query = """
        SELECT bands.* FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        WHERE concerts.id = %s
        """
        return self._execute_query(query, (self.concert_id,))

    def venue(self):
        query = """
        SELECT venues.* FROM venues
        JOIN concerts ON venues.id = concerts.venue_id
        WHERE concerts.id = %s
        """
        return self._execute_query(query, (self.concert_id,))

    def hometown_show(self):
        query = """
        SELECT bands.hometown, venues.city
        FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = %s
        """
        result = self._execute_query(query, (self.concert_id,))
        return result[0] == result[1]

    def introduction(self):
        query = """
        SELECT bands.name, bands.hometown, venues.city
        FROM bands
        JOIN concerts ON bands.id = concerts.band_id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = %s
        """
        result = self._execute_query(query, (self.concert_id,))
        return f"Hello {result[2]}!!!!! We are {result[0]} and we're from {result[1]}!"

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
                result = cur.fetchone()
            conn.close()
            return result
        except Exception as e:
            print
