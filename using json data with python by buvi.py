import urllib.request
import json


# json modleue to load string  data in to dictoionary
def printResults(data):

    theJSON = json.loads(data)
    # fetching the data from the json with python

    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    count = theJSON["metadata"]["count"]
    print(str(count) + " events recorded")



def main():

    # we use the free data feed from usgs
    # in this the earthquakes larger than mag 4.5 for the last day
    urlData= "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"

    #open url & read the data
    
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("recived, cannot parse results")


if __name__=='__main__':
    main()