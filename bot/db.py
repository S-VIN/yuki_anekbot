import psycopg2
import psycopg2.extras

POSTGRES_DSN = 'dbname=yuki_anekbot user=stepan-vinokurov password=stepan-vinokurov host=db port=5432'


class Database:
    def __init__(self, dsn):
        self.dsn = dsn
        self.conn = psycopg2.connect(dsn)


    def add_anek_sync(self, joke_text):
        with self.conn.cursor() as cur:
            cur.execute('INSERT INTO aneks (anek) VALUES (%s)', (joke_text,))
        self.conn.commit()


    def get_random_anek_sync(self):
        with self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute('SELECT id, anek FROM aneks ORDER BY RANDOM() LIMIT 1')
            row = cur.fetchone()
            return dict(row) if row else None

db = Database(POSTGRES_DSN)