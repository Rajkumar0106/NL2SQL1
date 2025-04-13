import psycopg2
import pandas as pd
from config import REDSHIFT_CONFIG

class RedshiftConnection:
    def __init__(self):
        self.conn = None
        
    def connect(self):
        try:
            self.conn = psycopg2.connect(**REDSHIFT_CONFIG)
            return True
        except Exception as e:
            print(f"Error connecting to Redshift: {e}")
            return False
            
    def execute_query(self, query):
        try:
            with self.conn.cursor() as cur:
                cur.execute(query)
                columns = [desc[0] for desc in cur.description]
                data = cur.fetchall()
                return pd.DataFrame(data, columns=columns)
        except Exception as e:
            print(f"Error executing query: {e}")
            return None