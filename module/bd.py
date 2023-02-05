import psycopg2
from psycopg2 import Error
import config as cf


def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(user=cf.user,
                                      password=cf.password,
                                      host=cf.host,
                                      port=cf.port,
                                      database=cf.database)
        print("Connection to PostgreSQL DB successful")
    except (Exception, Error) as error:
        print("Error connect to PostgreSQL", error)
    return connection
