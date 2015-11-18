import os
import sqlite3 as lite


class TransitDB(object):
    """
    Database class that wraps sqlite and provides interface for storing
    transit data.

    Parameters
    ----------
    db_file : str
        Path to db file. If the file doesn't exist, it will be created.
    """
    def __init__(self, db_file):
        self.db_file = db_file

    def __enter__(self):
        """
        Open DB connection and create predictions table.
        """
        self.conn = lite.connect(self.db_file)
        with self.conn:
            self.conn.execute("CREATE TABLE IF NOT EXISTS " +
                              self.table_name + "(agency TEXT, route TEXT, " +
                              "stop TEXT, direction TEXT, qtime INT, " +
                              "epochTime INT, seconds INT, vehicle INT, " +
                              "tripTag INT, isDeparture TEXT, dirTag TEXT, " +
                              "minutes INT, block INT)")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Closes DB connection.
        """
        self.conn.close()


    def read_all(self, table=None):
        """
        Read all data from table.

        Parameters
        ----------
        table : str
            Table to read data from (default: self.table).
        """
        if table is None:
            table = self.table_name
        return self.conn.execute("SELECT * FROM " + table)

class PredictionDB(TransitDB):
    """
    Database class that wraps sqlite and provides interface for storing
    transit predictions.

    Parameters
    ----------
    db_file : str
        Path to db file. If the file doesn't exist, it will be created.
    table : str
        Table to write prediction into (default: self.table).
    """
    def __init__(self, db_file, table_name=None):
        super(PredictionDB, self).__init__(db_file)
        self.table_name = table_name or 'predictions'

    def write_predictions(self, predictions, table=None):
        """
        Write one set of predictions into the DB.

        Parameters
        ----------
        predictions : tuple
            (predictions, prediction info)
        table : str
            Table to write prediction into (default: self.table).
        """
        predictions, info = predictions
        if table is None:
            table = self.table_name
        agency, route, stop, direction, time = info
        values_tuple = [(agency, route, stop, direction, time) + tuple(prediction)
                        for prediction in predictions]
        with self.conn:
            self.conn.executemany("INSERT INTO " + table +
                                  "(agency, route, stop, direction, qtime, epochTime, " +
                                  "seconds, vehicle, tripTag, isDeparture, dirTag, " +
                                  "minutes, block) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, " +
                                  "?, ?, ?, ?)", valuesTuple)
