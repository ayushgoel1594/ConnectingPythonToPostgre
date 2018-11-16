from configparser import ConfigParser
 
 
def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    print(parser.read(filename))

    print(parser.has_section(section))
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        print(params)
        for param in params:
            #print(param)
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db

import psycopg2
from . import config
 
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        print("inside connect:", params)
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')

        # conn = psycopg2.connect(database="postgres",  user=self.user,password=self.passwd)
        #below is dictionary equivalent of doing what is done above
        #above statement is another way of connecting
        #whwn we write **dict for dictionary its argument is taken as positional arguments for the function
        conn = psycopg2.connect(**params)
        # create a cursor
        cur = conn.cursor()
        
 # execute a statement
        print('PostgreSQL database version:')
        # cur.execute('SELECT version()')
        cur.execute('SELECT * from public.practice')

        #if we want to fetch only one row
        #executedQueryResult= cur.fetchone()
        executedQueryResult= cur.fetchall()
        print(executedQueryResult)
       
     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
connect()