#write prediction type data to table
def writePredictions(cursor,table,(agency,route,stop,direction,time,predictions)):
    for prediction in predictions:
        valuesTuple = (agency,route,stop,direction,time,)+tuple(prediction)
        cursor.execute("INSERT INTO "+table+"(agency, route, stop, direction, qtime, epochTime, seconds, vehicle, tripTag, isDeparture, dirTag, minutes, block) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",valuesTuple)

def readAll(cursor,table):
        return cursor.execute("SELECT * FROM "+table)
    
