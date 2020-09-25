import pandas as pd


class DbConnector(object):


    def __init__(self):
        import sqlite3
        self.conn = sqlite3.connect('data/northWind.sqlite')
        self.cur = self.conn.cursor()


    def close(self):
        """Closes the cursor and connection created by instantiating a DbConnector object."""
        self.cur.close()
        self.conn.close()


    def list_tables(self):
        """Queries the database and returns a list of table names."""
        query = """
            SELECT name 
            FROM sqlite_master
            WHERE type='table';
        """
        response = self.cur.execute(query).fetchall()
        table_names = [r[0] for r in response]
        return table_names


    def list_column_names(self, table_name):
        """Given the name of a table in the database, this function returns a list of column names.

        Keyword Arguments:
        table_name -- name of the table whose columns will be listed.

        Use list_tables method to obtain a list of tables.
        """
        query = f"""
            PRAGMA table_info('{table_name}');
            """
        response = self.cur.execute(query).fetchall()
        column_names = [r[1] for r in response]
        return column_names


    def load_query_as_df(self, query):
        """Given a valid SQL query formatted as a string, this function returns the output of the query as a pandas dataframe.

        Keyword Arguments:
        query -- SQL query formatted as a string.
        """
        df = pd.read_sql(query, self.conn)
        return df


    def load_table_as_df(self, table_name):
        """Given the name of a table in the database, 
        this function loads the table as as pandas dataframe.

        Keyword Arguments:
        table_name -- name of tables whose contents will be returned as a dataframe

        Use the list_tables method to obtain a list of tables.
        """
        query = f"""
            SELECT *
            FROM {table_name};
            """
        df = self.load_query_as_df(query)
        return df
