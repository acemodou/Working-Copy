import json 
import requests
source = 'https://api.github.com/events'

#Download the data 
def downloadJsonData(url):
    response = requests.get(url)
    response.raise_for_status()
    return response
    
#Read the data 
def readJsonData(source):
    respond = downloadJsonData(source)
    # print(respond.content)
    data = json.loads(respond.content)
    return data
    
#modify the data
def modifyJsonData(data):
    new_json = readJsonData(data)
    with open(str(new_json), 'r') as f:
        data = json.load(f)
   
def modifyStatesData():
    states_name_withA = list()
    
    with open('states.json') as f:
        data = json.load(f)
    
    for state in data['states']:
        del state['area_codes']
    
    return data

def statesWithoutAreaCode():
    data = modifyStatesData()
    with open('new_states.json', 'w') as file:
        json.dump(data, file, indent=2)

                

#write it back to another json file 

if __name__=="__main__":
    #modifyJsonData(source)
    statesWithoutAreaCode()
