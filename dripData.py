import sys, os, getopt, ConfigParser, time
import sqlite3 as lite
import dbaccess
#Reads in config file that determines when type of data to take and how often
def readConfig():
    pass
#This program should record data from the nextbus feed and store it in the supplied sqlite3 database
def main(argv):
    try:
        opts,args = getopt.getopt(argv,'h')
    except getopt.GetoptError:
        print 'dripData.py <database file>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'dripData.py <database file>'
            sys.exit()
        else:
            filename = args[0]
    config = ConfigParser.RawConfigParser()
    readConfig()
            
    print 'Storing data in '+filename
    con = lite.connect(filename)
    with con:
        table = 'predictions'
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXIST "+table+"(agency TEXT, route TEXT, stop TEXT, direction TEXT, qtime INT, epochTime INT, seconds INT, vehicle INT, tripTag INT, isDeparture TEXT, dirTag TEXT, minutes INT, block INT)")
        while True:
            time.sleep(10)
            try:
                preds = predictions.Prediction('actransit','18','0305120')
                cur.execute("PRAGMA table_info("+table+")")
                cols = cur.fetchall()
                dbaccess.writePredictions(cur,table,preds.getPredictionsDB(cols))
            except KeyboardInterupt:
                break
    print 'Done writing predictions to table: '+table+' in file: '+filename+'. Goodbye!'

    

if __name__ == '__main__':
    main(sys.argv[1:])
