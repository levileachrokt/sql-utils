from trino.auth import OAuth2Authentication
import pandas as pd
from trino.dbapi import connect
from sqlalchemy.engine import create_engine



"""
    This function creates a connection to the trino DB.
"""
def create_sql_connection():
    
    # an engine for querying the db
    print("Beginning SQL connection...")

    try:
        host = "trino-gateway-us-west-2.roktinternal.com"
        username = "levi.leach"
        catalog = "aws_legacy_datalake"
        engine = create_engine(f"trino://{username}@{host}:443/{catalog}?externalAuthentication=true")
        print("SQL connection successful")

    except Exception as e:
        print(f"Error connecting to SQL:{e}")
        return None

    return engine




"""
    This function runs a SQL query and returns a pandas dataframe.
    It uses the trino.dbapi to connect to the trino DB and the sqlalchemy engine to query the DB.
"""
def run_sql(query, conn=None):
    if conn is None:
        conn = create_sql_connection()

    try:
        df_query = pd.read_sql(query, con=conn)
        return df_query
    except Exception as e:
        if 'This result object does not return rows.' not in str(e):
            print(f"Error: {e}")

        return None
    


"""
    This function runs a SQL query and writes it to a specified csv file.
"""
def sql_to_csv(query, filename, conn=None):
    if conn is None:
        conn = create_sql_connection()

    df_sql = run_sql(query, conn=conn)
    df_sql.to_csv(filename, index=False)
    return df_sql





"""
    This function takes a pandas dataframe and writes it to a SQL table in chunks
"""
def df_to_sql_table(df, table_name, schema='analytics_ny', conn=None):
    if conn is None:
        conn = create_sql_connection()

    # drop the table to start
    print(f'Dropping table {schema}.{table_name}')
    run_sql(f'DROP TABLE IF EXISTS  {schema}.{table_name}', conn=conn)
    chunks = range(0, len(df), 1000)

    # split the data into chunks of 1000
    for i in chunks:
        start_index = i
        end_index = i + 1000
        
        print(f'Appending chunk {int(i / 1000) + 1} of {len(chunks)}; indexes {start_index} to {min(end_index - 1, len(df) - 1)}')
        df_chunk = df[start_index:end_index]
        df_chunk.to_sql(table_name, conn, schema=schema, if_exists='append', index=False, method='multi')




# Main function to run the script
if __name__ == '__main__':
    print('RunSQL.py')
