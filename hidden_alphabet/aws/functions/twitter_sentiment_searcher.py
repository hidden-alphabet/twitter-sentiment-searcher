import datetime
from dotenv import load_dotenv
import psycopg2
import json
import os

load_dotenv()

def search(start, end):
    """
      :start: Start Time String
      :end: End Time String
    """
    db = psycopg2.connect(
        host=os.environ['PG_HOST'],
        port=os.environ['PG_PORT'],
        dbname=os.environ['PG_DBNAME'],
        user=os.environ['PG_USERNAME'],
        password=os.environ['PG_PASSWORD']
    )
    cursor = db.cursor()
    date_query = """
        SELECT * FROM twitter
        WHERE tweet_time
        BETWEEN date '{}'
        AND date '{}';
    """.format(start,end)
    cursor.execute(date_query)
    # Creates list of tuples
    rows = cursor.fetchall()
    col_names_query = """
        SELECT * FROM twitter
        LIMIT 0
    """
    cursor.execute(col_names_query)
    # Get column names in twitter table
    names = [desc[0] for desc in cursor.description]

    def make_dictionary(rows, columns):
        """
          :rows: list of tuples
          :columns: list of strings
        """
        p = []
        for row in rows:
            for column in columns:
            # dictionary.setdefault(column, row).append(dic)
            p.append(dictionary)

    print(names)

    cursor.close()

    # return json.dumps()

search("2019-06-15","2019-06-16")