import sqlite3
import pandas as pd 

class DBStorage(): 
    def __init__(self): 
        self.con = sqlite3.connect("links.db")
        self.setup_tables()

    def setup_tables(self): 
        cur = self.con.cursor()
        results_table = r"""
            CREATE TABLE IF NOT EXISTS results(
                id INTEGER PRIMARY KEY, 
                query TEXT, 
                rank INTEGER, 
                link TEXT, 
                title TEXT, 
                snippet TEXT, 
                html TEXT, 
                created DATETIME,
                relevance INTEGER, 
                UNIQUE(query, link)
            ); 
        """ 
        cur.execute(results_table)
        self.con.commit()
        cur.close()

    def query_results(self, query): 
        df = pd.read_sql(f"SELECT * FROM results WHERE query='{query}' ORDER BY rank ASC;", self.con)
        return df
    
    def insert_row(self, values): 
        cur = self.con.cursor()
        try: 
            cur.execute('INSERT INTO results (query, rank, link, title, snippet, html, created) VALUES(?,?,?,?,?,?,?)', values)
            self.con.commit()
        except sqlite3.IntegrityError: 
            pass 
        cur.close()

    def update_relevance(self, query, link, relevance):
        cur = self.con.cursor()
        try:
            cur.execute('''
                UPDATE results 
                SET relevance = ? 
                WHERE query = ? AND link = ?
            ''', (relevance, query, link))
            self.con.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            cur.close()

    def mark_relevant(self, query, link, relevance_score):
        cur = self.con.cursor()
        try:
            cur.execute('''
                UPDATE results 
                SET relevance = ?
                WHERE query = ? AND link = ?
            ''', (relevance_score, query, link))
            self.con.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            cur.close()

    def get_relevance_data(self):
        query = '''
            SELECT query, link, title, snippet, relevance
            FROM results
            WHERE relevance IS NOT NULL
        '''
        return pd.read_sql(query, self.con)