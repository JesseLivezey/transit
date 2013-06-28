import urllib2
import xml.etree.ElementTree as ET
import time
#Class for fetching and storing prediction data
class Prediction(object):
    def __init__(self,agency,route,stop):
        self.predictionList = []
        self.rawPrediction = urllib2.urlopen('http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a='+agency+'&r='+route+'&s='+stop)
        self.agency = agency
        self.route = route
        self.stop = stop
        self.time = int(round(time.time()*1000))

        self.tree = ET.parse(self.rawPrediction)
        self.root = self.tree.getroot() 

        for self.child in self.root:
            for self.child2 in self.child:
                if self.child2.tag == 'direction':
                    self.direction = self.child2.attrib['title']
                for self.child3 in self.child2:
                    #Use ast.literal_eval to convert string to dict
                    self.predictionList.append(self.child3.attrib)

    def getPredictionsDict(self):
        return self.predictionList

    def getPredictionsDB(self,cols):
        #Break prediction into list of list of parts in DB format
        self.predictionsDB = [[self.pred[self.col[1]] for self.col in cols if self.col[1] in self.pred] for self.pred in self.predictionList]
        return (self.agency,self.route,self.stop,self.direction,self.time,self.predictionsDB)
