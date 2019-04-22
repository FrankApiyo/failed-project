import psycopg2
from config import config
 
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params)
 

        cur = connection.cursor()

        # sql = "CREATE DATABASE IF NOT EXISTS crimemap"
        # cur.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS crimes (
                id int NOT NULL,
                latitude FLOAT,
                longitude FLOAT,
                date DATE,
                category VARCHAR(50),
                description VARCHAR(1000),
                updated_at TIMESTAMP,
                PRIMARY KEY (id)
            )"""
        cur.execute(sql);
        connection.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
        print('Database connection closed.')
            
 
if __name__ == '__main__':
    connect()