#write prediction type data to table
def writePredictions(cursor,table,(agency,route,stop,direction,time,predictions)):
    for prediction in predictions:
        cursor.execute("INSERT INTO "+table+" VALUES("+agency+","+route+","+stop+","+direction+","+str(time)+","+prediction+")")

    def readAll(cursor,table):
        return cursor.execute("SELECT * FROM "+table)
    
