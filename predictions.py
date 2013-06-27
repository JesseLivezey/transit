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
        self.time = int(round(time.time()))

        self.tree = ET.parse(self.rawPrediction)
        self.root = self.tree.getroot() 

        for self.child in self.root:
            for self.child2 in self.child:
                if self.child2.tag == 'direction':
                    self.direction = str(self.child2.attrib)
                for self.child3 in self.child2:
                    #Use ast.literal_eval to convert string to dict
                    self.predictionList.append(self.child3.attrib)

    def getPredictions(self):
        return self.predictionList

    def getPredictionsDB(self):
        #break prediction into list of list of parts
        return (self.agency,self.route,self.stop,self.direction,self.time,self.predictionList)
