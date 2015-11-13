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
    overwrite : bool
        Whether to overwrite an existing file or add to it (default False).
    """
    def __init__(self, db_file):
        self.db_file = db_file
        self.setup_db()
        self.connection = lite.connect(self.db_file)
        self.cursor = self.connection.cursor()
        self.table_name = 'predictions'
        self.cursor.execute("CREATE TABLE IF NOT EXIST " +
                           self.table_name + "(agency TEXT, route TEXT, " +
                           "stop TEXT, direction TEXT, qtime INT, " +
                           "epochTime INT, seconds INT, vehicle INT, " +
                           "tripTag INT, isDeparture TEXT, dirTag TEXT, " +
                           "minutes INT, block INT)")

    def write_predictions(self, predictions, table=None):
        predictions, info = predictions
        if table is None:
            table = self.table_name
        agency, route, stop, direction, time = info
        for prediction in predictions:
            values_tuple = (agency, route, stop, direction, time) + tuple(prediction)
            cursor.execute("INSERT INTO " +
                           table +
                           "(agency, route, stop, direction, qtime, epochTime, " +
                           "seconds, vehicle, tripTag, isDeparture, dirTag, " +
                           "minutes, block) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, " +
                           "?, ?, ?, ?)", valuesTuple)

    def read_all(self, table=None):
        """
        Read all data from table.
        """
        if table is None:
            table = self.table_name
            return self.cursor.execute("SELECT * FROM " + table)
        
