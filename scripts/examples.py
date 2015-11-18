import urllib2

#Some examples of data that can be grabbed from NextBusXMLFeed
def main():
    agencyList = urllib2.urlopen('http://webservices.nextbus.com/service/publicXMLFeed?command=agencyList')
    for lines in agencyList:
        print lines

    routeList = urllib2.urlopen('http://webservices.nextbus.com/service/publicXMLFeed?command=routelist&a=actransit')
    for lines in routeList:
        print lines

    routeConfig = urllib2.urlopen('http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=actransit&r=18')
    for lines in routeConfig:
        print lines

    stop = urllib2.urlopen('http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=actransit&r=18&s=0305120&')
    for lines in stop:
        print lines

#Main
if __name__ == '__main__':
    main()
