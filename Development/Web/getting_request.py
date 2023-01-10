import urllib.request
import json 

def printResults(data):
    theJSON = json.loads(data)

    # now we can access the contents of the JSON: Let's get the title 
    if 'title' in theJSON['metadata']:
        print(theJSON['metadata']['title'])
    
    # Output the number of events, plus the magnitude and each event name
    count = theJSON['metadata']['count']
    print(str(count) + " events recorded")

    # for each event, print the place where it occured
    for i in theJSON['features']:
        print(i['properties']['place'])
    print("-----------------\n")

    #print the events that only have a magnitutde greater than 4.0
    for i in theJSON['features']:
        if i['properties']['mag'] > 4.0:
            print("%2.1f" %i['properties']['mag'], i['properties']['place'] )
    print("-----------------\n")

    #print the events where at least 1 person reported feeling something
    print("Events that were felt:")
    for i in theJSON['features']:
        feltReports = i['properties']['felt']
        if feltReports !=None:
            if feltReports > 0:
                print("%2.f" %i['properties']['mag'],i['properties']['place'], " reported " + str(feltReports) + " times" )


def main():
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    #Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))
    if webUrl.getcode() == 200:
        data = webUrl.read()
        printResults(data)
    else:
        print("Received error, cannot parse result")


if __name__ == "__main__":
    main()
