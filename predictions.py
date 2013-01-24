import urllib2
import xml.etree.ElementTree as ET
#Class for fetching and storing prediction data
class Prediction(object):
    def __init__(self):
        pass

    def fetch_Prediction(self,agency,route,stop):
        self.predictionList = []
        self.rawPrediction = urllib2.urlopen('http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a='+agency+'&r='+route+'&s='+stop)
        
        self.tree = ET.parse(self.rawPrediction)
        self.root = self.tree.getroot() 

        print self.root.tag
           
        for self.child in self.root:
            for self.child2 in self.child:
                for self.child3 in self.child2:
                    self.predictionList.append(self.child3.tag+str(self.child3.attrib))
                   
    def get_Prediction(self):
        return self.predictionList
