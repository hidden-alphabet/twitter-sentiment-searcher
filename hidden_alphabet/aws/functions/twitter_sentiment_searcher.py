import datetime
import psycopg2
import json
import os

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.date):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

def handler(event, context):
    db = psycopg2.connect(
        host=os.environ['PG_HOST'],
        port=os.environ['PG_PORT'],
        dbname=os.environ['PG_DBNAME'],
        user=os.environ['PG_USERNAME'],
        password=os.environ['PG_PASSWORD']
    )

    data = json.loads(event['body'])
    start = data['start']
    end = data['end']

    with db.cursor() as cursor:
        date_query = """
            SELECT * FROM twitter
            WHERE tweet_time
            BETWEEN date '{}'
            AND date '{}';
        """.format(start, end)

        cursor.execute(date_query)
        rows = cursor.fetchall()

        cursor.execute(""" SELECT * FROM twitter LIMIT 0 """)
        names = [desc[0] for desc in cursor.description]

        timeseries = [dict(zip(names, row)) for row in rows]

    return {
        'statusCode': 200,
        'body': json.dumps(timeseries, cls=DatetimeEncoder)
    }