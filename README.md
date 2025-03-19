# SQL Utils

A collection of utilities for working with SQL databases.

## Installation

```bash
pip install git+https://github.com/levileachrokt/sql-utils
```

Updating the installed repo:
```bash
pip install --upgrade --force-reinstall git+https://github.com/levileachrokt/sql-utils.git
```


## Getting Started

After installing, the function ```create_sql_connection()``` will return the connection object that you can pass into other functions. Every time this function is called, it will prompt a browser window to log in.


## Features

- Simplified database connections
- SQL query helpers
- Data transformation utilities
- Integration with pandas and SQLAlchemy

## Dependencies

- pandas
- sqlalchemy
- trino

## Usage

```python
from sql_utils import *

my_query_string = 'select count(*) from analytics_dbt.fct_transactions' # a query to run

conn = create_sql_connection() # creating the initial connection - will open a browser window to log in

df_query_output = run_sql(my_query_string) # get the output of my query in a pandas df 

df_to_sql_table(df_query_output, conn, 'my_table_name_to_create', schema='analytics_ny') # write to a table in chunks of 1000 rows

```

## License

This project is proprietary and owned by Rokt.

## Author

Levi Leach (levi.leach@rokt.com) 