import json
import csv


# handles single file conversions
def convertFile():
    # load the file and retrieve its contents
    json_file = open('./data/Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.json', 'r')
    data = json.load(json_file)
    keys = list(data.keys())
    values = data.values()
    # this will store all the individual values, for every single key in the file
    entries = []

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
    csv_data = open('./csv_data/Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.csv', 'w')
    csv_writer = csv.writer(csv_data)
    # add all the columns
    csv_writer.writerow(keys)
    # and the values for those columns
    for val in values:
        if type(val) == list:
            vals = handleListValues(val)
            for item in vals:
                entries.append(item)
        else:
            entries.append(val)
    csv_writer.writerow(entries)
    # closing everything at the end to save all changes
    csv_data.close()
    json_file.close()


# in case the value of the key is a list
# we need to identify if that list has any dictionaries
# and any potential keys
def handleTheList(listOfVals):
    keys = []
    for value in listOfVals:
        value_keys = handleDicts(value)
        for key in value_keys:
            keys.append(key)
    return keys


# in case there is a dictionary in any of the values in the file
# the keys need to be accounted for
def handleDicts(dictionary):
    dict_keys = list(dictionary.keys())
    dict_values = dictionary.values()
    for value in dict_values:
        if type(value) == dict:
            headers = handleDicts(value)
            for header in headers:
                dict_keys.append(header)
    return dict_keys


# if the value is a list, the individual values must be retrieved
# if there are dictionaries in the list, individual values per key need to be distinguished 
# and accounted for
def handleListValues(listForValues):
    values = []
    for value in listForValues:
        individual_values = handleDictValues(value)
        for item in individual_values:
            values.append(item)
    return values


# # if there are dictionaries, individual values per key need to be distinguished and accounted for
def handleDictValues(dictionary):
    single_values = []
    dict_values = dictionary.values()
    for value in dict_values:
        if type(value) == dict:
            items = handleDictValues(value)
            for item in items:
                single_values.append(item)
        elif type(value) == list:
            items = caseValueisList(value)
            for item in items:
                single_values.append(item)
        else:
            single_values.append(value)
    return single_values


# if the value is a list, this could be a list of individual items
# or a list of dictionaries, so a distinction needs to be made
def caseValueisList(value):
    outputs = []
    for item in value:
        if type(item) == dict:
            entries = handleDictValues(item)
            for entry in entries:
                outputs.append(entry)
        else:
            outputs.append(item)
    return outputs
