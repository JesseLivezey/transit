import sys, os, getopt, ConfigParser
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
        cur = con.cursor()
        cur.execute("CREATE TABLE StopPred(agency TEXT, route TEXT, stop TEXT, direction TEXT, time INT, prediction TEXT)")
        prediction = predictions.Prediction('actransit','18','0305120')

    

if __name__ == '__main__':
    main(sys.argv[1:])
