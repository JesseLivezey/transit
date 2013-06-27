import predictions
import sqlite3 as lite
import dbaccess
#Units tests for transit-stats
def main():
    table = 'predictions'
    predict = predictions.Prediction('actransit','18','0305120')
    for item in predict.getPredictions():
        print item
    
    con = lite.connect('test.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS "+table)
        cur.execute("CREATE TABLE "+table+"(agency TEXT, route TEXT, stop TEXT, direction TEXT, time INT, prediction TEXT)")
        preds = predictions.Prediction('actransit','18','0305120')
        dbaccess.writePredictions(cur,table,preds.getPredictionsDB())

    con = lite.connect('test.db')
    with con:
        cur = con.cursor()
        readAll(cur,table)
        rows = cur.fetchall()
        for row in rows:
            print row
        cur.execute("DROP TABLE IF EXISTS "+table)
if __name__ == '__main__':
    main()
