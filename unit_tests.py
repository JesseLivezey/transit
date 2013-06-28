import predictions
import sqlite3 as lite
import dbaccess
#Units tests for transit-stats
def main():
    table = 'predictions'
    predict = predictions.Prediction('actransit','18','0305120')
    for item in predict.getPredictionsDict():
        pass
        #print item
    
    con = lite.connect('test.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS "+table)
        cur.execute("CREATE TABLE "+table+"(agency TEXT, route TEXT, stop TEXT, direction TEXT, qtime INT, epochTime INT, seconds INT, vehicle INT, tripTag INT, isDeparture TEXT, dirTag TEXT, minutes INT, block INT)")
        preds = predictions.Prediction('actransit','18','0305120')
        cur.execute("PRAGMA table_info("+table+")")
        cols = cur.fetchall()
        dbaccess.writePredictions(cur,table,preds.getPredictionsDB(cols))

    con = lite.connect('test.db')
    with con:
        cur = con.cursor()
        dbaccess.readAll(cur,table)
        rows = cur.fetchall()
        for row in rows:
            print row
            
        cur.execute("DROP TABLE IF EXISTS "+table)
if __name__ == '__main__':
    main()
