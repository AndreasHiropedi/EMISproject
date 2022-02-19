import json
import csv

def convertFile():
    json_file = open('./data/Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.json', 'r')
    data = json.load(json_file)
    keys = data.keys()
    values = data.values()

    for val in values:
        if type(val) == list:
            headers = handleTheList(val)
            for header in headers:
                keys.append(header)
    print(len(data.keys()))
    print(len(keys))
    
    csv_data = open('./data/Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.csv', 'w')
    csv_writer = csv.writer(csv_data)
    
    csv_data.close()
    json_file.close()


def handleTheList(listOfVals):
    keys = []
    for value in listOfVals:
        value_keys = handleDicts(value)
        for key in value_keys:
            keys.append(key)
    return keys


def handleDicts(dictionary):
    dict_keys = []

    return dict_keys

