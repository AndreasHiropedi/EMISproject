import json
import csv

def convertFile():
    # load the file and retrieve its contents
    json_file = open('./data/Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.json', 'r')
    data = json.load(json_file)
    keys = list(data.keys())
    values = data.values()

    # identify all the dictionary keys in the file contents
    for val in values:
        # after looking at all the files, they all seem to have one entry as a list
        # which has several dictionaries. the other entries are single value strings
        if type(val) == list:
            # for the list, we will handle a special case using separate functions
            headers = handleTheList(val)
            for header in headers:
                keys.append(header)

    # writing to a CSV file, which will store the equivalent information of the JSON file
    # but in a tabular format
    csv_data = open('./data/Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.csv', 'w')
    csv_writer = csv.writer(csv_data)
    # add all the columns
    csv_writer.writerow(keys)
    # and the data
    
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
    dict_keys = list(dictionary.keys())
    dict_values = dictionary.values()
    for value in dict_values:
        if type(value) == dict:
            headers = handleDicts(value)
            for header in headers:
                dict_keys.append(header)
    return dict_keys

