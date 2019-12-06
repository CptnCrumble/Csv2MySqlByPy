import pandas
import sqlalchemy
import pymysql
from sqlalchemy import create_engine

# Fill in these strings
path_to_csv = ''
database_username = ''
database_password = ''
database_ip       = ''
database_name     = ''
table_name = ''

# Now save the file and run it in your terminal of choice.

df = pandas.read_csv(path_to_csv)
print(df.head())
print("Number of rows in csv = "+str(len(df.index)))

database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name), pool_recycle=1, pool_timeout=57600).connect()

df.to_sql(con=database_connection, name=table_name, if_exists='append',chunksize=100,index=False)

db_row_count = pandas.read_sql_query('SELECT COUNT(*) FROM {0}.{1}'.format(database_name,table_name),con=database_connection)
print("Row count from database:")
print(db_row_count)

database_connection.close() 


